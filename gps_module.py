import random

def get_location():
    # Simulated coordinates near Jharkhand
    lat = 23.34 + random.uniform(-0.01, 0.01)
    lon = 85.30 + random.uniform(-0.01, 0.01)

    return lat, lon