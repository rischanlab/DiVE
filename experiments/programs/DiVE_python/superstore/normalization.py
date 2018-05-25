import pandas as pd

xl = pd.ExcelFile("results_ship_mode_first_class.xlsx")
df = xl.parse("Sheet1", header=0)
lower, upper = 0.0, 0.5
df['Utility'] = df['Utility'].apply(lambda x: lower + (upper - lower) * x)
df = df.drop(['ID'],axis=1)
writer = pd.ExcelWriter('result_ship_mode_first_class_norm.xlsx')
df.to_excel(writer,'Sheet1', index=0)
writer.save()