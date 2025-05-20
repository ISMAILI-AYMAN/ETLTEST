import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
def extract_load(dataset_path):
    """
    Load a CSV dataset and return it as a pandas DataFrame.
    
    Parameters:
        dataset_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    try:
        df = pd.read_csv(dataset_path)
        print("✅ Dataset loaded successfully.")
        print(f"📊 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"🧼 Missing values:\n{df.isnull().sum()}")
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {dataset_path}")
        return None
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

from sklearn.preprocessing import LabelEncoder
import pandas as pd

def transform(df):
    """
    Clean and transform the dataset:
    - Fill missing numeric values
    - Encode categoricals
    - Drop known irrelevant columns
    - Normalize numeric columns
    
    Returns:
        pd.DataFrame: Transformed DataFrame
        dict: Label encoders used
    """
    label_encoders = {}

    # Step 1: Fill missing numeric values
    try:
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        print("✅ Missing numeric values filled.")
    except Exception as e:
        print(f"❌ Error filling missing values: {e}")

    # Step 2: Encode categorical variables
    try:
        for col in df.select_dtypes(include=['object']).columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
        print("✅ Categorical variables encoded.")
    except Exception as e:
        print(f"❌ Error encoding categoricals: {e}")

    # Step 3: Drop unnecessary columns (if present)
    try:
        if 'customerID' in df.columns:
            df.drop(columns=['customerID'], inplace=True)
            print("✅ Dropped column 'customerID'.")
    except Exception as e:
        print(f"❌ Error dropping columns: {e}")

    # Step 4: Normalize numeric columns
    try:
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())
        print("✅ Normalized numeric columns.")
    except Exception as e:
        print(f"❌ Error normalizing numeric columns: {e}")
    # Step 5 : plot the distribution of the target variable
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
        plt.figure(figsize=(10, 6))
        sns.countplot(x='Churn', data=df)
        plt.title('Distribution of Churn')
        plt.show()
    except Exception as e:
        print(f"❌ Error plotting distribution: {e}")
    # Step 6: Check for duplicates
    try:
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            df.drop_duplicates(inplace=True)
            print(f"✅ Dropped {duplicates} duplicate rows.")
        else:
            print("✅ No duplicates found.")
    except Exception as e:
        print(f"❌ Error checking for duplicates: {e}")
    # Step 7: save the cleaned dataset
    try:
        df.to_csv('data/cleaned_dataset.csv', index=False)
        print("✅ Cleaned dataset saved as 'cleaned_dataset.csv'.")
    except Exception as e:
        print(f"❌ Error saving cleaned dataset: {e}")
    return df, label_encoders
def load(dataset_path):
    try:
        df = pd.read_csv(dataset_path)
        print("✅ Dataset loaded successfully.")
        print(f"📊 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {dataset_path}")
        return None
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

            

