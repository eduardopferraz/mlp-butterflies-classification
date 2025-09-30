#!/usr/bin/env python3
import os
import pandas as pd
from datetime import datetime

"""
Script to preprocess the Global Crocodile Species Dataset:
1. Load raw data
2. Clean column names
3. Remove duplicates
4. Handle missing values
5. Convert dates to datetime
6. Extract year, month, day from 'Date of Observation'
7. Save cleaned dataset
"""

# Ensure the output directory exists
os.makedirs('data/processed', exist_ok=True)

# Load raw dataset (CSV)
df = pd.read_csv('data/raw/crocodile_dataset.csv')

# Strip extra spaces from column names
df.columns = df.columns.str.strip()
print("Loaded columns:", df.columns.tolist())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values for numeric columns with median
numeric_cols = ['Observed Length (m)', 'Observed Weight (kg)']
for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

# Fill missing values for categorical columns with 'Unknown'
categorical_cols = ['Common Name', 'Scientific Name', 'Family', 'Genus',
                    'Age Class', 'Sex', 'Country/Region', 'Habitat Type', 
                    'Conservation Status', 'Observer Name']
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown')

# Convert 'Date of Observation' to datetime
if 'Date of Observation' in df.columns:
    df['Date of Observation'] = pd.to_datetime(df['Date of Observation'], format='%d-%m-%Y', errors='coerce')

    # Extract year, month, day as separate columns
    df['Observation_Year'] = df['Date of Observation'].dt.year
    df['Observation_Month'] = df['Date of Observation'].dt.month
    df['Observation_Day'] = df['Date of Observation'].dt.day

# Save the cleaned dataset
df.to_csv('data/processed/crocodile_dataset_clean.csv', index=False)

print("Data saved in data/processed/crocodile_dataset_clean.csv")
