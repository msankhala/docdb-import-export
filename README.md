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
    python -m docdb_import_export import \
    --fromjson=../my-data-folder/my.json \
    --db=test --collection=temp \
    --drop
    ```

1. Import data from a json file to document db using custom importer class

    ```sh
    python -m docdb_import_export import \
    --fromjson=../my-data-folder/my.json \
    --db=test --collection=temp \
    --import-class=some-dir/MyCustomImporter.py \
    --drop
    ```

    The importer class filename and classname should be same and importer class should be a subclass of `DocDbDefaultJsonImporter` class and should implement all abstract methods.

1. Import data from a directory to document db

    ```sh
    python -m docdb_import_export import \
    --fromjsondir=../my-data-folder/ \
    --db=test \
    --collection=temp \
    --drop
    ```

1. Import data from a directory to document db using custom importer class

    ```sh
    python -m docdb_import_export import \
    --fromjsondir=../my-data-folder/ \
    --db=test --collection=temp \
    --import-class=some-dir/MyCustomImporter.py \
    --drop
    ```

    The importer class filename and classname should be same and importer class should be a subclass of `DocDbDefaultJsonImporter` class and should implement all abstract methods.

## Providing your own custom importer class

**src/some-path/MyCustomImporter.py**

```python
import json
from dotenv import load_dotenv
from docdb_import_export.docdb_client import DocDbClient
from docdb_import_export.docdb_json_importer import DocDbDefaultJsonImporter

load_dotenv()

class MyCustomImporter(DocDbDefaultJsonImporter):

  def __init__(self, source_json_file_path, db_name, collection_name, drop_collection):
    try:
      super().__init__(source_json_file_path, db_name, collection_name, drop_collection)
    except Exception as e:
      print("ERROR: Failed to initialize RecipeImporter: " + str(e))
      exit(1)

  def import_json(self):
    try:
      # Only add if you want to add support for --drop option.
      self.delete_collection()

      # Read the json data from the file.
      with open(self.source_json_file_path) as f:
        json_list = json.load(f)

      items = []
      for index in json_list:
        # Transform the json data into the format that can be imported
        # into DocumentDB.
        items.append(self.transform_item(json_list[index]))
      # Insert the recipe into DocumentDB.
      self.docdb[self.db][self.collection].insert_many(items)
      print("Successfully imported json file: " + self.source_json_file_path)

    except Exception as e:
      print("ERROR: Failed to import json file: ", e)

  # This method allows you to transform the json data so that you can add or
  # remove the fields from the json data.
  def transform_item(self, recipe):
    recipe["_id"] = recipe["id"]
    del recipe["id"]
    # Add more transformations here if you want to.
    return recipe
```
