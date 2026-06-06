from pydantic import BaseModel


class VehicleTelemetry(BaseModel):
    vehicle_id: str
    timestamp: str
    speed: int
    battery_level: int
    signal_strength: int
    network_status: str
    ota_status: str