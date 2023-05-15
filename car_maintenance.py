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
        if Miles_Last_change > self.current_mileage:
            print("\nyour current miles cant be less than your last change!")
        elif self.next_change <= 0:
            print("\nLooks like you need an oil change!")
        else:
            print(f'\nYou have {self.next_change} miles until your next oil change. make sure to check your oil atleast a few times in the next few months!')
        
    
    
    def estimate_days(self, miles_per_day):
        """A function to roughly estimate the weeks until your next change, based off of a normal day of driving."""
        days_till_change = self.next_change // miles_per_day 
        if days_till_change <= 0:
            print("\nYou need an oil change!")
        else:
            print(f"\nYou have roughly {days_till_change} days until your next oil change.")
            weeks = days_till_change // 7
            print(f"\nroughly {weeks} weeks.")
        



cars_make = input("Enter the make of your car: ")
car_model = input('Enter the model of your car: ')
car_year = input('Enter the year of your car: ')

car_mileage = int(input('Enter your current mileage: '))
my_car = Car(cars_make, car_model, car_year, car_mileage)
print(my_car.format_name())
car_last_chage = int(input("\nEnter your mileage at your last oil change:"))
my_car.oil_change(car_last_chage)
miles_a_day = int(input("Enter your miles of an average day of driving: "))
my_car.estimate_days(miles_a_day)
