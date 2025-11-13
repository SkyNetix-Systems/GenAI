# READING CSV FILES IN PYTHON

import csv

# Open the CSV file in read mode
with open('model_logs.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)  # Create a CSV reader object

    next(reader)  # Skip the header row

    # Create a dictionary: {date: token_count}
    token_data = {row[0]: int(row[3]) for row in reader}

    # Find the day with the highest token generation
    peak_day = max(token_data, key=token_data.get)

    # Display the peak day and the number of tokens generated
    print(f'Peak Model Usage: {peak_day}, Tokens Generated: {token_data[peak_day]}')
    # => Peak Model Usage: 2023-02-26, Tokens Generated: 500
