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


    etl_pipeline_project/
    ├── data/
    │   ├── raw_data.csv
    │   └── clean_data.csv
    ├── etl.py
    ├── main.py
    ├── requirements.txt
    └── README.md


---

## 💻 Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

---
---

## USAGE



```bash

Run the ETL pipeline with:

bash
Copier le code
python main.py



🛠️ How It Works
etl.py: Contains modular functions for each ETL step (e.g., fill missing values, encode categorical variables, drop columns, normalize data).

main.py: Orchestrates the full ETL process by calling functions in etl.py.

Input: data/raw_data.csv — your raw churn dataset.

Output: data/clean_data.csv — the cleaned and preprocessed data ready for analysis or modeling.
