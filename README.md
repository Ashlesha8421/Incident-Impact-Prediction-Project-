![Incident Impcat Prediction](https://github.com/Ashlesha8421/Incident-Impact-Prediction-Project-/blob/Ashlesha_Datir/Incident%20Impcat%20Prediction%20GIF.gif)


# Incident-Impact-Prediction-Project-
* Objective : 
             The objective of the analysis is to predict an impact on the basis of 
event log of an incident management process extracted from a service desk platform of an IT company.

# Business Problem :
  *  The Business Problem is to predict the impact of the incident raised by the customer.

# Data Set Details : 
 To check data description please click [ data Set Details ](https://github.com/Ashlesha8421/Incident-Impact-Prediction-Project-/blob/Ashlesha_Datir/Data/DataSet_Description.pdf)
 
 # Exploratory Data Analysis (EDA) :
 EDA is used for seeing what the data can tell us before the modeling task.

# Missing Value Treatment -
* We ues missing value imputation for numeric variable using backfill (use next valid observation to fill gap)
* We use missing value imputation for categorical variable using mode
![MissingValueTreatment](https://github.com/Ashlesha8421/Incident-Impact-Prediction-Project-/blob/Ashlesha_Datir/Images/MissingValueTreatment.png)

# Feature Selection :
Feature selection is a process where you automatically select those feature in your data that contribute most to prediction variables in which you are interested. The benifits of performing feature selections
- To avoid overfitting 
- Reduce training time
### Here I used  these techinques of feature selections :
1) Chi square test.
2) Mutule information.
3) Decision Tree classifier.
 
# Balancing The Data :
 From the below figure, we can see that there are two graph where 1st figure shows data is imbalance and other is balanced.
 and Balancing the data is done by using SMOTEomek.
Original data set shape Counter({1: 1415, 2: 54437, 3:1610)
Resample data set shape Counter({1: 54437, 2: 54437, 3:54437})

![Balance&Imbalance](https://github.com/Ashlesha8421/Incident-Impact-Prediction-Project-/blob/Ashlesha_Datir/Images/Balance%26Imbalance.png)

# Accuracy of models :
Model accuracy is defined as the number of classifications a model correctly predicts divided by the total number of predictions made. 
.It's a way of assessing the performance of a model, but certainly not the only way.


![Accuracyofmodels](https://github.com/Ashlesha8421/Incident-Impact-Prediction-Project-/blob/Ashlesha_Datir/Images/Accuracyofmodels.png)

# Model Building :
We used different different models but Finalized model is following below :

# RandomForestClassifier :
As the name suggests, "Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive  accuracy of that dataset." Instead of relying on one decision tree, the random forest takes the prediction from each tree and based on the majority votes of predictions,and it predicts the final output. for more info [Click Here ](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

# Deployment :
Finally I used Streamlit App framework to deploy my application.

# Challenges faced ?
* Balancing the Imbalance Data
* Missing Values
* To increase the Model Accuracy

# How did you overcome ?
* By using SMOTETomek
* Impute data using Mode and Num data using Bfill Method

# NOTE- How to run this
 * 1.Open Anaconda Prompt
* 2.Type 'streamlit run application2.py'
* 3.It will run successfully
(if not, open application2.py and just change the path of images and pickle file according to location)
