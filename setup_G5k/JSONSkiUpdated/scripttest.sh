#include "src/lib/RecordLoader.h"
#include "src/lib/QueryProcessor.h"
#include <iostream>

int main() {
    const char* file_path = "../dataset/twitter_sample_large_record.json";
    Record* rec = RecordLoader::loadSingleRecord(file_path);
    if (rec == nullptr) {
        std::cout << "Échec du chargement du fichier." << std::endl;
        return -1;
    }

    // Recherche du champ 'author'
    QueryProcessor authorProcessor("$[*].user.screen_name");
    std::string authorOutput = authorProcessor.runQuery(rec);
    std::cout << "Auteur : " << authorOutput << std::endl;

    // La commande g++ n'est pas exécutée ici car cela n'a pas de sens dans ce contexte
    // Si vous voulez exécuter une commande g++, vous devrez implémenter cette fonctionnalité dans QueryProcessor.

    return 0;
}
