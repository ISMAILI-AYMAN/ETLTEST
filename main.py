from etl import extract_load, transform, load
import pandas as pd
def main(dataset_path):
    """
    Main function to run the ETL process.
    
    Parameters:
        dataset_path (str): Path to the CSV file.
    """
    # Step 1: Extract
    df = extract_load(dataset_path)
    if df is None:
        return

    # Step 2: Transform
    df, label_encoders = transform(df)

    # Step 3: Load
    load("data/cleaned_dataset.csv")
    print("✅ Transformed dataset saved successfully.")
    print("✅ ETL process completed successfully.")


if __name__ == "__main__":

    main("data/churn_raw.csv")
