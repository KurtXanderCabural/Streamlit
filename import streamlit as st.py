import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")

# Set up page config and title
st.set_page_config(page_title="Laptop Prices Dataset EDA", page_icon="💻", layout="wide")
st.title("💻 Laptop Prices Dataset - Exploratory Data Analysis")
st.write("""
    Welcome to the Laptop Prices Dataset EDA! This app allows you to explore and analyze the dataset, revealing insights about laptop features, prices, and more.
    Use the sidebar filters to customize your view!
""")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("laptop_prices.csv")
    return df

df = load_data()

# Display dataset overview
st.header("Dataset Overview")
st.write("Here is a quick look at the dataset:")
st.dataframe(df.head())

# Display dataset information
st.subheader("General Information")
st.write(f"**Shape of Dataset**: {df.shape[0]} rows and {df.shape[1]} columns")
st.write(f"**Missing Values**: {df.isna().sum().sum()}")
st.write(f"**Duplicate Rows**: {df.duplicated().sum()}")

# Show column statistics
st.subheader("Summary Statistics")
st.write(df.describe())

# Sidebar filters for interactivity
st.sidebar.header("Filter Options")
selected_company = st.sidebar.multiselect("Select Companies", df['Company'].unique(), default=df['Company'].unique())
selected_os = st.sidebar.multiselect("Select OS", df['OS'].unique(), default=df['OS'].unique())
selected_ram = st.sidebar.slider("Select RAM Size (GB)", min_value=int(df['Ram'].min()), max_value=int(df['Ram'].max()), value=(int(df['Ram'].min()), int(df['Ram'].max())))
selected_price_range = st.sidebar.slider("Select Price Range (Euros)", min_value=int(df['Price_euros'].min()), max_value=int(df['Price_euros'].max()), value=(int(df['Price_euros'].min()), int(df['Price_euros'].max())))

# Filter data based on sidebar inputs
filtered_df = df[(df['Company'].isin(selected_company)) & 
                 (df['OS'].isin(selected_os)) & 
                 (df['Ram'].between(selected_ram[0], selected_ram[1])) & 
                 (df['Price_euros'].between(selected_price_range[0], selected_price_range[1]))]

# Show filtered data
st.write("### Filtered Laptop Data")
st.dataframe(filtered_df)

# Visualization 1: Count plots for categorical variables
st.subheader("Feature Counts")
columns_to_plot = ['Company', 'TypeName', 'Inches', 'Ram', 'OS', "Screen", "Touchscreen", 'IPSpanel', 'RetinaDisplay', "PrimaryStorageType", "CPU_company", "GPU_company"]

st.write("Distribution of Key Features:")
fig, axes = plt.subplots(6, 2, figsize=(20, 40))
axes = axes.flatten()

for i, col in enumerate(columns_to_plot):
    sns.countplot(y=col, data=df, ax=axes[i], palette='viridis', order=df[col].value_counts().index)
    axes[i].set_title(f'Count of {col}')
    axes[i].set_ylabel('')
    axes[i].set_xlabel('Count')

st.pyplot(fig)

# Visualization 2: Price distribution plot
st.subheader("Price Distribution")
plt.figure(figsize=(10, 6))
sns.histplot(df['Price_euros'], bins=30, kde=True)
plt.title('Distribution of Product Prices')
plt.xlabel('Price (euros)')
plt.ylabel('Frequency')
plt.grid()

st.pyplot()

# Visualization 3: Price Distribution by Categorical Features (Boxplots)
st.subheader("Price Distribution by Categorical Features")
lab_features = ['Company', 'TypeName', 'OS', 'Screen']
fig, axes = plt.subplots(2, 2, figsize=(15, 20))
axes = axes.flatten()

for i, feature in enumerate(lab_features):
    sns.boxplot(data=df, x=feature, y='Price_euros', palette='Spectral', ax=axes[i])
    axes[i].set_title(f'Price Distribution by {feature}')
    axes[i].tick_params(axis='x', rotation=45) 

st.pyplot(fig)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
# Encode categorical data for correlation analysis
label_encoder = LabelEncoder()
object_columns = df.select_dtypes(include=['object']).columns
for col in object_columns:
    df[col] = label_encoder.fit_transform(df[col])

corr = df.corr()
plt.figure(figsize=(20 , 10))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')

st.pyplot()

# Conclusion
st.subheader("Conclusion")
st.write("""
    This exploratory data analysis reveals key insights about laptop prices and their correlations with features like RAM, screen size, and brand. High RAM laptops tend to have higher prices, and certain brands dominate specific price ranges. This dataset offers valuable information for understanding laptop market trends.
""")
