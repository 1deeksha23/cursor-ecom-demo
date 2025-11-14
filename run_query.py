# run_query.py
import sqlite3
import pandas as pd

def main():
    conn = sqlite3.connect("ecom.db")

    # read SQL query
    query = open("query.sql").read()

    # run the query
    df = pd.read_sql_query(query, conn)

    # export result
    df.to_csv("top_50_orders.csv", index=False)

    print("Saved: top_50_orders.csv")
    print("Preview:")
    print(df.head(10))

    conn.close()

if __name__ == "__main__":
    main()