#include <iostream>
#include <simdxjson.h>
#include <fstream>
#include <string>

void countTypeFields(const simdjson::dom::element& element, int& typeCount) {
    // Check if the current element is an object
    if (element.is_object()) {
        // Iterate over each key-value pair in the object
        for (auto [key, value] : element.get_object()) {
            // Check if the key is "type"
            if (key == "type") {
                ++typeCount;
            }
            // Recursively call countTypeFields for nested elements
            countTypeFields(value, typeCount);
        }
    }
    // Check if the current element is an array
    else if (element.is_array()) {
        // Iterate over each element in the array
        for (auto child : element.get_array()) {
            // Recursively call countTypeFields for array elements
            countTypeFields(child, typeCount);
        }
    }
    // Otherwise, it's a scalar value (string, number, boolean, null), do nothing
}
int main() {
    // Open the JSON file
    std::ifstream file("/home/spirals/Documents/crossref/crossref4.json");

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

    // Count the "type" fields recursively
    int typeCount = 0;
    countTypeFields(doc, typeCount);

    // Print the number of "type" fields found
    std::cout << "Number of type fields: " << typeCount << std::endl;

    return 0;
}



