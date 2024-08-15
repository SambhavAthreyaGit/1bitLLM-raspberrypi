from datasets import load_dataset
import csv

def process_dataset(dataset):
    formatted_data = []
    total_items = len(dataset)
    
    for i, item in enumerate(dataset):
        command = item.get('Command', 'Unknown command')
        description = item.get('Text', 'Description not found')

        formatted_data.append({
            'command': command,
            'description': description,
        })

        if i % 100 == 0:
            print(f"Processing item {i}/{total_items}...")

    return formatted_data

def save_to_csv(data, filename="formatted_command_dataset.csv"):
    """Save the dataset to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['command', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)
    print(f"Dataset saved to {filename}")

dataset = load_dataset("tmskss/linux-man-pages-tldr-summarized")
formatted_data = process_dataset(dataset['train'])

save_to_csv(formatted_data)
