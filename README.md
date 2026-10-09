# India Data Stories

An end-to-end data pipeline analyzing IPL cricket data, built to publish data stories on X ([@Nikita26rai](https://x.com/Nikita26rai)).

## What it does
- Loads raw IPL match data into DuckDB
- Cleans it into an analysis-ready `matches` table
- Runs SQL analyses that power each post

## Data
Download `matches.csv` from the [IPL Complete Dataset on Kaggle](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)
and place it in `data/raw/`. Original source: Cricsheet.

## Run it
    pip install duckdb pandas matplotlib
    python3 pipelines/build_tables.py
    python3 pipelines/day1_toss.py

## Analyses
- Day 1: Does winning the toss decide IPL matches?