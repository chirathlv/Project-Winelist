# Import the geocoders and pandas
from geopy.geocoders import Nominatim
import pandas as pd

# Fetch Geo Codes and append to the existing DataFrame
def add_coordinates(df):
    # Initializing Geolocator object
    geolocator = Nominatim(user_agent="http")
    # Lat and Long list to store coordinates
    Lat_list, Long_list = [], []

    # Iterate eah rows and get County and State and passing to geolocator
    for i, row in df[['County','State']].iterrows():
        # get coordinates using geolocator
        coordinates = geolocator.geocode(f"{row['County']}, {row['State']}")

        # Append the latitude to Lat_list
        Lat_list.append(coordinates.latitude)

        # Append the latitude to Long_list
        Long_list.append(coordinates.longitude)

    new_data = pd.DataFrame({
        'Lat': Lat_list,
        'Lon': Long_list
    })

    # Reset the index before joining
    df.reset_index(drop=True, inplace=True)

    # Concat the existing df with the new data and return
    return pd.concat([df,new_data], axis='columns', join='inner')