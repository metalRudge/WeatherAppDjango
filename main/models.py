from django.db import models
class SearchHistory(models.Model):
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    pressure = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city_name} at {self.searched_at.strftime('%Y-%m-%d %H:%M')}"

class WeatherStation(models.Model):
    station_id = models.CharField(max_length=50, unique=True, null=False, blank=False,default="")
    station_name = models.CharField(max_length=100)
    measured_at = models.DateTimeField(null=True, blank=True, default=None)
    station_loc = models.CharField(max_length=100) # fetch GPS coord here in the future
    temperature = models.FloatField(null=True,blank=True)
    humidity_pct = models.FloatField(null=True,blank=True)
    pressure_hpa = models.FloatField(null=True,blank=True)
    perspiration = models.FloatField(null=True,blank=True) # Placeholder for future data    
    battery_v = models.FloatField(null=True,blank=True) # Placeholder for future data
    signal_rssi = models.IntegerField(null=True,blank=True) # Placeholder for future data
    desc = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True) # Placeholder for future status logic
    previous_reading = models.DateTimeField(auto_now_add=True) 
    batch_error = models.CharField(max_length=255, null=True, blank=True) # Placeholder for future error handling
    
    
    def __str__(self):
        return(
        f"{self.station_name} at {self.desc}"
        f"measured : {self.previous_reading.strftime('%Y-%m-%d %H:%M')}")


"""class StationTelemetry:
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
    """