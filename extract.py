import pandas as pd

# Sample employee data
employees = [
    {"id": 101, "name": "Rahul", "department": "IT", "salary": 45000},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 35000},
    {"id": 103, "name": "Amit", "department": "IT", "salary": 55000},
    {"id": 104, "name": "Sneha", "department": "Finance", "salary": 60000}
]

df=pd.DataFrame(employees)
print(df)