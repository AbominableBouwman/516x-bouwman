## Human Reaction Time
Whenever you see something, there is a slight delay before you can react to it. The delay is measurable and variable across many different factors such as race, sex, age, and various environmental factors. The current research tests the impact of different input methods as a significant impact factor for individual reaction time. 

(More Lit review on definitions and previous results to be added later)

## Testing Methods  
Data is being collected using a module created on Scratch, a free game/programming tool designed and maintained by the Lifelong Kindergarten group at the [MIT Media Lab](https://scratch.mit.edu/about). This module was designed and created by Elijah Bouwman as part of a graduate course at Iowa State University, Industrial Engineering 577: Human Factors. The module provides the participants an ID used to track their data across attempts. The module then asks participants to choose an input or control method from a list of three: Mouse, Keyboard, Touch Screen. The module then shows a red screen, and after a minimum of two seconds, the screen will light up green and ask the participant to interact with the screen. The time the green screen is visible is logged in milliseconds, and the test is repeated until five successful data points have been gathered. The testing process is repeated for each method of control a total of 15 times. 

The module is publically available at [https://scratch.mit.edu/projects/579740360/](https://scratch.mit.edu/projects/579740360/) (This module is not currently finished)

The participants are then asked to provide the participant ID given to them in a google forum to collect summary data points such as race, sex, age, and familiarity with technology. 




## Workflow  
![image](https://user-images.githubusercontent.com/64162566/142095286-ef9170f5-a87f-4212-a7e4-4458cd858f83.png)

This workflow is designed to explain the process of going from experimental data to a publishable article. The following links will walk through this process step by step, and each will export data at various stages for testing and transparency.  

1. [Data Collection](Data scraping Python Script/Export the collected data here)
2. [Data Processing](This will go to the Processing notebook)
3. [Data Exploration](This will go to the Exploration notebook)
4. [Model Prediction](This will go to the Visualization notebook)

The reaction times are logged in a separate cloud variable and can be collected from various URLs associated with the module. These can be grabbed with a python script and stored in a usable format. 

## Class Excercise
Follow along with this [notebook](Class activity). 

For this activity, you will download the notebooks and use the prediction model to determine which input method would be best for you based on your demographic information. We will then collect information using the testing module and compare the results to the predicted model.

