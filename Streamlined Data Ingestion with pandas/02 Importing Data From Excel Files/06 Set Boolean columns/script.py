# 1/2
# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())

# 2/2
# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype=({'HasDebt':'bool'}))

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())