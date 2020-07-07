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