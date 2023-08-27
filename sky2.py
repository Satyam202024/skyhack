# Extracting flight numbers and their corresponding scores
import pandas as pd

csv_file = 'comment.csv'

df = pd.read_csv(csv_file)


flight_scores = df[['flight_number', 'verbatim_text','scheduled_departure_date']]

output_file = 'test_all.csv'

flight_scores.to_csv(output_file, index=False)

print(f'Saved flight numbers and scores to {output_file}')