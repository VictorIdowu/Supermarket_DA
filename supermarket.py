import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("sales.csv")
# print(sales['Category'].unique())
males = sales[sales.Gender == 'Male']
large_transactions = sales[sales.Total > 100]
cash_newyork = sales.query('Payment=="Cash"&City=="NewYork"&Total<50' )
total_sales_transaction = sales.Total.sum()
max_amount_by_user = sales.Total.max()
min_amount_by_user = sales.Total.min()
avg_amount = sales.Total.mean()
total_amount_by_city = sales.groupby("City").sum()['Total']
# print(total_amount_by_city)

# answering questions about the branch
# which locations has the highest/lowest sales?
# represent the sales on a bar chart, also show the market share for each location using a pie chart

location_list = sales.groupby('Location')
locations = [x for x,y in location_list]
# plt.bar(locations,sales.groupby("Location").sum()['Total'])
# plt.pie(sales.groupby("Location").sum()['Total'],labels=locations,autopct='%1.1f%%')
# plt.show()

# Which location has more female customers and which branch has more meal
location_sales = sales.groupby(["Gender","Location"]).count()['Invoice ID']
unstacked_sales = location_sales.unstack(level=0)
# unstacked_sales.plot(kind='bar')
# plt.show()

# Which branch has more members vs which has less members?
# Which branch has the highest rate and which has the lowest?
members = sales.groupby(["Member","Location"]).count()['Invoice ID']
unstacked_members = members.unstack(level=0)
# unstacked_members.plot(kind='bar')

rating = sales.groupby('Location')['Rating'].mean()
# print(rating)
# rating.plot(kind='bar')
# plt.show()

# City ////
# Which city has more females shopping?
female_shoppers = sales.groupby(["Gender","City"]).count()['Invoice ID']
# female_shoppers.unstack(level=0).plot(kind='bar')

# Gender //
# Who spends more? Men or Women?
genders = sales.groupby("Gender")["Total"].sum()
# genders.plot(kind='bar')

# Customer Type ///
# Which type of customer spends more? Member or Non-member?
member = sales.groupby("Member")["Total"].sum()
# member.plot(kind='bar')

# Product line ///
# Which product line sells more?
category_sales = sales.groupby("Category").count()["Rating"]
# category_sales.plot(kind='bar')

# Which product line is popular among men vs women?
category_sales = sales.groupby(["Gender","Category"]).count()["Rating"]
# category_sales.unstack(level=0).plot(kind='bar')
# plt.show()

# What days the month makes most sales?
# print(pd.to_datetime(sales['Date']).dt.day)
sales["Day"] = pd.to_datetime(sales['Date']).dt.day
day_sales = sales.groupby('Day')['Total'].sum()
# day_sales.plot(kind='bar')

# What months makes most sales?
sales["Month"] = pd.to_datetime(sales['Date']).dt.month
month_sales = sales.groupby('Month')['Total'].sum()
# month_sales.plot(kind='bar')
# plt.grid()

# What hours makes most sales?
sales["Hour"] = pd.to_datetime(sales['Time']).dt.hour
hours_sales = sales.groupby('Hour')['Total'].sum()
# hours_sales.plot(kind='bar',grid=True)

# What times do people make more epayments VS 
# What time people make more cash payments?
sales.groupby(["Payment","Hour"]).count()["Invoice ID"].unstack(level=0).plot(kind='bar',grid=True)

plt.show()