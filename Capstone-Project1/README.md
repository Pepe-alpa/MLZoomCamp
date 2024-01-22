# *Multi-Class Prediction of obesity levels* 

## Problem:

The problem addresses the multi-class prediction of outcomes related to obesity levels. Obesity is a growing global health concern with significant implications for individual well-being and public health. It is characterized by an excess accumulation of body fat and is associated with an increased risk of various chronic conditions, including cardiovascular diseases, diabetes, and certain types of cancer. Despite the widespread recognition of obesity as a critical health issue, accurately identifying and classifying obesity levels can be a complex task. Traditional methods such as Body Mass Index (BMI) have limitations in capturing the diverse factors contributing to obesity, such as body composition, muscle mass, and distribution of fat.

### Context:

The integration of machine learning models into healthcare has shown promising results in various domains, including disease diagnosis and risk prediction. Developing a classification model for obesity aligns with the broader trend of leveraging data-driven approaches to improve health outcomes.

### Significance:

A precise classification model for obesity levels would enable healthcare professionals to tailor interventions more effectively. This could involve personalized diet and exercise plans, early interventions, and targeted prevention strategies based on an individual's specific risk profile. By identifying individuals at risk of obesity early on and implementing preventive measures, the model can contribute to reducing the economic burden associated with obesity-related healthcare costs. This includes expenses related to medical treatments, hospitalizations, and long-term management of obesity-related conditions.

## Data

The data used in this project is from [Obesity or CVD risk (Classify/Regressor/Cluster)](https://www.kaggle.com/datasets/aravindpcoder/obesity-or-cvd-risk-classifyregressorcluster/data) dataset, which can be found in [Kaggle](https://www.kaggle.com/)

Below is a brief description of the variables that make up the dataset.

| Variable       | Description                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------|
| Gender             | Male or Female.                                                                         |
| Age         | Age.                                                                 |
| Height           | Height in meters.                                                      |
| Weight            | Weight in kg.                                                                               |
| family_history_with_overweight            | Family member suffered or suffers from overweight.                                                                                    |
| FAVC        | Frequent consumption of high caloric food.                      |
| FCVC   | Frequency of consumption of vegetables.                                |
| NCP        | Number of main meals.    |
| CAEC          | Consumption of food between meals.                                             |
| SMOKE      | Smoker or not.                                                                             |
| CH20    | Consumption of water daily in complete liters.                                                                          |
| SCC        | Calories consumption monitoring.                                                                              |
| FAF         | Physical activity frequency.                                                                               |
| TUE       | Time using technology devices.                                                                 |
| CALC           | Consumption of alcohol.      |
| MTRANS  | Transportation used.                                                                        |
| NObeyesdad      | Obesity level deducted. This is the target variable.                                                                      |

## Obesity level deducted. The target variable 

This variable consists of 7 classes, corresponding to different levels of obesity. According to the body mass index, these levels are determined as follows:

•Underweight Less than 18.5 (Corresponding to level 0 in the model's output)

•Normal 18.5 to 24.9 (Corresponding to level 1 in the model's output)

•Overweight 25.0 to 29.9 (Corresponding to level 5 in the model's output)

•Obesity I 30.0 to 34.9 (Corresponding to level 2 in the model's output)

•Obesity II 35.0 to 39.9 (Corresponding to level 3 in the model's output)

•Obesity III Higher than 40 (Corresponding to level 4 in the model's output)

However, the dataset includes one more level, corresponding to level II of overweight. (Corresponding to level 6 in the model's output)



## Getting Started

This is a set of instructions on setting up this project locally. 

Prerequisites. You need to have the following installed:

- Python
- Pipenv
- Docker 

### Installing Dependencies

You have to install the **dependencies** with pipenv (because the version of model XgBoost that i used on this project has to be the same), as they are specified in the `Pipfile` and `Pipfile.lock`, by running the following commands:

```
pipenv install
pipenv shell
```

### Building the model

You have the option to execute either the `train.py` file to carry out all the necessary steps for training the final model used in this project.

To initiate the model training, you can use the following command:

```
python train.py
```

## Serving the model (Locally)

For the purpose of testing the model locally, two files were created (`predict_test.py`, `predict.py`), which serve to load and execute the model, and similarly, submit new input for prediction.

To testing the model:
    
1. Open a new terminal and run the `predict.py` file:
        
```
python predict.py

```
2. At the same time, open another new terminal and run the `predict_test.py` file:
        
```
python predict_test.py
```

3. Now, you can see the response for the new data. It must be: `{'level': 1} Your weight status is NORMAL`.

Also, you can use the model with docker:

1. **First install docker**
2. **Build the docker image:**
   - *Build the docker image*
     - Open a new terminal, enter the 'Capstone-Project1' folder and run the following command:

       ```
       docker build -t capstone-project .
       ```
        
        - REMEMBER THE DOT (.) IN THE LAST COMMAND!!!This command builds a Docker image from the provided files.

    - *Run the previous image*

      ```
      docker run -it --rm -p 9696:9696 capstone-project:latest
      ```
### Testing the model

Finally, you can test the model. At the same time, open another terminal, and:

```
python predict_test.py
```


## Citation 

1. Fabio Mendoza Palechor, Alexis de la Hoz Manotas, (2023). Obesity or CVD risk (Classify/Regressor/Cluster). Kaggle. https://www.kaggle.com/datasets/aravindpcoder/obesity-or-cvd-risk-classifyregressorcluster/data