 #count the frequency of each flight number
import pandas as pd

csv_file = 'test.csv'

df = pd.read_csv(csv_file)

flight_counts = df['flight_number'].value_counts().reset_index()


flight_counts.columns = ['Flight_Number', 'Frequency']

flight_counts.to_csv('flight_counts.csv', index=False)

print("Flight counts saved to flight_counts.csv")