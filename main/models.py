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
<<<<<<< HEAD
=======
    

class WeatherStation(models.Model):
    station_name = models.CharField(max_length=100)
    station_loc = models.CharField(max_length=100) # fetch GPS coord here in the future
    temperature = models.FloatField(null=True,blank=True)
    humidity = models.FloatField(null=True,blank=True)
    pressure = models.IntegerField(null=True,blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)
    previous_reading = models.DateTimeField(auto_now_add=True) 
    
    
    def __str__(self):
        return(
        f"{self.station_name} at {self.desc}"
        f"measured : {self.previous_reading.strftime('%Y-%m-%d %H:%M')}")
    

>>>>>>> master
