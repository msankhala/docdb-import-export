import json
import os
from abc import ABC, abstractmethod
from docdb_import_export.docdb_client import DocDbClient

# Abstract class for importing json data into DocumentDB database. This class
# should be extended by all the classes that import json data into DocumentDB.
class DocDbJsonImporterAbstract(ABC):

  def __init__(self, source_json_file_path, db_name, collection_name):
    # Check if the source json file path is valid file.
    if not source_json_file_path or not os.path.isfile(source_json_file_path):
      raise Exception("Invalid source json file path: " + source_json_file_path)

    # Initialize instance variables.
    self.docdb = DocDbClient().get_instance("docdb", True)
    self.source_json_file_path = source_json_file_path
    self.db =  db_name
    self.collection = collection_name

  # This method should be implemented by the classes that extend this class.
  @abstractmethod
  def import_json(self):
    pass

  @abstractmethod
  def import_dir_json(self):
    pass

  @abstractmethod
  def transform_item(self, item):
    pass

  # Set the given collection name as the current collection.
  def set_collection(self, collection_name):
    self.collection = collection_name

  # Set the given database name as the current database.
  def set_db(self, db_name):
    self.db = db_name

# Class for importing json data into DocumentDB database.
class DocDbJsonImporter(DocDbJsonImporterAbstract):

  def __init__(self, source_json_file_path, db_name, collection_name):
    try:
      super().__init__(source_json_file_path, db_name, collection_name)
    except Exception as e:
      print("ERROR: Failed to initialize RecipeImporter: " + str(e))
      exit(1)

  def import_json(self):
    # self.docdb[self.db][self.collection].drop()
    try:
      # Read the json data from the file assuming it is a array of json objects.
      with open(self.source_json_file_path) as f:
        items = json.load(f)

      for item in items:
        # Transform the recipes json data into the format that can be imported
        # into DocumentDB.
        item = self.transform_item(item)
        # Insert the recipe into DocumentDB.
        self.docdb[self.db][self.collection].insert_one(item)
      print("Successfully imported json file: " + self.source_json_file_path)

    except Exception as e:
      print("ERROR: Failed to import json file: ", e)

  def import_dir_json(self):
    # self.docdb[self.db][self.collection].drop()
    try:
      # Read the json files from the directory assuming each file is a array of
      # json objects.
      for file in os.listdir(self.source_json_file_path):
        if file.endswith(".json"):
          with open(os.path.join(self.source_json_file_path, file)) as f:
            items = json.load(f)
            for item in items:
              # Transform the json data into the format that can be imported
              # into DocumentDB.
              item = self.transform_item(item)
              # Insert the json data into DocumentDB.
              self.docdb[self.db][self.collection].insert_one(item)
          print("Successfully imported json file: " + file)
      print("Successfully imported json files in the directory: " + self.source_json_file_path)

    except Exception as e:
      print("ERROR: Failed to import json file: ", e)

  # This method transforms the item into the format that can be imported into
  # DocumentDB.
  def transform_item(self, item):
      return item
        # recipe["_id"] = recipe["id"]
        # del recipe["id"]
        # yield recipe


