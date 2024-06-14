#include "../src/lib/RecordLoader.h"
#include "../src/lib/QueryProcessor.h"
#include <iostream>

using namespace std;

int main() {
    char* file_path = "../../../crossref/crossref16.json";

    Record* rec = RecordLoader::loadSingleRecord(file_path);
    if (rec == NULL) {
        cout << "Échec du chargement du fichier." << endl;
        return -1;
    }

    QueryProcessor processor("$.items[*].URL");
    string output = processor.runQuery(rec);
    cout << "Author : " << output << endl;

    return 0;
}
