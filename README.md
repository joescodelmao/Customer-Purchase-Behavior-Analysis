# Customer Purchase Behavior Analysis

A reproducible end-to-end **customer segmentation** pipeline that simulates e-commerce transactions, performs data cleaning and aggregation, applies clustering, and exports results for visualization (Tableau/Excel). This repository is designed as a portfolio-ready project you can run locally or adapt to real data.

---

## Tech stack (highlighted)

* **Languages:** `Python` (3.8+)
* **Libraries / Tools:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `Tableau` (for visualization)

---

## What this project does (step-by-step)

1. **Simulate** a realistic e-commerce transaction dataset (100k records) with `CustomerID`, `TransactionDate`, `Quantity`, and `UnitPrice`.
2. **Clean** the data by removing invalid records (e.g., non-positive quantities/prices) and duplicates.
3. **Aggregate** transactions into customer-level features: total `Revenue`, total `Quantity`, and `NumPurchases`.
4. **Scale** features with `StandardScaler` to normalize ranges for clustering.
5. **Cluster** customers using `KMeans` into 4 segments (configurable).
6. **Visualize** segmentation with scatter plots (Revenue vs NumPurchases) and export the clustered customer table to `customer_segments.csv` for dashboarding in `Tableau` or other BI tools.

---

## Repository structure

```
├─ customer_segmentation.py    # Main script (simulate, clean, cluster, plot, export)
├─ customer_segments.csv       # Output (generated after running script)
├─ README.md                   # This file
└─ requirements.txt            # (optional) pinned dependencies
```

---

## Quick start — setup

1. (Recommended) Create and activate a virtual environment:

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip3 install -r requirements.txt
# or
pip3 install pandas numpy scikit-learn matplotlib seaborn
```

If you prefer, create a `requirements.txt` with:

```
pandas
numpy
scikit-learn
matplotlib
seaborn
```

---

## Run the project

Save or confirm the main script is named `customer_segmentation.py` and run:

```bash
python3 customer_segmentation.py
```

What to expect:

* A scatter plot window showing clusters (Revenue vs NumPurchases).
* A CSV file `customer_segments.csv` created in the working directory.
* Console output with a sample `head()` of the customer-level DataFrame.

---

## How to test and validate outputs

* **Quick validation (manual):**

  * Open `customer_segments.csv` and run `head` or load it into a notebook to verify columns: `CustomerID`, `Revenue`, `Quantity`, `NumPurchases`, `Cluster`.
  * Verify the number of unique clusters:

    ```python
    import pandas as pd
    df = pd.read_csv('customer_segments.csv')
    df['Cluster'].nunique()
    ```
* **Basic sanity checks:** ensure `Revenue > 0` for all rows, `NumPurchases` is an integer count, and cluster labels range from 0 to (n\_clusters-1).

---

## Using your own data

If you want to run the pipeline on real transaction data, your input CSV should contain at least these columns (case-sensitive unless you adapt the script):

* `CustomerID` (numeric or string)
* `TransactionDate` (ISO date or parseable by `pandas.to_datetime`)
* `Quantity` (integer)
* `UnitPrice` (float)

Steps:

1. Replace the simulation block in `customer_segmentation.py` with a `pd.read_csv('your_transactions.csv')` call.
2. Parse dates: `data['TransactionDate'] = pd.to_datetime(data['TransactionDate'])`.
3. Run the same cleaning & aggregation steps.

Notes:

* If you have multiple items per transaction (multiple rows per TransactionID), the aggregation by `CustomerID` still works because we sum `Quantity` and `Revenue`.
* You may want to group by a `CustomerID` + time window (e.g., last 12 months) to capture recency.

---

## Tableau / BI tips

* Import `customer_segments.csv` into Tableau.
* Recommended visualizations:

  * Scatterplot: `Revenue` vs `NumPurchases`, color by `Cluster`.
  * Bar chart: Average `Revenue` per `Cluster`.
  * Boxplot: `Revenue` distribution per `Cluster` to spot outliers.
* Add filters for date ranges or customer cohorts if you extend the dataset with `RegistrationDate` or `Region`.

---
