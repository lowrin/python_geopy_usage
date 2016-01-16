import pandas as pd

# load the excel file into the dataframe
df = pd.read_excel("data_3.xlsx",sheetname="Sheet1",header=0)

# select only the columns which will be used
# only nice to have
#df = df[[0,1,2,7,8]]

# goal data frame
df2 = pd.DataFrame(columns=['ort-id', 'ort', 'lat','lon', 'Geschlecht', 'Anzahl (Geschlecht)'])


for index,row in df.iterrows():
    df2.loc[df2.size] = [row["id"], row["Ort"], row["lat"],row["lon"], 'Maennlich', row["Männer"]]
    df2.loc[df2.size] = [row["id"], row["Ort"], row["lat"],row["lon"], 'Weiblich', row["Frauen"]]

# reset index
df2 = df2.reset_index(drop=True)

# print head to console
print(df2)

df2.to_excel('data_6.xlsx', sheet_name='Sheet1')
print("end")

