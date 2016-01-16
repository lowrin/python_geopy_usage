from geopy.geocoders import Nominatim
import pandas as pd


# geopy init
geolocator = Nominatim()

# load the excel file into the dataframe
df = pd.read_excel("daten_2.xlsx",sheetname="input_data",index_col=0,header=0)

# add new columns
df.insert(1,"lat","")
df.insert(1,"lon","")

# iterate through rows and add the lat and lon
for index,row in df.iterrows():
    location = geolocator.geocode(row["Ort"])
    print(location.address)
    df.loc[index, 'lat'] = location.latitude
    df.loc[index, 'lon'] = location.longitude

# add new column
df.insert(15,"male/female","")
# iterate through rows and add a calculated field
for index,row in df.iterrows():
    df.loc[index, 'male/female'] = row["Männer"] / row["Frauen"]

print(df.head())

# save as xlsx file
df.to_excel('data_3.xlsx', sheet_name='Sheet1')



