# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM employee WHERE employeeid >= 6 ORDER BY birthdate', engine)

# Print head of DataFrame
print(df.head())