# BDA-and-BI-Group-4

Big Data & Business Intelligence group project analyzing Amazon Electronics reviews.

## Project Overview

A 3-phase Big Data pipeline analyzing Amazon Electronics product reviews using Python, Hadoop MapReduce, and Apache Spark.

## Dataset

Amazon Electronics reviews dataset (`Electronics_5.json.gz`). Download from [Amazon Review Data (2014)](https://snap.stanford.edu/data/web-Amazon.html).

Place the dataset in the project root as `Electronics_sample_50k.json.gz` (or update the path in each notebook).

## Project Structure

```
├── Phase 1 - EDA & HDFS Setup
│   ├── Phase 1.ipynb          # Main EDA notebook
│   ├── Phases 1.ipynb         # Extended Phase 1 notebook
│   ├── part1                  # Data loading & rating distribution script
│   ├── Loading data           # Data loading from gzipped JSON
│   ├── Display the first five rows from the loaded datasets
│   ├── Phase 1_ HDFS image.png
│   ├── phase1_visualizations.png
│   └── phase1_time_analysis.png
│
├── Phase 2 - MapReduce
│   ├── phases 2.ipynb         # Main Phase 2 notebook
│   ├── job1_mapper.py         # Extract product ID and rating
│   ├── job1_reducer.py        # Calculate average rating per product
│   ├── job2_mapper.py         # Extract reviewer ID
│   ├── job2_reducer.py        # Count total reviews per user
│   ├── job3_mapper.py         # Count reviews per product
│   ├── job3_reducer.py        # Find top 10 most reviewed products
│   ├── phase 2 job 1.png
│   ├── phase 2 job 2.png
│   ├── phase 2 job 3.png
│   └── phase2_results.txt
│
├── Phase 3 - Spark ML & Analytics
│   ├── Phases 3.ipynb         # Main Phase 3 notebook
│   ├── phase3_clusters.png
│   ├── phase3_timeseries.png
│   ├── phase3_cluster_profiles.txt
│   └── phase3_cluster_stats.csv
│
├── docs/
│   └── start_jupyter.bat      # Helper to launch Jupyter Notebook
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Phases

### Phase 1: Data Exploration & HDFS
- Load gzipped JSON review data
- Exploratory Data Analysis (rating distribution)
- HDFS setup and data ingestion
- Time analysis visualizations

### Phase 2: MapReduce Processing
- **Job 1:** Average rating per product
- **Job 2:** Review count per user (top active reviewers)
- **Job 3:** Top 10 most reviewed products
- Python mappers and reducers simulating Hadoop MapReduce

### Phase 3: Spark-based Analytics
- **K-Means Clustering:** Segment products into 3 clusters based on rating, review count, and price
- **ALS Recommendation:** Collaborative filtering recommendation system
- **Time Series Analysis:** Monthly rating and review count trends

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Download the Amazon Electronics dataset and place it in the project root
4. Launch Jupyter:
   ```
   jupyter notebook
   ```
5. Open the phase notebooks in order

## Requirements

- Python 3.8+
- Apache Spark (for Phase 3)
- Hadoop HDFS (for Phase 1 HDFS tasks)
- See `requirements.txt` for Python packages

## Team

Group 4 - BDA and BI Course Project
 
