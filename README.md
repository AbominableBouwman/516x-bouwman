## Human Reaction Time
Whenever you see something, there is a slight delay before you can react to it. The delay is measurable and variable across many different factors such as race, sex, age, and various environmental factors. The current research tests the impact of different input methods as a significant impact factor for individual reaction time. 

(More Lit review on definitions and previous results to be added later)

## Testing Methods  
Data is being collected using a module created on Scratch, a free game/programming tool designed and maintained by the Lifelong Kindergarten group at the [MIT Media Lab](https://scratch.mit.edu/about). This module was designed and created by Elijah Bouwman as part of a graduate course at Iowa State University, Industrial Engineering 577: Human Factors. The module provides the participants an ID used to track their data across attempts. The module then asks participants to choose an input or control method from a list of three: Mouse, Keyboard, Touch Screen. The module then shows a red screen, and after a minimum of two seconds, the screen will light up green and ask the participant to interact with the screen. The time the green screen is visible is logged in milliseconds, and the test is repeated until five successful data points have been gathered. The testing process is repeated for each method of control a total of 15 times. 

The module is publically available at [https://scratch.mit.edu/projects/603093411/](https://scratch.mit.edu/projects/603093411/)

The participants are then asked to provide the participant ID given to them in a google forum to collect summary data points such as ethnicity, sex, age, and familiarity with technology. The responses for this form can be found at [Drive Link](https://docs.google.com/spreadsheets/d/11fNLn7-7c9rlHEPKpTqid2YDDLQVBW_QTY4EYnlaYXQ/edit?usp=sharing) 
The Qestionaires are located at [Link](https://docs.google.com/forms/d/e/1FAIpQLSeYyGLxR2mH17MzsrR1sm4dumOfsZECpoG1EHJ0FHw2-jYiwA/viewform?usp=sf_link) and [Link](https://docs.google.com/forms/d/e/1FAIpQLScREfhTiPqMwQLZ-XsUYUHF3L7s-LemZivaJv6_3uhFI8_K6Q/viewform?usp=sf_link)




## Workflow  
![image](https://user-images.githubusercontent.com/64162566/142462497-994e1e03-6f15-475b-a22f-378929688296.png)

This workflow is designed to explain the process of going from experimental data to a publishable article. The following links will walk through this process step by step, and each will export data at various stages for testing and transparency.  

1. [Data Collection](https://docs.google.com/spreadsheets/d/11fNLn7-7c9rlHEPKpTqid2YDDLQVBW_QTY4EYnlaYXQ/edit?usp=sharin) - [Github Link](JupyterNotebooks/Demographic Information.xlsx)
2. [Data Processing](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/9535f6ebfc1931f22422a895dc3358a248cdc575/JupyterNotebooks/Data%20Cleaning%20and%20Sorting.ipynb)
3. [Data Exploration](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/9535f6ebfc1931f22422a895dc3358a248cdc575/JupyterNotebooks/Data%20Exploration.ipynb)
4. [Model Prediction](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/9535f6ebfc1931f22422a895dc3358a248cdc575/JupyterNotebooks/Classification%20of%20Reaction%20Time%20Data.ipynb)
5. (Bonus) [Data Visualization](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/9535f6ebfc1931f22422a895dc3358a248cdc575/JupyterNotebooks/Data%20Visualization.ipynb)


## Class Excercise
Follow along with this partially filled [notebook](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/9535f6ebfc1931f22422a895dc3358a248cdc575/JupyterNotebooks/Class%20Activity%21%20%28Empty%29.ipynb).   
or this fully completed one - [link](https://nbviewer.org/github/AbominableBouwman/516x-bouwman/blob/9535f6ebfc1931f22422a895dc3358a248cdc575/JupyterNotebooks/Class%20Activity%21%20%28Filled%29.ipynb)

For this activity, you will download the notebooks and use the prediction model to determine which input method would be best for you based on your demographic information. We will then collect information using the testing module and compare the results to the predicted model.

