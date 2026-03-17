import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],  
    'Age': [24, 30, 22, 35],  
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'phone': ['123-456-7890', '987-654-3210', '555-555-5555', '444-444-4444']
}
df = pd.DataFrame(data)
print(df)