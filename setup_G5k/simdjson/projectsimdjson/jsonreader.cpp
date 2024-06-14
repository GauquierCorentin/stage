#include <iostream>
#include <simdjson.h>
#include <fstream>
#include <string>

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

    // Access the "author" fields and print their values
    simdjson::dom::object obj;
    simdjson::error_code error = doc.get(obj);
    if (error) {
        std::cerr << "Error parsing JSON: " << error << std::endl;
        return 1;
    }

    for (auto [key, value] : obj) {
        if (key == "author") {
            std::cout << "Author: " << value.get_string() << std::endl;
        }
    }

    return 0;
}
