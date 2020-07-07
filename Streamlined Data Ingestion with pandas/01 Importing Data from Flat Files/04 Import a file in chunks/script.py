# Create data frame of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=vt_data_first500.columns)

# View the Vermont data frames to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())