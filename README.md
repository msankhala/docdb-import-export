# Document DB import export

A simple utility package to import json files to document db and export data from document db collections.

https://github.com/msankhala/docdb-import-export

## Roadmap

1. - [x] Provider importer script to import data from json files to document db.
1. - [x] Provider a simple python api to extend the functionality of the package.
1. - [ ] Provider exporter script to export data from document db collections to json files.
1. - [ ] Provider exporter script to export all data from document db collections to json files in a given directory.

## Uses

1. Import data from a json file to document db

    ```sh
    python -m docdb_import_export import --fromjson=../my-data-folder/my.json --db=test --collection=temp --drop
    ```

1. Import data from a json file to document db using custom importer class

    ```sh
    python -m docdb_import_export import --fromjson=../my-data-folder/my.json --db=test --collection=temp --import-class=some-dir/MyCustomImporter.py --drop
    ```

    The importer class filename and classname should be same and importer class should be a subclass of `DocDbDefaultJsonImporter` class and should implement all abstract methods.

1. Import data from a directory to document db

    ```sh
    python -m docdb_import_export import --fromjsondir=../my-data-folder/ --db=test --collection=temp --drop
    ```

1. Import data from a directory to document db using custom importer class

    ```sh
    python -m docdb_import_export import --fromjsondir=../my-data-folder/ --db=test --collection=temp --import-class=some-dir/MyCustomImporter.py --drop
    ```

    The importer class filename and classname should be same and importer class should be a subclass of `DocDbDefaultJsonImporter` class and should implement all abstract methods.
