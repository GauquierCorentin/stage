#include "src/lib/RecordLoader.h"
#include "src/lib/QueryProcessor.h"

int main() {
    char* file_path = "../../crossref/crossref1.json";
    Record* rec = RecordLoader::loadSingleRecord(file_path);
    if (rec == NULL) {
        cout<<"record loading fails."<<endl;
        return -1;
    }

    // Recherche du champ 'author'
    QueryProcessor authorProcessor("$[*].user.screen_name");
    string authorOutput = authorProcessor.runQuery(rec);
    cout<<"Author: "<<authorOutput<<endl;

    // Compilation de la commande g++
    QueryProcessor gppProcessor("g++");
    string gppOutput = gppProcessor.runCommand();
    cout<<"g++ command output: "<<gppOutput<<endl;

    return 0;

}
