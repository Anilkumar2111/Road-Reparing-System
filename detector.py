def detect_pothole(distance):
    THRESHOLD = 20  # adjust based on testing

    if distance > THRESHOLD:
        return True
    return False