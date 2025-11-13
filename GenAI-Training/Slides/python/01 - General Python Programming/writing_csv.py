# WRITING CSV FILES

import csv

# Writing to a CSV file with comma as the default delimiter
with open('model_performance.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Writing the header row
    writer.writerow(['Model Version', 'Accuracy', 'Response Time (ms)', 'Tokens'])

    # Each tuple in the list represents a row
    models = [
        ('GPT-4', 98.7, 45, 300),
        ('GPT-4o', 99.7, 42, 350)
    ]

    # Writing each model's data to the CSV file
    for model in models:
        writer.writerow(model)

# Writing to a tab-separated CSV file
with open('tab_separated_logs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')

    # Writing the header row
    writer.writerow(['Date', 'Latency (ms)', 'Request Count'])

    # Writing a single log entry
    writer.writerow(['2023-11-01', 60, 1500])
