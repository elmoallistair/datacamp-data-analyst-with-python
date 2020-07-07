# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], 
                                             format="%m%d%y %H:%M:%S")

# Print first few values of Part2EndTime
print(survey_data['Part2EndTime'].head())