# Create dict specifying data types for agi_stub and zipcode
data_types = {'agi_stub':'category',
			  'zipcode':'str'}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())