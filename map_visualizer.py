import folium
import csv

def generate_map():
    map = folium.Map(location=[23.34, 85.30], zoom_start=13)

    with open('data/potholes.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            lat = float(row[1])
            lon = float(row[2])

            folium.Marker([lat, lon], popup="Pothole").add_to(map)

    map.save("output/map.html")