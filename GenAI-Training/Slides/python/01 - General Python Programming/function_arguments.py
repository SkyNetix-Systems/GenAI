# FUNCTION ARGUMENTS

# TYPES OF FUNCTION ARGUMENTS:
# 1. **Positional Arguments** - Arguments that must be passed in the correct order.
# 2. **Keyword (Named) Arguments** - Arguments that are explicitly named when passed.
# 3. **Default Arguments** - Arguments that take a default value if not provided.
# 4. *args (Arbitrary Positional Arguments) - Allows passing multiple positional arguments.
# 5. **kwargs (Arbitrary Keyword Arguments) - Allows passing multiple keyword arguments.

# POSITIONAL AND KEYWORD ARGUMENTS

def display_weather(temp, humidity, wind_speed):
    """Displays the weather conditions."""
    print(f'Temperature: {temp}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} km/h')

# Using keyword arguments (order does not matter)
display_weather(humidity=70, temp=22, wind_speed=15)

# Mixing positional and keyword arguments (order still matters for positional)
display_weather(70, wind_speed=15, humidity=22)

# ❌ This will cause a **SyntaxError**
# display_weather(humidity=70, 15, temp=22)  # Positional argument after keyword argument is not allowed

# DEFAULT ARGUMENTS

def adjust_lighting(room, brightness=75, color_temp=4000):
    """Adjusts lighting settings for a given room."""
    print(f'Adjusting lighting in {room} to {brightness}% brightness and {color_temp}K color temp.')

# Function calls with default values
adjust_lighting('Living Room')  # Uses default brightness (75) and color_temp (4000)
adjust_lighting('Bedroom', 50)  # Overrides brightness, keeps default color_temp
adjust_lighting('Kitchen', 50, 3500)  # Overrides both brightness and color_temp
