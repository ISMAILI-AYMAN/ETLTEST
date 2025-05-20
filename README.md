# ETL Data Pipeline – Churn Dataset

This project demonstrates a simple end-to-end data pipeline for preprocessing a customer churn dataset using Python and Pandas.

## 📌 Features

- Load raw CSV data
- Fill missing values with column means
- Encode categorical variables using LabelEncoder
- Drop unnecessary columns (e.g., customerID)
- Normalize numerical features to [0, 1]
- Modular and extensible design (ETL functions)

## 📁 Project Structure

/etl_pipeline_project/
├── data/
│   ├── raw_data.csv
│   └── clean_data.csv
├── etl.py
├── main.py
├── requirements.txt
└── README.md
