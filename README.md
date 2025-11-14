Cursor E-Commerce Data Project

Synthetic Data Generation • SQLite Ingestion • SQL Querying (Completed in Cursor IDE)

This project was completed as part of the Develop with Cursor (A-SDLC) exercise.
It demonstrates using Cursor AI to generate synthetic data, ingest it into a SQLite database, and execute SQL join queries.



Project Overview

This project performs four major tasks:

✅ 1. Generate Synthetic E-Commerce Data

Using generate_data.py, the project generates around 5 CSV files:
	•	customers.csv
	•	categories.csv
	•	products.csv
	•	orders.csv
	•	order_items.csv



✅ 2. Ingest Data into SQLite

ingest_sqlite.py loads all generated CSV files into a SQLite database named ecom.db, and creates tables:
	•	customers
	•	categories
	•	products
	•	orders
	•	order_items



✅ 3. Execute SQL Join Query

query.sql joins multiple tables to calculate:
	•	order totals
	•	customer details
	•	number of items per order

run_query.py executes this SQL and saves the output to:
	•	top_50_orders.csv



✅ 4. Push the Project to GitHub

The entire codebase was initialized with Git, committed, and pushed to this repository.



📁 Project Structure

cursor-ecom-demo/
├── .gitignore
├── generate_data.py       # Generates synthetic e-commerce data (CSV files)
├── ingest_sqlite.py       # Loads CSVs into SQLite database (ecom.db)
├── query.sql              # SQL JOIN query for reporting
└── run_query.py           # Runs SQL and exports top_50_orders.csv



🛠️ How to Run This Project

1️⃣ Install dependencies

pip install pandas faker

2️⃣ Generate synthetic data

python generate_data.py

3️⃣ Ingest into SQLite

python ingest_sqlite.py

4️⃣ Run the SQL query

python run_query.py

This will create:
top_50_orders.csv

What This Demonstrates
	•	Automated code generation using Cursor IDE
	•	Creating synthetic datasets
	•	SQLite data ingestion
	•	Multi-table SQL JOIN queries
	•	Using Git + GitHub for version control.
