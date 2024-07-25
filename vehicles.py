class vehicles:
    def __init__(self):
        self.available_vehicles={
            'car':4,
            'bike':2,
            'bicycle':10,
            'jeep':2
        }
        self.rented_vehicles={
            'car':0,
            'bike':0,
            'bicycle':0,
            'jeep':0    
        }
        
    def display_available_vehicles(self):
        for vehicle,count in self.available_vehicles.items():
            print(f'{vehicle}:{count}')
            
    def rent_vehicle(self,vehicle):
        if vehicle in self.available_vehicles and self.available_vehicles[vehicle]>0:
            self.available_vehicles[vehicle]-=1
            self.rented_vehicles[vehicle]+=1
        return self.available_vehicles[vehicle],self.rented_vehicles[vehicle]
    
    def return_vehicle(self,vehicle):
        if vehicle in self.rented_vehicles and self.rented_vehicles[vehicle]>0:
            self.rented_vehicles[vehicle]-=1
            self.available_vehicles[vehicle]+=1
        return self.rented_vehicles[vehicle],self.available_vehicles[vehicle]
    
vehicle= vehicles()
vehicle.display_available_vehicles()

vehicle.rent_vehicle('car')
vehicle.display_available_vehicles()
        
vehicle.rent_vehicle('bicycle')
vehicle.display_available_vehicles()

vehicle.return_vehicle('car')
vehicle.display_available_vehicles() 
           
