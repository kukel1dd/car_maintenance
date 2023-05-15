"""A class for checking on some information about the car."""
class Car:
    def __init__(self, make, model, year, current_mileage):
        self.make = make
        self.model = model
        self.year = year
        self.current_mileage = current_mileage
        self.next_change = 0
        
        self.current_miles = current_mileage
    def format_name(self):
        """A simple function to format the name of your car."""
        car_name = f"{self.year} {self.make} {self.model}"
        return car_name.title()
    

    
    def oil_change(self, Miles_Last_change):
        """a simple function to check how many miles until your next oil change."""
        self.next_change = 5000 - (self.current_mileage - Miles_Last_change)
        
        print(f'you have {self.next_change} miles until your next oil change. make sure to check your oil atleast a few times in the next few months!')
        
    
    
    def estimate_days(self, miles_per_day):
        """A function to roughly estimate the weeks until your next change, based off of a normal day of driving."""
        days_till_change = self.next_change // miles_per_day 
        print(f"you have roughly {days_till_change} until your next oil change.")
        weeks = days_till_change // 7
        print(f"roughly {weeks} weeks.")
        


# my_car = Car('nissan', 'sentra', 2015, 82148)

# print(my_car.format_name())
# my_car.oil_change(82016)
# my_car.estimate_days(36)