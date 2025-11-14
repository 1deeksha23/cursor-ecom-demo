# ingest_sqlite.py
# Reads CSVs and writes them into a SQLite database `ecom.db`
import sqlite3
import pandas as pd
import sys

DB_FILE = "ecom.db"

def main():
    try:
        customers = pd.read_csv("customers.csv")
        categories = pd.read_csv("categories.csv")
        products = pd.read_csv("products.csv")
        orders = pd.read_csv("orders.csv")
        order_items = pd.read_csv("order_items.csv")
    except FileNotFoundError as e:
        print("Missing file:", e)
        sys.exit(1)

    conn = sqlite3.connect(DB_FILE)
    customers.to_sql("customers", conn, if_exists="replace", index=False)
    categories.to_sql("categories", conn, if_exists="replace", index=False)
    products.to_sql("products", conn, if_exists="replace", index=False)
    orders.to_sql("orders", conn, if_exists="replace", index=False)
    order_items.to_sql("order_items", conn, if_exists="replace", index=False)

    cur = conn.cursor()
    cur.execute("CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_orderitems_order ON order_items(order_id);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_orderitems_product ON order_items(product_id);")
    conn.commit()
    conn.close()
    print(f"Ingested CSVs into {DB_FILE}")

if __name__ == "__main__":
    main()