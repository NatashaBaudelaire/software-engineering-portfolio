# Data Science Projects

Worked Jupyter notebooks on the data science lifecycle: exploratory data
analysis, data visualization and preprocessing. All datasets are shared,
deduplicated and stored once in [`datasets/`](datasets/); every notebook reads
its data from there via a relative path, so results are reproducible.

## Directory Structure

### `datasets`

Single source of truth for the datasets used across the notebooks:

| File | Used by |
| --- | --- |
| `diabetes.csv` | `data-analysis-and-visualization/diabetes.ipynb`, `data-preprocessing/pima_diabetes.ipynb` |
| `house_prices.csv` | `data-preprocessing/house_prices.ipynb` |
| `traffic_accident_severity_detection.csv` | `exploratory-data-analysis/traffic_accident_severity_detection.ipynb` |
| `watersupply.csv` | Sample for data acquisition and sharing practices |

### `projects`

| Folder | Notebook | Dataset |
| --- | --- | --- |
| `exploratory-data-analysis` | `traffic_accident_severity_detection.ipynb` - EDA on traffic accident severity | `../../datasets/traffic_accident_severity_detection.csv` |
| `data-analysis-and-visualization` | `diabetes.ipynb` - analysis and visualization of the diabetes dataset | `../../datasets/diabetes.csv` |
| `data-preprocessing` | `house_prices.ipynb` - data cleaning and preprocessing pipeline | `../../datasets/house_prices.csv` |
| `data-preprocessing` | `pima_diabetes.ipynb` - preprocessing of the PIMA diabetes dataset | `../../datasets/diabetes.csv` |

## How to Run

1. Install Jupyter and the required libraries:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

2. Start Jupyter and open a notebook:

```bash
jupyter notebook
```

3. Keep the notebook in its `projects/` subfolder so the relative dataset
   paths (`../../datasets/...`) resolve correctly.

> Notebooks are always executed from their own folder; Jupyter resolves the
> relative `../../datasets/*.csv` path to the shared `data-science/datasets/`
> directory automatically.

## Learning Objectives

- Data acquisition and responsible sharing practices
- Exploratory data analysis (distributions, correlations, missing values)
- Data visualization (matplotlib and seaborn)
- Preprocessing: handling missing data, scaling, encoding
- Reproducible analysis with shared, deduplicated datasets