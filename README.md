# Bengaluru House Price Predictor 🏡

An end-to-end Machine Learning web application designed to forecast residential real estate prices across major localities in Bengaluru, India. The project encompasses raw data preprocessing, domain-specific outlier filtering, categorical feature encoding, model training via Linear Regression, and an interactive frontend built with Streamlit.

---

## Features

* **Data Cleaning & Standardization:** Cleans irregular square footage formats (e.g., unit ranges converted to arithmetic means) and parses structural bedroom metrics (BHK).


* **Domain Outlier Removal:** Filters unrealistic physical proportions (properties under 300 sq. ft. per room, disproportionate bathroom-to-bed ratios) and eliminates pricing spikes using location-wise standard deviation bounds.


* **High-Performance Linear Model:** Implements ordinary least squares regression over 240+ location-encoded dummy features.


* **Streamlit Web UI:** Intuitive interface providing interactive sliders, numeric inputs, dynamic locality selection, and instant price estimations in Lakhs (INR).



---

## Project Structure

```text
.
├── Bengaluru_House_Data.csv              # Raw Kaggle dataset
├── bangalore_house_price_clean.ipynb     # Data preparation, EDA & training pipeline
├── bangalore_home_prices_model.pickle    # Serialized scikit-learn model
├── columns.json                          # Exported feature schema for UI inference
├── app.py                                # Streamlit dashboard application
└── README.md                             # Documentation

```

---

## Getting Started

### 1. Prerequisites

Ensure you have Python 3.10+ installed along with Conda or `venv`.

### 2. Environment Setup

Create and activate a isolated environment:

```bash
conda create -n house_price_env python=3.10 -y
conda activate house_price_env

```

Install the required dependencies:

```bash
pip install numpy pandas scikit-learn streamlit

```

---

## Training Pipeline

If you want to retrain the model or explore the data cleaning process:

1. Open the Jupyter Notebook:
```bash
jupyter notebook bangalore_house_price_clean.ipynb

```


2. Execute the notebook cells sequentially to clean the raw data, train the estimator, evaluate the test set metric, and export `bangalore_home_prices_model.pickle` along with `columns.json`.



---

## Running the Web Application

Launch the Streamlit web dashboard directly from your terminal:

```bash
streamlit run app.py

```

The application will launch on your local loopback address:

```text
Local URL: http://localhost:8501

```

Enter the required property dimensions (Total Square Feet, Bedrooms, Bathrooms, and Locality) and click **Estimate Price** to generate a market projection.