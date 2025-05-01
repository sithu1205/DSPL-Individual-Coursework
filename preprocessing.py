import pandas as pd
df = pd.read_csv('D:\Streamlit\DSPL-Individual-Coursework\Places for Travel-Dining-Recreational activities and Information of travel agents.csv')

#Replacing missing values in 'Grade' with 'Not Graded'
df["Grade"].fillna("Not Graded", inplace=True)

#Droping rows where 'District', 'AGA Division', or 'PS/MC/UC' contain 'N/A'
columns_to_check = ["District", "AGA Division", "PS/MC/UC"]
df = df[~df[columns_to_check].isin(["N/A"]).any(axis=1)]

# Drop rows with NaN in those columns
df = df.dropna(subset=columns_to_check)

# Drop rows with blank or whitespace-only strings in those columns
df = df[~df[columns_to_check].apply(lambda x: x.str.strip() == "").any(axis=1)]


df.to_csv("cleaned_Places for Travel-Dining-Recreational activities and Information of travel agents.csv")
