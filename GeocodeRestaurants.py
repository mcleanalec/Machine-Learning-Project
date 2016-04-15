#!/usr/bin/env python
import pandas as pd
import geopy
from supportFunctions.GEOCODING import geocoding


if __name__ == '__main__':
    data = pd.read_csv('restaurants_inspection.csv')
    geocoding(data, coder=geopy.geocoders.Nominatim(),
              address='Address', n_init=0, n_end=-1)
