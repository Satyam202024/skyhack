




#filtered data by the 'score' column (which will only contain 1)

import pandas as pd
csv_file = 'test.csv'

df = pd.read_csv(csv_file)

score_1_data = df[df['score'] == 1]
 
groups = score_1_data.groupby('score')

for name, group in groups:
    output_file = f'score_{name}_data.csv'
    group.to_csv(output_file, index=False)
    print(f'Saved {len(group)} rows with score {name} to {output_file}')