# Summer Project Research Journal

**Project Title:**
Explainable Machine Learning Framework for Cloud Intrusion Detection using CIC-IDS2017

---

# Day 1

## Objective
Set up the project environment and perform initial dataset exploration.

## Tasks Completed

- Created the project structure.
- Set up a Python virtual environment.
- Installed required Python libraries.
- Downloaded the CIC-IDS2017 dataset.
- Implemented a reusable dataset loader.
- Explored the dataset structure.
- Identified leading spaces in feature names.
- Implemented column name cleaning.

## Observations

- Dataset contains 225,745 network flow records.
- Dataset contains 79 columns.
- All column names contained leading spaces.
- Cleaning column names simplifies future preprocessing.

## Conclusion

Successfully prepared the project environment and completed the initial dataset exploration. The dataset is ready for validation.

---

# Day 2

## Objective

Validate and clean the dataset before model development.

## Tasks Completed

- Performed missing value analysis.
- Performed duplicate row analysis.
- Checked label distribution.
- Detected infinite values.
- Built a reusable data cleaning pipeline.
- Saved the cleaned dataset.

## Validation Results

Original Dataset

Rows : 225745

Columns : 79

Missing Values

Flow Bytes/s : 4

Duplicate Rows

2633

Infinite Values

Flow Bytes/s : 30

Flow Packets/s : 34

Total Infinite Values : 64

Label Distribution

DDoS : 128027

BENIGN : 97718

Cleaning Results

Original Shape : (225745,79)

↓

Final Shape : (223082,79)

Cleaning Operations

- Replaced 64 infinite values with NaN.
- Removed rows containing missing values.
- Removed duplicate rows.
- Saved cleaned dataset to data/processed/.

## Research Observations

- The dataset contains only a very small number of missing values.
- Duplicate records account for approximately 1.17% of the dataset.
- Infinite values occur mainly in Flow Bytes/s and Flow Packets/s.
- The dataset is reasonably balanced between DDoS and BENIGN traffic.

## Conclusion

A clean dataset was successfully generated and will be used for all future experiments.

---

# Day 3

## Objective

Perform Exploratory Data Analysis (EDA).

## Tasks Completed

- Loaded the cleaned dataset.
- Generated summary statistics.
- Created the class distribution visualization.

## Observations

- Cleaned dataset contains 223,082 samples.
- Flow Duration has a minimum value of -1, indicating a possible invalid record.
- Destination Port is predominantly 80, suggesting most traffic targets HTTP services.
- Features such as Idle Max exhibit a wide range, indicating possible outliers.
- Generated and saved the first visualization (Class Distribution).

## Conclusion

Initial EDA confirms that the cleaned dataset is suitable for further analysis. Additional feature distribution and correlation analysis will be performed before feature engineering.