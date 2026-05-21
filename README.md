# BDA-and-BI-Group-4

Big Data & Business Intelligence project focused on large-scale analysis of Amazon Electronics product reviews using Python, Hadoop MapReduce, and Apache Spark.

---

## Project Overview

This project implements a complete Big Data analytics pipeline for processing and analyzing Amazon Electronics review data.

The workflow is divided into three major phases:

- Data Exploration and Preprocessing
- Hadoop MapReduce Processing
- Spark-based Machine Learning Analytics

Project objectives:

- Explore and clean large datasets
- Process data using Hadoop MapReduce
- Apply Spark machine learning algorithms
- Generate visual insights and analytical reports
- Build recommendation and clustering systems

---

## Dataset

Dataset used:

Amazon Electronics Reviews Dataset

Dataset file:

Electronics_sample_50k.json.gz

Dataset source:

https://snap.stanford.edu/data/web-Amazon.html

Place the dataset file inside the project root directory before running notebooks.

---

## Project Structure

Phase 1 — EDA & HDFS Setup

├── Phase 1.ipynb
├── Phases 1.ipynb
├── part1
├── Loading data
├── Display first rows
├── Phase 1_HDFS image.png
├── phase1_visualizations.png
└── phase1_time_analysis.png


Phase 2 — Hadoop MapReduce

├── phases 2.ipynb
├── job1_mapper.py
├── job1_reducer.py
├── job2_mapper.py
├── job2_reducer.py
├── job3_mapper.py
├── job3_reducer.py
└── phase2_results.txt


Phase 3 — Spark Analytics

├── Phases 3.ipynb
├── phase3_clusters.png
├── phase3_timeseries.png
├── phase3_cluster_profiles.txt
└── phase3_cluster_stats.csv


Additional Files

├── docs
├── requirements.txt
├── .gitignore
└── README.md

---

## Phase 1: Data Exploration and HDFS

Tasks:

- Load compressed JSON review datasets
- Perform exploratory data analysis
- Analyze rating distributions
- Configure HDFS storage
- Generate visual reports

---

## Phase 2: Hadoop MapReduce Processing

Implemented Jobs:

Job 1:
Average rating calculation per product

Job 2:
Review count per user

Job 3:
Top reviewed product analysis

---

## Phase 3: Spark Machine Learning Analytics

Implemented Models:

K-Means Clustering

- Product segmentation

ALS Recommendation System

- Collaborative filtering recommendations

Time-Series Analysis

- Review trends over time

---

## Setup Instructions

Step 1:

Clone repository

git clone repository_url


Step 2:

Install project requirements

pip install -r requirements.txt


Step 3:

Place dataset file:

Electronics_sample_50k.json.gz

inside project root directory


Step 4:

Launch Jupyter Notebook

jupyter notebook


Step 5:

Run project notebooks in sequence

Phase 1 → Phase 2 → Phase 3

---

## Requirements

- Python 3.8+
- Apache Spark
- Hadoop HDFS
- Jupyter Notebook

Required Python packages are available in:

requirements.txt

---

## Expected Outputs

The project generates:

- Product rating analysis
- User activity reports
- Review statistics
- Product clusters
- Recommendation results
- Time-series visualizations

---

## Team

Group 4

Big Data Analytics and Business Intelligence Course Project
