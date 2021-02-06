## Importing JSON Data and Working with APIs

Learn how to work with JSON data and web APIs by exploring a public dataset and getting cafe recommendations from Yelp. End by learning some techniques to combine datasets once they have been loaded into data frames.

<br>

### Load JSON data

```
# Load pandas as pd
import pandas as pd

# Load the daily report to a data frame
pop_in_shelters = pd.read_json('dhs_daily_report.json')

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())
```

### Work with JSON orientations

```
try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient='split')
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")
```

### Get data from an API

```
# Create dictionary to query API for cafes in NYC
parameters = {'term':'cafe',
          	  'location':'NYC'}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                params=parameters,
                headers=headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data['businesses'])
print(cafes.head())
```

### Set API parameters

```
# Create dictionary to query API for cafes in NYC
parameters = {'term':'cafe',
          	  'location':'NYC'}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                params=parameters,
                headers=headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data['businesses'])
print(cafes.head())
```

### Set request headers

```
# Create dictionary that passes Authorization and key string
headers = {'Authorization': "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                        params=params,
                        headers=headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print names
cafes = pd.DataFrame(data['businesses'])
print(cafes.name)
```

### Flatten nested JSONs

```
# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a data frame, replace separator
cafes = json_normalize(data["businesses"],
                       sep="_")

# View data
print(cafes.head())
```

### Handle deeply nested data

```
# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=['name', 
                                  'alias',  
                                  'rating',
                          		  ['coordinates', 'latitude'], 
                          		  ['coordinates', 'longitude']],
                    		meta_prefix='biz_')

# View the data
print(flat_cafes.head())
```

### Merge data frames

```
# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, 
                   			   left_on="location_zip_code", 
                               right_on="zipcode")

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on="puma")

# View the data
print(cafes_with_pop.head())
```