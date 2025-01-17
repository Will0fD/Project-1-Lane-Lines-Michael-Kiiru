#**Traffic Sign Recognition** 

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/visualization.jpg "Visualization"
[image4]: ./google_pics/50.jpg "Traffic Sign 1"
[image5]: ./google_pics/bike_crossing.jpg  "Traffic Sign 2"
[image6]: ./google_pics/road_work.jpg  "Traffic Sign 3"
[image7]: ./google_pics/slippery-road.jpg  "Traffic Sign 4"
[image8]: ./google_pics/straight-or-left.jpg  "Traffic Sign 5"

## Rubric Points
###Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
###Writeup / README

You're reading it! and here is a link to my [project code](https://github.com/Will0fD/SDCND/blob/master/CarND-Traffic-Sign-Classifier-Project/Traffic_Sign_Classifier.ipynb)

###Data Set Summary & Exploration

####1. Provide a basic summary of the data set and identify where in your code the summary was done. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

The code for this step is contained in the second code cell of the IPython notebook.  

I used the pandas library to calculate summary statistics of the traffic
signs data set:

* The size of training set is 39209
* The size of test set is 12630
* The shape of a traffic sign image is (32, 32, 3)
* The number of unique classes/labels in the data set is 43

####2. Include an exploratory visualization of the dataset and identify where the code is in your code file.

The code for this step is contained in the third & fourth code cell of the IPython notebook.  

Here is an exploratory visualization of the data set. It is a bar chart showing how the data ...

![alt text][image1]

###Design and Test a Model Architecture

####1. Describe how, and identify where in your code, you preprocessed the image data. What tecniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc.

The code for this step is contained in the fifth code cell of the IPython notebook.

For preprocessing, I decided to only shuffle the data.

####2. Describe how, and identify where in your code, you set up training, validation and testing data. How much data was in each set? Explain what techniques were used to split the data into these sets. (OPTIONAL: As described in the "Stand Out Suggestions" part of the rubric, if you generated additional data for training, describe why you decided to generate additional data, how you generated the data, identify where in your code, and provide example images of the additional data)

The code for splitting the data into training and validation sets is contained in the sixth code cell of the IPython notebook.  

To cross validate my model, I randomly split the training data into a training set and validation set. I did this by using the train_test_split funtion to allocate 20% of the train.p data set for validation. The rest is left as training data. All of the data from the test.p data set is used for the test set. 

My final training set had 31367 number of images. My validation set and test set had 7842 and 12630 number of images.

####3. Describe, and identify where in your code, what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

The code for my final model is located in the seventh cell of the ipython notebook. 

My final model consisted of the following layers:

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x3 RGB image   							| 
| Convolution 3x3     	| 1x1 stride, valid padding, outputs 28x28x6 	|
| Dropout   | Keep probability 70%          |
| RELU					|					Activation							|
| Max pooling	      	| 2x2 stride,  outputs 14x14x6 				|
| Convolution 3x3	    | 1x1 stride, valid padding, outputs 10x10x16     									|
| RELU     |      Activation      |
| Convolution 3x3     | 1x1 stride, valid padding, outputs 7x7x50            |
| RELU     |     Activation       |
| Max pooling        | 2x2 stride,  outputs 3x3x50     |
| Flatten		| Outputs 450        									|
| Fully connected		| Outputs 120        									|
| RELU     |     Activation       |
| Fully connected  | Outputs 84                |
| RELU     |     Activation       |
| Fully connected  | Outputs 43                |
| Softmax  |             |


####4. Describe how, and identify where in your code, you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

The code for training the model is located in the ninth, tenth, and eleventh cells of the ipython notebook. 

To train the model, I used an Adam optimizer, batch size of 128, 10 epochs, a learning rate of 0.001.

####5. Describe the approach taken for finding a solution. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

The code for calculating the accuracy of the model is located in the eleventh and twelfth cells of the Ipython notebook.

My final model results were:
* validation set accuracy of 96.4% 
* test set accuracy of 89.9%

If an iterative approach was chosen:
* What was the first architecture that was tried and why was it chosen? 

The first architecture that was chosen was Lenet because it was convenient to start with what was initially given.

* What were some problems with the initial architecture?

It seemed to cap out at a validation accuracy of ~96% and it didn't cross  90% until the 4th epoch.

* How was the architecture adjusted and why was it adjusted? Typical adjustments could include choosing a different model architecture, adding or taking away layers (pooling, dropout, convolution, etc), using an activation function or changing the activation function. One common justification for adjusting an architecture would be due to over fitting or under fitting. A high accuracy on the training set but low accuracy on the validation set indicates over fitting; a low accuracy on both sets indicates under fitting.

I had a high validation accuracy but a low testing accuracy. I experimented with adding pooling and dropout layers to deal with the overfitting. My metric of improved performance before I checked the testing accuracy was in which epoch did the validation accuracy cross 90%.

* Which parameters were tuned? How were they adjusted and why?

After 5 or 6 iterations of trying larger and smaller rates, a learning rate of 0.001 gave me the best performance.

* What are some of the important design choices and why were they chosen? For example, why might a convolution layer work well with this problem? How might a dropout layer help with creating a successful model? 

I chose to add more convolutional layers in order to pick up more features and complexity in the data. I also decided to add pooling and dropout layers to deal with the overfitting issues that my network was experiencing.

###Test a Model on New Images

####1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are five German traffic signs that I found on the web:

![alt text][image4] 

![alt text][image5] 

![alt text][image6] 

![alt text][image7] 

![alt text][image8]

The second image might be difficult to classify because of the rotation of the sign. The 3rd image has trees and vegetation in the background that may add complications, and the 2nd through the 4th all have watermarks as well. 

####2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. Identify where in your code predictions were made. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

The code for making predictions on my final model is located in the sixteenth & seventeenth cells of the Ipython notebook.

Here are the results of the prediction:

| Image			        |     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| Bicycle Crossing      		| Road work   									| 
| Road work     			| Speed limit (80km/h)										|
| Speed limit (50km/h)				| Speed limit (30km/h)											|
| Go straight or left     		| Go straight or left					 				|
| Slippery Road			| Slippery Road      							|


The model was able to correctly guess 2 of the 5 traffic signs, which gives an accuracy of 40%. This compares unfavorably to the accuracy on the test set of 89%.

####3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction and identify where in your code softmax probabilities were outputted. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

The code for making predictions on my final model is located in the sixteenth & seventeenth cells of the Ipython notebook.

For the first image, the model is relatively sure that this is a Road work sign (probability of 0.9987), but the image contains a Bicycle crossing sign. The top five soft max probabilities were

| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 9.987e-01         			| Road work   									| 
| 6.028e-04     				| Speed limit (60km/h)	 										|
| 5.275e-04					| Speed limit (80km/h)											|
| 5.724e-05	      			| Speed limit (20km/h)					 				|
| 3.609e-05				    | Dangerious curve to the right      							|


For the second image, the model is relatively sure that this is a Speed limit (80km/h) sign (probability of 0.9942), but the image contains a Road work sign. The top five soft max probabilities were

| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 9.942e-01       			| Speed limit (80km/h)   									| 
| 2.340e-02     				| Wild animals crossing	 										|
| 2.101e-02					| Bicycles crossing											|
| 7.053e-03	      			| Road work					 				|
| 7.003e-03				    | No passing for vehicles over 3.5 metric tons		|

For the third image, the model is relatively sure that this is a Speed limit (30km/h) sign (probability of 0.9314), but the image contains a Speed limit (50km/h)  sign. The top five soft max probabilities were

| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 9.314e-01       			| Speed limit (30km/h)   									| 
| 6.831e-02     				| Speed limit (80km/h)	 										|
| 2.051e-04					| Speed limit (20km/h)											|
| 3.025e-05      			| Speed limit (50km/h)				 				|
| 1.853e-05				    | Speed limit (60km/h)     							|

For the fourth image, the model is relatively sure that this is a Go straight or left sign (probability of 0.9999999), and the image does contain a Go straight or left sign. The top five soft max probabilities were

| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 9.999999e-01         			| Go straight or left   									| 
| 1.083e-07     				| Roundabout mandatory	 										|
| 5.057e-09					| Keep right											|
| 5.636e-11	      			| Keep left					 				|
| 3.569e-11				    | Turn left ahead      							|

For the fifth image, the model is relatively sure that this is a Slippery road sign (probability of 0.9998), and the image does contain a Slippery road sign. The top five soft max probabilities were

| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 9.998e-01         			| Slippery Road 							| 
| 9.635e-05     				| Children crossing	 										|
| 5.121e-05				| Beware of ice/snow											|
| 3.359e-05	      			| Dangerious curve to the right					 				|
| 2.331e-05				    | Bicycles crossing	      							|
