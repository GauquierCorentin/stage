import json
from jsonpath_ng import jsonpath, parse

def search_json_path(json_data, path_expression):
    jsonpath_expr = parse(path_expression)

    matches = [match.value for match in jsonpath_expr.find(json_data)]

    return matches

def main():
    with open('crossref4.json', 'r') as file:
        json_data = json.load(file)

    path_expression = '$..author'

    authors = search_json_path(json_data, path_expression)

    for author in authors:
        print(author)

if __name__ == "__main__":
    main()
