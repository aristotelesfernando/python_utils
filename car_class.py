class Car:    

    def __init__(self, color, mileage_initial):
        self.color = color        
        self.mileage_initial = mileage_initial
        self.mileage_total = mileage_initial

        
    def drive(self, mileage_driven):
        self.mileage_total = self.mileage_total + mileage_driven

