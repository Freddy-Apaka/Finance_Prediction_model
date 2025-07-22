# Loan Default Prediction Model

This project was developed as part of my internship program with **Xaltius Academy**. The goal was to build and evaluate a machine learning model that predicts whether a loan applicant is likely to default. By using historical loan data, we aimed to support data-driven decision-making in financial services.

## 🔍 Project Objective
The main objective of this project was to create a classification model that predicts the `default_status` of a loan application based on key financial features. A particular focus was placed on:
- Evaluating model accuracy and performance
- Comparing different classification models
- Improving predictive power through feature selection and model tuning

## 🧠 Features Used
The model was trained on a dataset with the following key features:
- `loan_amount`: The total amount of the loan
- `interest_rate`: The interest rate assigned to the loan
- `credit_score`: The credit score of the applicant
- `employment_type_encoded`: The Encoded values of the Employment type (Self-employeed, Full-time, Part-time)
- `income_level_encoded`: Th encoded values of the income leve (Low, Medium, High)

**Target Variable:**
- `default_status`: Indicates whether the applicant defaulted on the loan.

## 🛠️ Tools & Technologies
- Python 🐍
- pandas & NumPy
- scikit-learn
- Matplotlib & Seaborn (for visualization)
- Jupyter Notebook
- PowerPoint (for presentation)
- Excel (for data Wrangling)

## 📈 Model Overview
1. **Logistic Regression** was first applied as a baseline model.
2. **Decision Tree Classifier** was then used to improve accuracy and predictive performance.
3. **Over-Sampling** was used to balance the dataset
4. Results were evaluated using accuracy score, confusion matrix, and feature importance.

The Decision Tree model & Over-sampling the data gave significantly better results and captured more meaningful relationships in the data.

## 📝 Recommendations
To improve the model further, the following strategies could be implemented:
- Use hyperparameter tuning (e.g., GridSearchCV)
- Apply data balancing techniques (e.g., SMOTE for imbalanced data)
- Experiment with advanced algorithms like XGBoost or LightGBM
- Apply cross-validation for better generalization

## 📊 Presentation
A 5-slide PowerPoint presentation was created to summarize the process and results of this project. It includes visuals like feature importance, model evaluation metrics, and key insights.

## 🤝 Acknowledgment
Special thanks to **Xaltius Academy** for the opportunity and mentorship provided during this internship. This project has been an invaluable experience in applying machine learning to real-world financial data problems.

## 📂 Repository Structure
