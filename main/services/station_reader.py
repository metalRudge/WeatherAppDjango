import json
from pathlib import Path
from django.conf import settings
from dataclasses import dataclass
from datetime import datetime
"""
def normalize_station(station):
    telemetry = station.get("telemetry", {})

    return {
        "station_id": station.get("station_id"),
        "station_name": station.get("station_name"),
        "location": station.get("location"),
        "measured_at": station.get("measured_at"),
        "temperature_c": telemetry.get("temperature_c"),
        "humidity_pct": telemetry.get("humidity_pct"),
        "pressure_hpa": telemetry.get("pressure_hpa"),
        "perspiration": telemetry.get("perspiration"),
        "battery_v": telemetry.get("battery_v"),
        "signal_rssi": telemetry.get("signal_rssi"),
        "status": telemetry.get("status"),
        "batch_error": station.get("batch_error"),
    }
"""
@dataclass
class StationTelemetry:
    station_id: str
    station_name: str
    measured_at: datetime
    temperature_c: float | None
    humidity_pct: float | None
    pressure_hpa: float | None
    perspiration: float | None
    battery_v: float | None
    signal_rssi: int | None
    status: str
    batch_error: str | None



def load_stations_data():
    file_path = Path(settings.BASE_DIR) / "main" / "mock_data" / "station1.json"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data, None
    except FileNotFoundError:
        return None,"No station data found."
    except json.JSONDecodeError:
        return None,"JSON could not be read, invalid format"
    except OSError:
        return None,"JSON file couldn't be openend"