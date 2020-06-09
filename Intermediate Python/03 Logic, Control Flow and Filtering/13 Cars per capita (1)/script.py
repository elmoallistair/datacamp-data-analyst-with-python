# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
many_cars = cars['cars_per_cap'] > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)