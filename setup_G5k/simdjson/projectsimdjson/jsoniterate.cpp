#include "simdjson.h"
#include <iostream>

int main() {
    // Charger un fichier contenant plusieurs documents JSON
    const char* filename = "multiple_documents.json";
    simdjson::dom::parser parser;
    simdjson::padded_string json;

    try {
        json = simdjson::padded_string::load(filename);
    } catch (const std::exception& e) {
        std::cerr << "Error loading file: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    try {
        // Utiliser iterate_many pour traiter chaque document JSON indépendamment
        simdjson::dom::document_stream docs = parser.iterate_many(json);
        for (simdjson::dom::element doc : docs) {
            // Accéder aux données du document JSON
            std::string text = doc["text"];
            std::cout << "Text: " << text << std::endl;
        }
    } catch (const simdjson::simdjson_error& e) {
        std::cerr << "simdjson error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
