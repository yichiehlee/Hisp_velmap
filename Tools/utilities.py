import pandas as pd

def read_GNSS_file(filename, region):
    gnss = pd.read_csv(filename, sep=r'\s+', skiprows=1, names=['Lon', 'Lat', 'VE', 'VN', 'VU', 'SE', 'SN', 'SU', 'ID'],
                       dtype = {'Lon': float, 'Lat': float, 'VE': float, 'VN': float, 'VU': float, 'SE': float, 'SN': float, 'SU': float, 'ID': str})
    mask = (gnss['Lat'] > region[0]) & (gnss['Lat'] < region[1]) & (gnss['Lon'] > region[2]) & (gnss['Lon'] < region[3])
    gnss = gnss[mask]
    return gnss


def setup_grid(num_tracks, region, inc):
    # 1. Setup parameters
    n_tracks = num_tracks
    
    # 2. Create coordinate vectors
    grid_lon = np.arange(region[2], region[3], inc)
    grid_lat = np.arange(region[0], region[1], inc)
    
    # 3. Get dimensions
    nrows = grid_lat.shape[0]
    ncols = grid_lon.shape[0]
    
    # 4. Create the meshgrid
    grid_lon_mesh, grid_lat_mesh = np.meshgrid(grid_lon, grid_lat)
    
    return grid_lon_mesh, grid_lat_mesh, nrows, ncols
