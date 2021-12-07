## Introduction
When a hazardous event begins to escalate into a mishap event, individuals may respond quickly to the situation to limit the impacts of the mishap or possibly stop the event from propagating altogether. This study proposes software to test an individuals' reaction time during onset events with various input methods. This proposed software design includes developing clear criteria for evaluating this or similar software. These criteria will be used to analyze reaction time data gathered through a prototype module created in Scratch, a visual coding service, and the Lifelong Kindergarten Group project at the MIT Media Lab (n.d). This project will impact various industries, including military, manufacturing, and agriculture, but this study will focus mainly on the manufacturing sector for reaction-based events. 

## Problem
In case of manufacturing machine failure, such as a CNC mill or lathe, or process error that needs to be corrected rapidly, which type of interface control produces the least response delay from a human?

## Research Questions
1. Which type of interface control produces the least response delay from a human?   
2. What is the best way to model and detect the difference in response times?
3. To what extent was the prototype able to gauge the reaction time of participants?

## Human Reaction Time
Whenever you see something, there is a slight delay before you can react to it. The delay is measurable and variable across many different factors such as race, sex, age, and various environmental factors. The current research tests the impact of different input methods as a significant impact factor for individual reaction time.  
(For more information and a more detailed write up see the file "IE577_Project_Final_ReactionTimeMethod" in the main directory or linked [here](IE577_Project_Final_ReactionTimeMethod)) 

## Testing Methods  
Data is being collected using a module created on Scratch, a free game/programming tool designed and maintained by the Lifelong Kindergarten group at the [MIT Media Lab](https://scratch.mit.edu/about). This module was designed and created by Elijah Bouwman as part of a graduate course at Iowa State University, Industrial Engineering 577: Human Factors. The module provides the participants an ID used to track their data across attempts. The module then asks participants to choose an input or control method from a list of three: Mouse, Keyboard, Touch Screen. The module then shows a red screen, and after a minimum of two seconds, the screen will light up green and ask the participant to interact with the screen. The time the green screen is visible is logged in milliseconds, and the test is repeated until five successful data points have been gathered. The testing process is repeated for each method of control a total of 15 times. 

The module is publically available at [https://scratch.mit.edu/projects/603093411/](https://scratch.mit.edu/projects/603093411/)

The participants are then asked to provide the participant ID given to them in a google forum to collect summary data points such as ethnicity, sex, age, and familiarity with technology. The responses for this form can be found at [Drive Link](https://docs.google.com/spreadsheets/d/11fNLn7-7c9rlHEPKpTqid2YDDLQVBW_QTY4EYnlaYXQ/edit?usp=sharing) 
The Qestionaires are located at [Link](https://docs.google.com/forms/d/e/1FAIpQLSeYyGLxR2mH17MzsrR1sm4dumOfsZECpoG1EHJ0FHw2-jYiwA/viewform?usp=sf_link) and [Link](https://docs.google.com/forms/d/e/1FAIpQLScREfhTiPqMwQLZ-XsUYUHF3L7s-LemZivaJv6_3uhFI8_K6Q/viewform?usp=sf_link)




## Workflow  
![image](https://user-images.githubusercontent.com/64162566/144971081-d756de7a-816f-45ee-9c05-41d1e68b53c5.png)

This workflow is designed to explain the process of going from experimental data to a publishable article. The following links will walk through this process step by step, and each will export data at various stages for testing and transparency.  

1. [Data Collection](https://docs.google.com/spreadsheets/d/11fNLn7-7c9rlHEPKpTqid2YDDLQVBW_QTY4EYnlaYXQ/edit?usp=sharin)
2. [Data Processing](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/cae5b450f6221f1b8d79e74ef9d5ba3673212f80/JupyterNotebooks/Data%20Cleaning%20and%20Sorting.ipynb)
3. [Data Exploration](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/4f61c3ac8d07efb8aa7262f3558ee3bb75dee454/JupyterNotebooks/Data%20Exploration.ipynb)
4. [Model Prediction](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/cae5b450f6221f1b8d79e74ef9d5ba3673212f80/JupyterNotebooks/Classification%20of%20Reaction%20Time%20Data.ipynb)
5. (Bonus) [Data Visualization](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/9535f6ebfc1931f22422a895dc3358a248cdc575/JupyterNotebooks/Data%20Visualization.ipynb)

## Conclusion for Data Exploration  

Let us start with our research questions:  

1. Which type of interface control produces the least response delay from a human?  

RQ1: Since the prototype could not detect any significant results from the difference in methods, we will use the human factors principles to develop a new testing model and test again.  

2. What is the best way to model and detect the difference in response times?  

RQ2: Establishing a linear regression model with regularly fitted data with sex + ethnicity + age + round + method produced fairly even residual and predicted vs. actual plots, but again the shortcomings of the data collection method increase the difficulty of making predictive models.  

3. To what extent was the prototype able to gauge the reaction time of participants?  

RQ3: Our model failed to produce any statistically significant results. Do not use Scratch for Reaction Time Data. It was discovered after testing that Scratch runs at a locked 30 frames per second, meaning the screen only updates once every .033 seconds. This source of error would impact any method tested in the Scratch software. For example, the mean human reaction time is 0.371688 for Mouse (after the removal of outliers), a nearly 10% error when the screen decides to update adds an undo amount of error to the test results.   


## Class Excercise
Follow along with this partially filled [notebook](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/9535f6ebfc1931f22422a895dc3358a248cdc575/JupyterNotebooks/Class%20Activity%21%20%28Empty%29.ipynb).   
or this fully completed one - [link](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/9535f6ebfc1931f22422a895dc3358a248cdc575/JupyterNotebooks/Class%20Activity%21%20%28Filled%29.ipynb)

For this activity, you will download the notebooks and use the prediction model to determine which input method would be best for you based on your demographic information. We will then collect information using the testing module and compare the results to the predicted model.

## ABE 516x Discussion
This project makes use of various data science methods. There is a strong use of the merge and melt functions in the data cleaning document. Without these functions, there would be no easy way to match demographic data up with the response time data or turn the five rounds into multiple entries for easier data analysis. This study had intended to use data scraping to grab the data from Scratch, but that fell through as it was not accessible on the server-side. This class prepared the study for quick and easy visualizations of the exploratory data. The Ability to filter groups to make an insightful discovery in the Data Exploration file was very useful. In the same file, OLS and ANOVA modules are used, and while no significance was found, the methodology is sound. The use of SVM to determine the input method based on other characteristics is mostly for fun and to practice the implementation of SVM. This study pulled information from various packages and implemented them throughout the process. The documentation was vital to fixing errors and defining variables throughout the process.        

## FAIR Statement  
This project strives to uphold FAIR principles to that end:  

To be Findable: The columns are transformed to make each piece of data easy to locate within the original data and care has been taken to match data up properly when merging or transforming.  
  
To be Accessible: The data is accessable to all and each piece is noted for when it is moved and stored. All data is accessiable in this repository or linked to where it is stored.  
  
To be Interoperable: Clear headings and language are used in all possible locations for the data. This is consistent and there is an attempt to comment through the data processing process. The data uses accessible language for the coding portion to allow for readability.   
  
To be Reusable: All data is availiable for use by other researchers to check the conclusions drawn in this study or to be used for another study.
  
This project can be reproduced using the workflow provided. This will only work if you use the headers from the Google form or if they are formatted similarly. All of the figures can be reproduced from the data given or changed to account for new information if the Google form is updated with more results.  
  
