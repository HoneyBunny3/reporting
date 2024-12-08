# Reporting Repository

This repository demonstrates the ability to generate complex and meaningful insights using raw datasets, specifically focusing on monthly construction spending reports. The insights align with the responsibilities of a Senior Business Analyst role, particularly in the field of capital planning and construction.

---

## Project Overview

The `reporting` repository showcases the analysis of **U.S. Census Bureau's Construction Spending Reports** from January 2024 to September 2024. These reports provide detailed monthly spending data across various construction categories such as residential, non-residential, public, and private projects. The goal is to analyze trends, identify patterns, and generate actionable insights that aid strategic decision-making.

### Key Features
- **Data Processing and Cleaning**: Transform raw datasets into a standardized format for analysis.
- **Comprehensive Analysis**: Perform exploratory and advanced analysis to identify key trends in construction spending.
- **Actionable Insights**: Present findings using visualizations and dashboards to support capital planning efforts.
- **Documentation**: Provide clear and detailed documentation of all data handling processes.

---

## Repository Structure

```plaintext
reporting/
├── data/
│   ├── raw/                 # Raw .xlsx datasets (January 2024 - September 2024)
│   ├── cleaned/             # Cleaned and processed datasets
├── docs/                    # Project documentation
├── notebooks/               # Jupyter Notebooks for exploratory data analysis
├── scripts/                 # Python scripts for data cleaning and analysis
├── README.md                # Project overview and instructions
├── requirements.txt         # Python dependencies
```

---

## Datasets

### Source
All datasets were obtained from the **U.S. Census Bureau**, specifically the [Construction Spending Reports](https://www.census.gov/construction/c30/data/index.html).

### Description
The datasets include monthly construction spending estimates for:
- **Residential Projects**
- **Non-Residential Projects**
- **Public and Private Construction**

### Raw Data Location
Raw data files are stored in the `data/raw/` directory, named by their corresponding months (e.g., `pr202401.xlsx` for January 2024).

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Scripts
1. **Data Cleaning**:
   Use the `scripts/data_cleanup.py` script to process raw datasets:
   ```bash
   python scripts/data_cleanup.py
   ```
   Cleaned data will be saved in the `data/cleaned/` directory.

2. **Exploratory Analysis**:
   Open and run Jupyter Notebooks in the `notebooks/` directory for detailed data exploration.

---

## Insights and Reports

The key findings and visualizations generated from this project will be available in the `docs/` directory. These include:
- Trends in total construction spending over time.
- Category-wise spending breakdown (residential vs. non-residential).
- Public vs. private construction trends.

---

## Future Enhancements

Planned improvements include:
- Incorporating additional datasets for comparative analysis.
- Implementing predictive modeling for future construction spending trends.
- Expanding visualizations with interactive dashboards using Tableau.

---

## License

This repository is for educational purposes and follows the terms of use for the U.S. Census Bureau datasets.

---