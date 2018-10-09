# Flood-prediction

Problem stament:

Disaster prevention and prediction
Flood prediction using machine learning approach.

Proposed solution:

A dataset with the amount of rainfall and if a flood had occured in a particular area/state/city, in the previous years, will be used. The dataset will have the rainfall data for a duration of 3 months approx.

Using this dataset, we take average rainfall for every 10 days and plot it on a graph to visualize it.
We take this average data of rainfall, as input to our machine learning model and if it causes a flood or not as the output labels.
We train our model and save it.(depending on some threshold value of average rainfall in the dataset)

Given the input data, for consecutive 10 days, we give this data as an input, and let the model predict, if whether there is a possibility of flooding or not, by setting some threshold in the training data. 

This approach can be made real time prediction and accuracy can be improved with adding more features such as the type of land in that area, the location of the area etc.

Our basic approach for this problem is binary classification, using basic machine learning algorithms(linear regression or logistic regression).
