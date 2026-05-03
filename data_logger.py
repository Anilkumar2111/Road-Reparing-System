import csv
import os

FILE_PATH = "data/potholes.csv"

def init_file():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Distance", "Latitude", "Longitude"])

def log_data(distance, lat, lon):
    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([distance, lat, lon])