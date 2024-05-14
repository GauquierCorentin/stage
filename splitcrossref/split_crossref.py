import json

def split_json_file(filename, num_parts):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
   
    # Assumons que les données sont sous une clé 'items'
    items = data['items']
   
    # Diviser les données en parties égales
    total_items = len(items)
    part_size = total_items // num_parts
    parts = []

    for i in range(num_parts):
        start_index = i * part_size
        # Assurer que le dernier morceau inclut tous les éléments restants
        end_index = (i + 1) * part_size if i < num_parts - 1 else total_items
        part = items[start_index:end_index]
        parts.append(part)

    return parts

def write_json_parts(parts, base_filename):
    for i, part in enumerate(parts):
        part_filename = f"{base_filename}_part{i+1}.json"
        with open(part_filename, 'w', encoding='utf-8') as file:
            json.dump({"items": part}, file, indent=2)
        print(f"Écrit {len(part)} éléments dans {part_filename}")

def main():
    input_filename = '../crossref16.json'
    num_parts = 20

    parts = split_json_file(input_filename, num_parts)
    write_json_parts(parts, 'crossref16')

if __name__ == "__main__":
    main()



