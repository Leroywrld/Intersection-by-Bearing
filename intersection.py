import math
class IntersectByBearing:
    def __init__(self, northing_a: float, easting_a: float, northing_b: float, easting_b: float, bearing_1: float, bearing_2: float):
        
        assert northing_a >= 0, "northing of point a cannot be negative"
        assert easting_a >= 0, "easting of point a cannot be negative"
        assert northing_b >= 0, "northing of point b cannot be negative"
        assert easting_b >= 0, "easting of point b cannot be negative"
        assert bearing_1 >= 0, "bearings cannot be negative"
        assert bearing_2 >= 0, "bearings cannot be negative"
        
        
        self.northing_a = northing_a
        self.easting_a = easting_a
        self.northing_b = northing_b
        self.easting_b = easting_b
        self.bearing_1 = bearing_1
        self.bearing_2 = bearing_2
        
    def get_delta_northing_ac(self):
        numerator = (self.northing_b - self.northing_a)*(math.tan(math.radians(self.bearing_2))) - (self.easting_b-self.easting_a)
        tan_bearing_one = math.tan(math.radians(self.bearing_1))
        tan_bearing_two = math.tan(math.radians(self.bearing_2))
        delta_northing_ac = numerator / (tan_bearing_two - tan_bearing_one)
        return delta_northing_ac
    
    def get_delta_easting_ac(self):
        delta_northing_ac = self.get_delta_northing_ac()
        tan_bearing_one = math.tan(math.radians(self.bearing_1))
        delta_easting_ac = delta_northing_ac * tan_bearing_one
        return delta_easting_ac
    def get_northing_c(self):
        delta_northing_ac = self.get_delta_northing_ac()
        northing_c = self.northing_a + delta_northing_ac
        return northing_c
    def get_easting_c(self):
        delta_easting_ac = self.get_delta_easting_ac()
        easting_c = self.easting_a + delta_easting_ac
        return easting_c
        
    
ibb = IntersectByBearing(4016, 3076, 1120, 2101, 110.5111111, 46.50555556)
print(f"change in northing btwn points a & c: {ibb.get_delta_northing_ac()}")
print(f"change in easting btwn points a & c: {ibb.get_delta_easting_ac()}")
print(f"northing c: {ibb.get_northing_c()}")
print(f"easting c: {ibb.get_easting_c()}")