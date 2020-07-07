# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, 
                   			   left_on="location_zip_code", 
                               right_on="zipcode")

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on="puma")

# View the data
print(cafes_with_pop.head())