from backend.alert_engine import generate_alerts, calculate_health_score


def test_low_battery_alert():
    data = {
        "battery_level": 20,
        "signal_strength": -80,
        "network_status": "CONNECTED",
    }

    alerts = generate_alerts(data)

    assert "LOW_BATTERY" in alerts


def test_poor_signal_alert():
    data = {
        "battery_level": 80,
        "signal_strength": -105,
        "network_status": "CONNECTED",
    }

    alerts = generate_alerts(data)

    assert "POOR_SIGNAL" in alerts


def test_vehicle_offline_alert():
    data = {
        "battery_level": 80,
        "signal_strength": -80,
        "network_status": "DISCONNECTED",
    }

    alerts = generate_alerts(data)

    assert "VEHICLE_OFFLINE" in alerts


def test_health_score_good_vehicle():
    data = {
        "battery_level": 90,
        "signal_strength": -70,
        "network_status": "CONNECTED",
    }

    score = calculate_health_score(data)

    assert score == 100


def test_health_score_critical_vehicle():
    data = {
        "battery_level": 20,
        "signal_strength": -105,
        "network_status": "DISCONNECTED",
    }

    score = calculate_health_score(data)

    assert score == 10