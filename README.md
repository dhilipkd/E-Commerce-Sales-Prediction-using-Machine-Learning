# Sales-Prediction-using-Machine-Learning
This project builds a complete sales prediction model using Linear Regression, Random Forest, and XGBoost. A full ML pipeline is implemented with data cleaning, preprocessing, model training, hyperparameter tuning, evaluation, and saving the best model.

## Features
- Data cleaning and feature preprocessing
- Scaling numerical features and encoding categorical features
- Model training using three regression algorithms
- Hyperparameter tuning with GridSearchCV
- Model evaluation using R2, MAE, MSE, and RMSE
- Actual vs Predicted visualization
- Saving the best model as a .pkl file

## Tech Stack
Python, Pandas, NumPy, Scikit-Learn, XGBoost, Matplotlib, Seaborn, Joblib

## How It Works
1. Load and clean dataset  
2. Build preprocessing pipeline  
3. Train multiple models  
4. Perform GridSearchCV tuning  
5. Compare performance metrics  
6. Save best model


<img width="1185" height="901" alt="image" src="https://github.com/user-attachments/assets/3564d42c-67b7-428e-93c2-073a6f46ca56" />

<img width="1172" height="900" alt="image" src="https://github.com/user-attachments/assets/00dde169-9184-4c87-a1ba-a35baf9a1345" />

<img width="1173" height="905" alt="image" src="https://github.com/user-attachments/assets/c30723d7-09bf-4fd0-a0de-f9344e549fc1" />


## Save Best Model
```python
import joblib
joblib.dump(best_model, "best_model.pkl")
```

## Results
The script prints:
- Best model  
- Best R2 score  
- Model comparison summary

