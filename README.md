# E-Commerce Sales Prediction using Machine Learning
This project builds an end-to-end E-Commerce Sales Prediction system using Machine Learning.
It compares multiple regression models, applies proper preprocessing pipelines, tunes hyperparameters, evaluates performance, and deploys the best model using Streamlit for real-time predictions.

## Key Features
- End-to-end ML pipeline (data cleaning → deployment)

- Numerical feature scaling using StandardScaler

- Categorical feature encoding using OneHotEncoder

- Model training with:

    - Linear Regression

    - Random Forest Regressor

    - XGBoost Regressor

- Hyperparameter tuning using GridSearchCV

- Model evaluation using:

    - R² Score

    - MAE

    - MSE

    - RMSE

- Actual vs Predicted Sales visualization

- Best model saved as a .pkl file

- Interactive Streamlit web app for prediction


## Machine Learning Workflow
1. Load and clean the dataset

2. Drop irrelevant and identifier columns

3. Handle missing values and duplicates

4. Split features into numerical and categorical columns

5. Build preprocessing pipeline using ColumnTransformer

6. Train multiple regression models

7. Perform hyperparameter tuning with GridSearchCV

8. Compare model performance

9. Save the best performing model

10. Deploy the model using Streamlit


## Tech Stack
- Programming Language: Python

- Libraries:

    - Pandas, NumPy

    - Scikit-Learn

    - XGBoost

    - Matplotlib, Seaborn

    - Joblib

- Deployment: Streamlit

## Model Evaluation Metrics
The models are evaluated using:

- R² Score – Model accuracy

- MAE – Mean Absolute Error

- MSE – Mean Squared Error

- RMSE – Root Mean Squared Error

A comparison summary is printed to identify the best model.

## Save Best Model
```python
import joblib
joblib.dump(best_model, "best_model.pkl")
```

## Streamlit Web Application
The Streamlit app allows users to:

- Enter order and product details

- Predict sales amount instantly

- View results in a clean and interactive UI

Example inputs include:

- Year

- Shipment Days

- Ship Mode

- Segment

- Region

- Category

- Sub-Category

- Quantity

- Discount


## Results
- Best performing model is selected based on R² score

- Displays:

    - Best Model Name

    - Best R² Score

    - Model comparison summary table

