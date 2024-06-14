

#include <iostream>
#include <simdjson.h>
#include <fstream>
#include <string>

void printTypeFields(const simdjson::dom::element& element) {
    // Check if the current element is an object
    if (element.is_object()) {
        // Iterate over each key-value pair in the object
        for (auto [key, value] : element.get_object()) {
            // Check if the key is "type"
            if (key == "URL") {
                std::cout << "URL: " << value.get_string() << std::endl;
            }
            // Recursively call printTypeFields for nested elements
            printTypeFields(value);
        }
    }
    // Check if the current element is an array
    else if (element.is_array()) {
        // Iterate over each element in the array
        for (auto child : element.get_array()) {
            // Recursively call printTypeFields for array elements
            printTypeFields(child);
        }
    }
    // Otherwise, it's a scalar value (string, number, boolean, null), do nothing
}

int main() {
    // Open the JSON file
    std::ifstream file("/home/spirals/Documents/crossref/crossref0.json");

    if (!file.is_open()) {
        std::cerr << "Failed to open file." << std::endl;
        return 1;
    }

    // Read the JSON data from the file into a string
    std::string json;
    std::string line;
    while (std::getline(file, line)) {
        json += line;
    }

    // Close the file
    file.close();

    // Parse the JSON string using SIMDjson
    simdjson::dom::parser parser;
    simdjson::dom::element doc = parser.parse(json);

    // Print the "type" fields recursively
    printTypeFields(doc);

    return 0;
}

