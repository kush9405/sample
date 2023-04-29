
# Define a list of dictionaries to store information about the government schemes
schemes = [
  {"name": "Pradhan Mantri Jan Dhan Yojana (PMJDY)", "age_min": 10, "age_max": 100, "gender": "male" or  "female", "income_min": 0},
  {"name": "Pradhan Mantri Awas Yojana (PMAY)", "age_min": 18, "age_max": 65, "gender": "Male" or "Female", "income_max": 85000},
  {"name": "Deen Dayal Upadhyaya Grameen Kaushalya Yojana (DDU-GKY).", "age_min": 6, "age_max": 18, "gender": "male" or "Female", "income_min": 0},
  {"name": "National Rural Employment Guarantee Act (NREGA)", "age_min": 18, "age_max": 60, "gender": "male" or "female", "income_min": 0},
  {"name": "Pradhan Mantri Garib Kalyan Ann Yojana", "age_min": 18, "age_max": 60, "gender":"male" or "female", "income_min": 0},
  {"name": "Pradhan Mantri Sahaj Bijli Har Ghar Yojana", "age_min": 18, "age_max": 100, "gender": "male" or "female", "income_min": 10000},
]  

# Define the selection criteria
age = "myAge"
gender = "myGender"
income = "myIncome"

# Filter the schemes based on the selection criteria
filtered_schemes = [scheme for scheme in schemes if scheme["age_min"] <= age <= scheme["age_max"] and scheme["gender"] == gender and scheme["income_min"] <= income]

# Display the filtered schemes
for scheme in filtered_schemes:
  print(scheme["name"])