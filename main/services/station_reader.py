import json
from pathlib import Path
from django.conf import settings
from dataclasses import dataclass
from datetime import datetime
from ..models import WeatherStation

@dataclass
class StationTelemetry:
    station_id: str
    station_name: str | None
    station_loc :str    | None
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
    try:
        stations = WeatherStation.objects.order_by('-previous_reading')
        stations_data = [
            StationTelemetry(
                station_id=station.station_id,
                station_name=station.station_name,
                station_loc=station.station_loc,
                measured_at=station.previous_reading,
                temperature_c=station.temperature,
                humidity_pct=station.humidity_pct,
                pressure_hpa=station.pressure_hpa,
                perspiration=station.perspiration,  # Placeholder for future data
                battery_v=station.battery_v,    # Placeholder for future data
                signal_rssi=station.signal_rssi,  # Placeholder for future data
                status= station.status,  #if station.is_online else "Offline",Placeholder for future status logic, implement stations.is_online property in the future
                batch_error=station.batch_error   # Placeholder for future error handling
                )
            for station in stations
        ]
        return stations_data, None
    except Exception as e:
        return None, f"Error fetching stations from database: {str(e)}"