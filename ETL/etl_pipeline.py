import pandas as pd
import os

# -------------------------------
# PATHS
# -------------------------------

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

RAW_PATH = os.path.join(BASE_PATH, "Raw")
PROCESSED_PATH = os.path.join(BASE_PATH, "Processed")
# -------------------------------
# LOAD DATASETS
# -------------------------------

users = pd.read_csv(os.path.join(RAW_PATH, "users.csv"))
sessions = pd.read_csv(os.path.join(RAW_PATH, "sessions.csv"))
events = pd.read_csv(os.path.join(RAW_PATH, "events.csv"))
orders = pd.read_csv(os.path.join(RAW_PATH, "orders.csv"))
order_items = pd.read_csv(os.path.join(RAW_PATH, "order_items.csv"))
products = pd.read_json(os.path.join(RAW_PATH, "products.json"))
campaigns = pd.read_csv(os.path.join(RAW_PATH, "campaigns.csv"))

print("Datasets loaded successfully")

# -------------------------------
# MERGE ORDER ITEMS + PRODUCTS
# -------------------------------

order_items_products = order_items.merge(
    products,
    on="product_id",
    how="left"
)

# -------------------------------
# TOTAL ITEMS PER ORDER
# -------------------------------

total_items = order_items.groupby("order_id")["quantity"].sum().reset_index()
total_items = total_items.rename(columns={"quantity": "total_items"})

# -------------------------------
# DISTINCT PRODUCTS PER ORDER
# -------------------------------

distinct_products = order_items.groupby("order_id")["product_id"].nunique().reset_index()
distinct_products = distinct_products.rename(columns={"product_id": "distinct_products"})

# -------------------------------
# TOP CATEGORY PER ORDER
# -------------------------------

category_qty = (
    order_items_products
    .groupby(["order_id", "category"])["quantity"]
    .sum()
    .reset_index()
)

top_category = (
    category_qty
    .sort_values(["order_id", "quantity"], ascending=[True, False])
    .drop_duplicates("order_id")
)

top_category = top_category[["order_id", "category"]].rename(
    columns={"category": "top_category"}
)

# -------------------------------
# CATEGORY MIX
# -------------------------------

category_mix = (
    order_items_products
    .groupby("order_id")[["category", "quantity"]]
    .apply(lambda x: dict(zip(x["category"], x["quantity"])))
    .reset_index(name="category_mix")
)

# -------------------------------
# AVERAGE RATING PER ORDER
# -------------------------------

avg_rating = (
    order_items_products
    .groupby("order_id")["rating"]
    .mean()
    .reset_index()
)

# -------------------------------
# MARGIN PROXY
# -------------------------------

order_items_products["margin"] = (
    order_items_products["price"] - order_items_products["cost"]
) * order_items_products["quantity"]

margin_proxy = (
    order_items_products
    .groupby("order_id")["margin"]
    .sum()
    .reset_index()
)

margin_proxy = margin_proxy.rename(columns={"margin": "margin_proxy"})

# -------------------------------
# BUILD FACT ORDERS TABLE
# -------------------------------

fact_orders = orders.merge(total_items, on="order_id", how="left")

fact_orders = fact_orders.merge(distinct_products, on="order_id", how="left")

fact_orders = fact_orders.merge(top_category, on="order_id", how="left")

fact_orders = fact_orders.merge(category_mix, on="order_id", how="left")

fact_orders = fact_orders.merge(avg_rating, on="order_id", how="left")

fact_orders = fact_orders.merge(margin_proxy, on="order_id", how="left")

print("\nFACT ORDERS CREATED\n")
print(fact_orders.head())

# -------------------------------
# SAVE OUTPUT
# -------------------------------

output_file = os.path.join(PROCESSED_PATH, "fact_orders.csv")

fact_orders.to_csv(output_file, index=False)

print("\nSaved file to:")
print(output_file)


# -------------------------------
# FACT SESSIONS
# -------------------------------

# Count events per session
event_counts = (
    events.groupby("session_id")
    .size()
    .reset_index(name="event_count")
)

# Mark sessions that converted (had an order)
converted_sessions = orders[["session_id"]].drop_duplicates()
converted_sessions["converted"] = 1

# Merge sessions with event counts
fact_sessions = sessions.merge(event_counts, on="session_id", how="left")

# Merge conversion flag
fact_sessions = fact_sessions.merge(converted_sessions, on="session_id", how="left")

# Fill missing values
fact_sessions["event_count"] = fact_sessions["event_count"].fillna(0)
fact_sessions["converted"] = fact_sessions["converted"].fillna(0)

# Join campaign info
fact_sessions = fact_sessions.merge(
    campaigns,
    on=["campaign_id", "channel"],
    how="left"
)

print("\nFACT SESSIONS CREATED\n")
print(fact_sessions.head())

# Save file
sessions_output = os.path.join(PROCESSED_PATH, "fact_sessions.csv")

fact_sessions.to_csv(sessions_output, index=False)

print("\nSaved fact_sessions to:")
print(sessions_output)


# -------------------------------
# DIM USERS
# -------------------------------

# Total orders per user
user_orders = (
    orders.groupby("user_id")["order_id"]
    .count()
    .reset_index(name="total_orders")
)

# Lifetime value (total revenue per user)
lifetime_value = (
    orders.groupby("user_id")["net_amount"]
    .sum()
    .reset_index(name="lifetime_value")
)

# Average order value
avg_order_value = (
    orders.groupby("user_id")["net_amount"]
    .mean()
    .reset_index(name="avg_order_value")
)

# Merge with users table
dim_users = users.merge(user_orders, on="user_id", how="left")

dim_users = dim_users.merge(lifetime_value, on="user_id", how="left")

dim_users = dim_users.merge(avg_order_value, on="user_id", how="left")

# Fill missing values
dim_users["total_orders"] = dim_users["total_orders"].fillna(0)
dim_users["lifetime_value"] = dim_users["lifetime_value"].fillna(0)
dim_users["avg_order_value"] = dim_users["avg_order_value"].fillna(0)

print("\nDIM USERS CREATED\n")
print(dim_users.head())

# Save file
users_output = os.path.join(PROCESSED_PATH, "dim_users.csv")

dim_users.to_csv(users_output, index=False)

print("\nSaved dim_users to:")
print(users_output)


print("\nCurrent working directory:", os.getcwd())