import ijson
import json

def split_large_json(input_file, output_prefix, chunk_size):
    with open(input_file, 'r') as file:
        parser = ijson.items(file, 'item')
        chunk = []
        chunk_count = 0

        for index, item in enumerate(parser):
            chunk.append(item)
            if (index + 1) % chunk_size == 0:
                output_file = f"{output_prefix}_{chunk_count}.json"
                with open(output_file, 'w') as chunk_file:
                    json.dump(chunk, chunk_file)
                chunk_count += 1
                chunk = []

        # Write any remaining items in the last chunk
        if chunk:
            output_file = f"{output_prefix}_{chunk_count}.json"
            with open(output_file, 'w') as chunk_file:
                json.dump(chunk, chunk_file)

if __name__ == "__main__":
    input_file = '../crossref16.json'  # Remplacez par le chemin de votre fichier JSON
    output_prefix = 'crossref16chunk'  # Préfixe pour les fichiers de sortie
    chunk_size = 200000  # Nombre d'éléments par fichier, ajustez selon vos besoins

    split_large_json(input_file, output_prefix, chunk_size)
