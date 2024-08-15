from datasets import load_dataset
import json

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

dataset = load_dataset("tmskss/linux-man-pages-tldr-summarized")
formatted_data = process_dataset(dataset['train'])
with open('formatted_command_dataset.json', 'w') as f:
    json.dump(formatted_data, f, indent=2)
