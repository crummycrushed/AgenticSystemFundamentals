import pandas as pd

users = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "city": ["Bangalore", "Delhi", "Mumbai", "Pune", "Chennai"]
})

#print(users)

products = pd.DataFrame({
    "product_id": [101, 102, 103, 104, 105],
    "product_name": ["Laptop", "Phone", "Headphones", "Chair", "Desk"],
    "category": ["Electronics", "Electronics", "Electronics", "Furniture", "Furniture"],
    "price": [60000, 20000, 5000, 3000, 8000]
})

#print(products)

orders = pd.DataFrame({
   "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
   "user_id": [1, 1, 2, 3, 3, 4],
   "product_id": [101, 102, 104, 103, 101, 105],
   "quantity": [1, 2, 4, 1, 1, 2],
   "order_date": [
       "2024-01-01",
       "2024-01-03",
       "2024-01-05",
       "2024-01-06",
       "2024-01-07",
       "2024-01-08",
   ]
})

#print(orders)

merged_inner = pd.merge(users, orders, on="user_id", how="left")
print(merged_inner[['name', 'order_id']])