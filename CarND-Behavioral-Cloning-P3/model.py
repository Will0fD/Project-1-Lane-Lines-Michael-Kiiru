import csv
import cv2
import numpy as np

# open the csv and read in and store every line
lines = []
path = '/home/carnd/data/driving_log.csv'
with open(path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for line in reader:
        lines.append(line)
# create 2 arrays: steering angles (w/left and right adjustments)...
# ...and first person images
# creates 3 times as much data
images = []
measurements = []
correction = 0.25
for line in lines:
    for i in range(3):
        source_path = line[i]
        filename = source_path.split('/')[-1]
        current_path = '/home/carnd/data/IMG/' + filename
        image = cv2.imread(current_path)
        images.append(image)
    measurement = float(line[3])
    center = measurement
    steering_lft = measurement + correction
    steering_rght = measurement - correction
    measurements.extend([center, steering_lft, steering_rght])

# flip every image horizontally to simulate driving in the opposite direction
# creates 2 times as much data
augmented_images, augmented_measurements = [], []
for image,measurement in zip(images, measurements):
    augmented_images.append(image)
    augmented_measurements.append(measurement)
    augmented_images.append(cv2.flip(image,1))
    augmented_measurements.append(-measurement)

X_train = np.array(augmented_images)
y_train = np.array(augmented_measurements)

from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D

# NVIDIA model architecture
model = Sequential()
# normalize image between 0 and 1 and shift center to 0 (-0.5 and 0.5)
model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=(160,320,3)))
# crop top 70 pixels and bottom 25 pixels
model.add(Cropping2D(cropping=((70,25),(0,0))))
model.add(Convolution2D(24,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(36,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(48,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(64,3,3,activation="relu"))
model.add(Convolution2D(64,3,3,activation="relu"))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=5)

model.save('model.h5')
