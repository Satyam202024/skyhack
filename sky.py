#numeric sum of different score of rating 1 to 3 how many they are example score 1  = 7713,score 2= 8250 ,score 3=6390 this is out of 1lakhs+ data

import pandas as pd
import re
csv_file = 'test.csv'
column_name = 'score'

def extract_and_sum_numeric(cell):
    numeric_values = re.findall(r'\d+', str(cell))
    if numeric_values:
        return sum(map(int, numeric_values))
    else:
        return 0

df = pd.read_csv(csv_file)

df['Numeric_Sum'] = df[column_name].apply(extract_and_sum_numeric)

total_numeric_sum = df['Numeric_Sum'].sum()

print("Total Numeric Sum:", total_numeric_sum)

numeric_counts = df[column_name].str.extractall(r'(\d+)')[0].value_counts()
print("Numeric Value Counts:")
print(numeric_counts)