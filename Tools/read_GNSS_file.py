import pandas as pd

def read_GNSS_file(filename, region):
    gnss = pd.read_csv(filename, sep=r'\s+', skiprows=1, names=['Lon', 'Lat', 'VE', 'VN', 'VU', 'SE', 'SN', 'SU', 'ID'],
                       dtype = {'Lon': float, 'Lat': float, 'VE': float, 'VN': float, 'VU': float, 'SE': float, 'SN': float, 'SU': float, 'ID': str})
    mask = (gnss['Lat'] > region[0]) & (gnss['Lat'] < region[1]) & (gnss['Lon'] > region[2]) & (gnss['Lon'] < region[3])
    gnss = gnss[mask]
    return gnss
