latest_telemetry = {}

def update_telemetry(data):
    global latest_telemetry
    latest_telemetry = data

def get_latest_telemetry():
    return latest_telemetry