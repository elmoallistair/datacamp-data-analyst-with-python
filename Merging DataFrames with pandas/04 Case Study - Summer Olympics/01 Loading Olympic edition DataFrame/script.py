#Import pandas
import pandas as pd

# Create file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'

# Load DataFrame from file_path: editions
editions = pd.read_csv('Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv', sep='\t')

# Extract the relevant columns: editions
editions = editions[['Edition','Grand Total','City','Country']]

# Print editions DataFrame
print(editions)