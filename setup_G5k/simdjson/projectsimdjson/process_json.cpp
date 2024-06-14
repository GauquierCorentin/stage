#include "simdjson.h"
#include <iostream>

using namespace simdjson;
using namespace std;

// Range adapter for document_stream
class DocumentStreamRange {
public:
    explicit DocumentStreamRange(simdjson::ondemand::document_stream stream) : stream(stream) {}

    auto begin() const { return stream.begin(); }
    auto end() const { return stream.end(); }

private:
    simdjson::ondemand::document_stream stream;
};

// Helper function to create the range adapter
inline DocumentStreamRange to_range(simdjson::ondemand::document_stream stream) {
    return DocumentStreamRange(std::move(stream));
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <path to large JSON file>" << endl;
        return EXIT_FAILURE;
    }

    const char *filename = argv[1];

    simdjson::ondemand::parser parser;

    // Load the entire file into a padded_string
    simdjson::padded_string json;
    auto error = simdjson::padded_string::load(filename).get(json);
    if (error) {
        cerr << "Error loading JSON file: " << error_message(error) << endl;
        return EXIT_FAILURE;
    }

    // Iterate over JSON documents in the file using iterate_many
    auto stream = parser.iterate_many(json);
    for (auto result : to_range(stream)) {
        if (result.error()) {
            cerr << "Error parsing JSON document: " << error_message(result.error()) << endl;
            continue;
        }
        auto doc = result.value();
        try {
            std::string_view name = doc["name"];
            cout << "Name: " << name << endl;
        } catch (const simdjson::simdjson_error &e) {
            cerr << "Error extracting field: " << e.what() << endl;
        }
    }

    return EXIT_SUCCESS;
}
