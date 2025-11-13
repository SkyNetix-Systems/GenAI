class Robot:
    """
    This class implements a Robot.
    """
    population = 0  # Class attribute to track the number of Robot instances

    def __init__(self, name, price):
        # Initialize the Robot with a name and price
        self.name = name
        self.price = price
        Robot.population += 1  # Increment population count when a new robot is created

    def __str__(self):
        # String representation of the Robot instance
        return 'My name is ' + self.name + ' and my price is ' + str(self.price)

    def __add__(self, other):
        # Overload the '+' operator to sum the prices of two Robot instances
        return self.price + other.price


# Create two Robot instances
r1 = Robot("Marvin", 150)
r2 = Robot('Calvin', 100)

# Print the string representation of the first Robot
print(r1)

# Use the overloaded '+' operator to sum the prices of both robots
print(r1 + r2)
