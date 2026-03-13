import matplotlib.pyplot as plt


# categories = ['A', 'B', 'C', 'D']
# values = [10, 25, 13, 18]

# plt.bar(categories, values, color='indigo')
# plt.title("Bar Chart of Categories")
# plt.xlabel("Category")
# plt.ylabel("Value")
# plt.show()


import pandas as pd

df = pd.read_csv("test.csv")

# print(f"Column Names : {df.columns}")

# print("Age Groups :: >>> \n", df["age_group"])
# print("Salary :: >>>\n", df["income"])
# print("Expenses :: >>>\n", df["expense"])


# plt.bar(df["age_group"].values.tolist(), df["income"].values.tolist(), color='indigo')
# plt.title("Bar Chart of Income Under Different Age Groups")
# plt.xlabel("Age Groups")
# plt.ylabel("Income")
# plt.show()

# plt.bar(df["age_group"].values.tolist(), df["expense"].values.tolist(), color='indigo')
# plt.title("Bar Chart of Expenses Under Different Age Groups")
# plt.xlabel("Age Groups")
# plt.ylabel("Income")
# plt.show()

expense_total = sum(df["expense"].values.tolist())


df["expense_percentage"] = df["expense"] / expense_total


# Data: sizes of each slice
sizes = df["expense_percentage"].values.tolist()
# Labels for each slice
labels = df["age_group"].values.tolist()

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot the pie chart on the axes
ax.pie(sizes, labels=labels)

# Set the aspect ratio of the axes to equal to ensure the pie chart is a circle
ax.axis('equal') 

# Display the chart
plt.show()