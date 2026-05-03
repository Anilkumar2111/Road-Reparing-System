import time
import random
from detector import detect_pothole
from gps_module import get_location
from data_logger import init_file, log_data
from map_visualizer import generate_map

def simulate_sensor():
    # simulate distance values
    return random.randint(5, 30)

def main():
    print("🚧 Road Damage Detection System Started")

    init_file()

    for i in range(20):  # run 20 cycles
        distance = simulate_sensor()
        print(f"Distance: {distance} cm")

        if detect_pothole(distance):
            print("Pothole Detected!")

            lat, lon = get_location()
            print(f"Location: {lat}, {lon}")

            log_data(distance, lat, lon)

        time.sleep(1)

    print("📍 Generating Map...")
    generate_map()
    print("✅ Map saved in output/map.html")

if __name__ == "__main__":
    main()