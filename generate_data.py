# generate_data.py
# Small, fast synthetic e-commerce CSV generator
import random
from faker import Faker
import pandas as pd

fake = Faker()
Faker.seed(42)
random.seed(42)

def make_customers(n=30):
    rows = []
    for i in range(1, n+1):
        rows.append({
            "customer_id": i,
            "name": fake.name(),
            "email": fake.email(),
            "city": fake.city(),
            "signup_date": fake.date_between(start_date='-2y', end_date='today').isoformat()
        })
    return pd.DataFrame(rows)

def make_categories(n=6):
    return pd.DataFrame([{"category_id": i, "category_name": fake.word().title()} for i in range(1, n+1)])

def make_products(n=50, categories_df=None):
    rows = []
    for i in range(1, n+1):
        cat_id = random.choice(categories_df["category_id"].tolist())
        price = round(random.uniform(5.0, 400.0), 2)
        rows.append({
            "product_id": i,
            "product_name": fake.sentence(nb_words=3).rstrip('.'),
            "category_id": cat_id,
            "price": price
        })
    return pd.DataFrame(rows)

def make_orders(n=80, customers_df=None):
    rows = []
    for i in range(1, n+1):
        cust = random.choice(customers_df["customer_id"].tolist())
        rows.append({
            "order_id": i,
            "customer_id": cust,
            "order_date": fake.date_between(start_date='-1y', end_date='today').isoformat(),
            "shipping_city": fake.city()
        })
    return pd.DataFrame(rows)

def make_order_items(orders_df=None, products_df=None):
    rows = []
    item_id = 1
    for order_id in orders_df["order_id"]:
        item_count = random.randint(1, 4)
        products = random.sample(products_df["product_id"].tolist(), item_count)
        for p in products:
            price = float(products_df.loc[products_df["product_id"]==p, "price"].iloc[0])
            qty = random.randint(1, 3)
            rows.append({
                "order_item_id": item_id,
                "order_id": order_id,
                "product_id": p,
                "quantity": qty,
                "unit_price": price
            })
            item_id += 1
    return pd.DataFrame(rows)

if __name__ == "__main__":
    customers = make_customers(30)
    categories = make_categories(6)
    products = make_products(50, categories)
    orders = make_orders(80, customers)
    order_items = make_order_items(orders, products)

    customers.to_csv("customers.csv", index=False)
    categories.to_csv("categories.csv", index=False)
    products.to_csv("products.csv", index=False)
    orders.to_csv("orders.csv", index=False)
    order_items.to_csv("order_items.csv", index=False)
    print("Created CSVs: customers.csv, categories.csv, products.csv, orders.csv, order_items.csv")