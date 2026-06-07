fleet_telemetry = {}


def update_telemetry(data):
    vehicle_id = data.get("vehicle_id")

    if vehicle_id:
        fleet_telemetry[vehicle_id] = data


def get_latest_telemetry():
    if not fleet_telemetry:
        return {}

    latest_vehicle = list(fleet_telemetry.keys())[-1]
    return fleet_telemetry[latest_vehicle]


def get_fleet_telemetry():
    return fleet_telemetry