def generate_alerts(data):

    alerts = []

    if data.get("battery_level", 100) < 25:
        alerts.append("LOW_BATTERY")

    if data.get("signal_strength", -50) < -100:
        alerts.append("POOR_SIGNAL")

    if data.get("network_status") == "DISCONNECTED":
        alerts.append("VEHICLE_OFFLINE")

    return alerts

def calculate_health_score(data):

    score = 100

    if data.get("battery_level", 100) < 25:
        score -= 30

    if data.get("signal_strength", -50) < -100:
        score -= 20

    if data.get("network_status") == "DISCONNECTED":
        score -= 40

    return max(score, 0)