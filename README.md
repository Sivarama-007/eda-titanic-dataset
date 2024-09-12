# EDA on Titanic Dataset 🚢

This repository contains a project focused on performing data cleaning and exploratory data analysis (EDA) on the Titanic dataset. The goal of this task is to understand and analyze the dataset to identify patterns and trends.

## Table of Contents
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Dataset](#dataset)
4. [Code and Analysis](#code-and-analysis)
5. [Results](#results)
6. [How to Run](#how-to-run)
7. [License](#license)

## Project Description
The project involves:
- Performing data cleaning on the Titanic dataset.
- Conducting exploratory data analysis to uncover insights.
- Visualizing various aspects of the data to understand relationships between variables.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/eda-titanic-dataset.git
    ```
2. Navigate into the project directory:
    ```bash
    cd eda-titanic-dataset
    ```
3. Install the required Python libraries using:
    ```bash
    pip install -r requirements.txt
    ```

## Dataset
The dataset used for this project is the Titanic dataset, which can be downloaded from [Kaggle](https://www.kaggle.com/c/titanic/data). If included, the dataset file is `train.csv`.

## Code and Analysis
The notebook (`.ipynb`) and Python script (`.py`) files include the code for:
- Data cleaning:
  - Handling missing values.
  - Encoding categorical variables.
  - Dropping unnecessary columns.
- Exploratory data analysis:
  - Visualizations of survival distribution.
  - Survival rates by gender, passenger class, and embarkation location.
  - Age distribution and correlation heatmap.

## Results
Key visualizations from the analysis include:
- **Survival Distribution**:
  ![Survival Distribution](survival_distribution.png)
- **Survival Rate by Gender**:
  ![Survival Rate by Gender](survival_rate_by_gender.png)
- **Age Distribution**:
  ![Age Distribution](age_distribution.png)
- **Survival Rate by Passenger Class**:
  ![Survival Rate by Passenger Class](survival_rate_by_class.png)
- **Correlation Heatmap**:
  ![Correlation Heatmap](correlation_heatmap.png)
- **Survival Rate by Embarked Location**:
  ![Survival Rate by Embarked Location](survival_rate_by_embarked.png)

## How to Run
1. To run the project, open the `eda_titanic.ipynb` file in Google Colab or Jupyter Notebook and execute the cells step-by-step.
2. If using the Python script:
    ```bash
    python eda_titanic.py
    ```

## License
This project is licensed under the MIT License.
