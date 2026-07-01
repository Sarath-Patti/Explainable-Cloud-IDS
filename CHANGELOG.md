# Changelog

All notable changes to this project will be documented in this file.

---

## v0.1.0 - Project Initialization

### Added

- Created project directory structure.
- Set up Python virtual environment.
- Installed required dependencies.
- Downloaded the CIC-IDS2017 dataset.
- Organized dataset into raw and processed folders.

### Implemented

- dataset_loader.py
  - Reusable dataset loading function.

- test_loader.py
  - Verified successful dataset loading.

- explorer.py
  - Dataset shape inspection.
  - Column name inspection.
  - Summary exploration.

- preprocessing.py
  - Removed leading/trailing spaces from feature names.

- validation.py
  - Missing value analysis.
  - Duplicate row analysis.
  - Infinite value detection.
  - Label distribution analysis.

- cleaning.py
  - Replaced infinite values with NaN.
  - Removed missing values.
  - Removed duplicate rows.
  - Saved cleaned dataset.

### Results

Original Dataset

225,745 rows

↓

Cleaned Dataset

223,082 rows

### Reports

- Generated class distribution visualization.
- Started research journal.