# # import pandas as pd
# # import numpy as np
# # import matplotlib.pyplot as plt

# # from sklearn.model_selection import train_test_split
# # from sklearn.ensemble import RandomForestRegressor
# # from sklearn.metrics import mean_absolute_error
# # from sklearn.preprocessing import LabelEncoder
# # import pickle

# # df = pd.read_csv("data.csv")

# # print("First 5 rows:")
# # print(df.head())

# # print(df.isnull().sum())

# # df.dropna(inplace=True)
# # df.drop_duplicates(inplace=True)

# # print("After cleaning:", df.shape)

# # print(df.describe())

# # df.groupby("Category")["Sales"].sum().plot(kind="bar")
# # plt.title("Sales by Category")
# # plt.show()

# # df.groupby("Region")["Sales"].sum().plot(kind="bar")
# # plt.title("Sales by Region")
# # plt.show()

# # le = LabelEncoder()

# # df["Category"] = le.fit_transform(df["Category"])
# # df["Region"] = le.fit_transform(df["Region"])

# # X = df[["Category", "Region", "Quantity", "Discount"]]
# # y = df["Sales"]

# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # model = RandomForestRegressor()
# # model.fit(X_train, y_train)

# # y_pred = model.predict(X_test)
# # print("Prediction done")

# # mae = mean_absolute_error(y_test, y_pred)
# # print("Mean Absolute Error:", mae)

# # pickle.dump(model, open("model.pkl", "wb"))
# # print("Model saved!")

# # model = pickle.load(open("model.pkl", "rb"))

# # sample_input = [[1, 2, 5, 0.2]]

# # result = model.predict(sample_input)

# # print("Predicted Sales:", result)

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error

# df = pd.read_csv("data.csv")

# print("First 5 rows:")
# print(df.head())

# df.dropna(inplace=True)
# df.drop_duplicates(inplace=True)

# print("After cleaning:", df.shape)

# print(df.describe())

# df.groupby("Category")["Sales"].sum().plot(kind="bar")
# plt.title("Sales by Category")
# plt.show()

# df.groupby("Region")["Sales"].sum().plot(kind="bar")
# plt.title("Sales by Region")
# plt.show()

# X = df[["Quantity", "Discount"]]
# y = df["Sales"]

# model = RandomForestRegressor()
# model.fit(X, y)

# sample_input = [[5, 0.2]]  # quantity=5, discount=0.2

# result = model.predict(sample_input)

# print("Predicted Sales:", result)

# pred = model.predict(X)
# print("MAE:", mean_absolute_error(y, pred))

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

print("\nFirst 5 rows:")
print(df.head())

# -----------------------------
# 1. Total Sales by Category
# -----------------------------
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Category:")
print(category_sales)

# Plot
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# -----------------------------
# 2. Profit by Category
# -----------------------------
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

print("\nProfit by Category:")
print(category_profit)

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar", color="green")
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Insights
# -----------------------------
print("\nINSIGHTS:")
print("1. Highest Sales Category:", category_sales.idxmax())
print("2. Lowest Sales Category:", category_sales.idxmin())
print("3. Highest Profit Category:", category_profit.idxmax())
print("4. Lowest Profit Category:", category_profit.idxmin())