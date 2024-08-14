import pandas as pd
df = pd.read_excel('JCM.01304-20-sd004.xlsx',sheet_name='WHO database', skiprows=5)
df.to_csv('extracted_table.csv', index=False)