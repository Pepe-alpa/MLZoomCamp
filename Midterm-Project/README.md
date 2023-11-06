# *Status of Cirrhosis Desease*

## Problem description
Liver cirrhosis is a chronic and progressive medical condition characterized by the scarring of liver tissue, which impairs liver function. It can be caused by various factors, including chronic liver diseases (e.g., hepatitis and fatty liver disease), excessive alcohol consumption, and other underlying health conditions. Liver cirrhosis can lead to serious complications and, in some cases, requires liver transplantation.

## Liver Cirrhosis Study
The data provided is sourced from a Mayo Clinic study on primary biliary cirrhosis (PBC) of the liver carried out from 1974 to 1984. During 1974 to 1984, 424 PBC patients referred to the Mayo Clinic qualified for the randomized placebo-controlled trial testing the drug D-penicillamine. Of these, the initial 312 patients took part in the trial and have mostly comprehensive data. The remaining 112 patients didn't join the clinical trial but agreed to record basic metrics and undergo survival tracking. Six of these patients were soon untraceable after their diagnosis, leaving data for 106 of these individuals in addition to the 312 who were part of the randomized trial.

## Justification
The significance of this project lies in the importance of understanding the risk of death that a patient with liver cirrhosis has. The objective is to obtain a prediction of the risk of death status depending on the values of various metrics in the patient with liver cirrhosis.

## Data
The data used in this project is from [Cirrhosis Patient Survival Prediction](https://www.kaggle.com/datasets/joebeachcapital/cirrhosis-patient-survival-prediction) dataset, which can be found in [Kaggle](https://www.kaggle.com/).

Take a thorough look at the characteristics presented in the dataset, including their descriptions and the unit of measurement, if relevant.

| Feature Name | Feature Description |
| :----------: | :-----------------: |
| ID   | Unique identifier |
| N_Days | Number of days between registration and the earlier of death, transplantation or study analysis |
| Status   | Status of the patient; C(censored), CL (censored due to liver tx) or D(death) |
| Drug   | Type of drug D-penicilamine or placebo |
| Age   | Age of the patient in days |
| Sex   | M (male), F (female) |
| Ascites   | Presence of ascites N(no), or Y (yes) |
| Hepatomegaly   | Presence of hepatomegaly N (no), Y (yes) |
| Spiders   | Presence of spiders N (no), Y (yes) |
| Edema   |Presence of edema N (no edema and no diuretic therapy for edema), S (edema present without diuretics) or Y (edema despite diuretic therapy) |
| Bilirubin   | Serum bilirubin |
| Cholesterol   | Serum cholesterol |
| Albumin   | Albumin |
| Copper   | Urine copper |
| Alk_Phos   | Alkaline phosphatase |
| SGOT   | SGOT |
| Tryglicerides   | Tryglicerides |
| Platelets   | Platelets per cubic |
| Prothrombin   | Prothrombin time |
| Stage   | Histologic stage of desease (1,2,3 or 4) |


## Getting Started

This is a set of instructions on setting up this project locally. To get a local copy up and running follow these simple example steps.

Prerequisites:

- Python
- Pipenv
- Docker 

### Installing Dependencies

You can install the dependencies with pipenv, as they are specified in the `Pipfile` and `Pipfile.lock`, by running the following commands:

```
pipenv install
pipenv shell
```

### Building the model

You have the option to execute either the `train.py` file  to carry out all the necessary steps for training the final model used in this project.

To initiate the model training, you can use the following command:

```
python train.py
```

### Serving the model (Locally)

To serve the model with Docker:

1. **First install docker:**

    - *Download Docker Desktop (Windows user)*
        - Visit the official Docker website: [Docker Desktop](https://www.docker.com/products/docker-desktop).
        - Click on the "Get Docker Desktop for Windows" button.
        - You will be redirected to the download page. Download the installation file here.

    - *Install Docker Desktop:*
        - Run the installation file you just downloaded.
        - Follow the installer instructions to complete the installation.

    - *Launch Docker Desktop:*
        - Once installed, look for Docker Desktop in your start menu and run it.
    
    - *Verify the Installation:*
        - Open a terminal and run the following command to verify that Docker is installed correctly:
        
            ```bash
            docker --version
            ```
        - You can also run:
            ```bash
            docker run hello-world
            ```
        - This will download a small image, run it, and you should see a message indicating that Docker is working correctly.
    
    And that's it! Now you should have Docker installed and ready to use on your Windows system.

2. **Click and initialize the DOCKER DESKTOP app after installing it:**

    - Maybe it asks you to update wsl. Open your terminal and run the following command:
        ```bash
        wsl --update
        ```

3. **Build the Docker image and run it:**

    - *Build the Docker image*
        - Open a new terminal, enter the 'Midterm_Project' folder and run the following command:
            ```
            docker build -t zoomcamp-midterm-project-cirrhosis .
            ```
        
        - REMEMBER THE DOT (.) IN THE LAST COMMAND!!!This command builds a Docker image from the provided files.

    - *Run the previous image*
        ```
        docker run -it --rm -p 9696:9696 zoomcamp-midterm-project-cirrhosis
        ```
        - This command runs a container based on the previously built image. Maps port 9696 on the host system to port 9696 on the container. This is important if the application inside the container is listening on port 9696.

### Testing the model

Finally, you can test the model. Serving the model locally, open another terminal, and:

```
python predict_test.py
```

## Citation

1. Dickson,E., Grambsch,P., Fleming,T., Fisher,L., and Langworthy,A.. (2023). Cirrhosis Patient Survival Prediction. UCI Machine Learning Repository. https://doi.org/10.24432/C5R02G.
