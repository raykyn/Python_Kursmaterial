
import pandas as pd
import numpy as np
from tqdm import tqdm

def create_geo_df(cities, cities_df):
    """Create a DF with 'original Name', 'standard name', 'longitude', 'latitude'
    :inputs 
        - cities: A list of city names
        - cities_df: a pandas df "city name" "alternate names: list(str)" and coordinates (a string of lat,lon)
    """
    lons = []
    lats = []
    cities_output = []
    cities_orig_name = []
    cities_not_found = []
    cities_multiple_matches = []
    for city in tqdm(cities):
        if city in list(cities_df["Name"]):
            lat,lon = cities_df[cities_df["Name"]==city]["Coordinates"].iloc[0].split(",")
            official_name = city

        
        else:  # Check for a cityname in the alternate names
            possibilities = []
            for city_names in list(cities_df["Alternate Names"].dropna()):
                
                if city in city_names.split(","):
                    city_data = cities_df[cities_df["Alternate Names"]==city_names]
                    lat, lon = city_data["Coordinates"].iloc[0].split(",")
                    official_name = city_data["Name"].iloc[0]  # Use the now official name!!
                    possibilities.append(official_name)
            
            if len(possibilities) == 0:
                cities_not_found.append(city)
                continue
            elif len(possibilities) > 1:
                cities_multiple_matches.append([city, possibilities])
                continue                
        lons.append(lon)
        lats.append(lat)
        cities_output.append(official_name)
        cities_orig_name.append(city)
    
    return pd.DataFrame.from_dict({"city_orig_name":cities_orig_name, "city": cities_output, "lon": lons, "lat": lats}), cities_not_found, cities_multiple_matches


def create_arrow_data(origin_point, coordinate_df):
    """Create a df for the arrows
    Inputs:
        - origin_point: a Tuple or list with two coordinates (lat, lon)
        - coordinate_df: and pandas df with columns lat and lon
        
    Outputs:
        - Two lists for lats and lon of the form: [start, end, None, start, end, None, etc.]
        """

    start_lats = []
    start_lons = []
    end_lats = []
    end_lons = []


    for coordinate in coordinate_df.iloc:
        start_lats.append(origin_point[1])
        start_lons.append(origin_point[0])
        end_lats.append(coordinate.lat)
        end_lons.append(coordinate.lon)

    # Creating the vectors for plotting
    lons = np.empty(3 * len(start_lons))
    lons[::3] = start_lons
    lons[1::3] = end_lons
    lons[2::3] = None
    lats = np.empty(3 * len(start_lats))
    lats[::3] = start_lats
    lats[1::3] = end_lats
    lats[2::3] = None
    return lons, lats