# CSV Profiler

A lightweight Python application for automated CSV dataset profiling and exploratory data analysis. The tool generates structured reports that help users quickly understand the quality, structure, and statistical characteristics of their data before further analysis or machine learning workflows.

## Features

- Upload and analyze CSV datasets
- Automatically detect column data types
- Calculate missing value counts and percentages
- Count unique values per column
- Generate descriptive statistics for numerical columns:
  - Minimum value
  - Maximum value
  - Mean value
- Export reports in:
  - JSON format
  - Markdown format
- Interactive web interface built with Streamlit

## Technologies Used

- Python
- Streamlit
- CSV
- JSON
- Pathlib

## Project Structure

```text
CSV-PROFILER-PROJECT/
│
├── app.py
├── profiler.py
├── exporters.py
├── sample_data.csv
├── reports/
├── requirements.txt
└── README.md
```

## How It Works

The application analyzes a CSV file and generates a profiling report containing:

### Dataset Summary

- Total number of rows
- Total number of columns

### Column Analysis

For each column, the profiler provides:

- Data type detection
- Missing value count
- Missing value percentage
- Number of unique values

### Numerical Statistics

For numeric columns:

- Mean
- Minimum
- Maximum

## Installation

Clone the repository:

```bash
git clone https://github.com/noura05x/CSV-PROFILER-PROJECT.git
cd CSV-PROFILER-PROJECT
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

Then open the local URL provided by Streamlit in your browser.

## Example Use Cases

- Initial dataset exploration
- Data quality assessment
- Missing value detection
- Data preprocessing preparation
- Educational data analysis projects

## Future Improvements

- Median calculation
- Standard deviation analysis
- Correlation matrix generation
- Outlier detection
- Interactive visualizations
- PDF report export
- Advanced analytics using Pandas
- Data quality scoring system

## Learning Outcomes

This project demonstrates practical experience in:

- Python programming
- Data profiling techniques
- Data quality assessment
- File processing
- Report generation
- Streamlit application development
- Software project organization

## Author

**Noura Aljandol**

Information Technology Student | Data Analytics & Artificial Intelligence Enthusiast

- GitHub: https://github.com/noura05x
- LinkedIn: https://www.linkedin.com/in/noura-aljandol
