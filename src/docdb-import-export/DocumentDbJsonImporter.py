import os
from abc import ABC, abstractmethod
from DocumentDbClient import DocumentDbClient

# Abstract class for importing json data into DocumentDB database. This class
# should be extended by all the classes that import json data into DocumentDB.
class DocumentDbJsonImporter(ABC):

  def __init__(self, source_json_file_path, db_name, collection_name):
    # Check if the source json file path is valid file.
    if not source_json_file_path or not os.path.isfile(source_json_file_path):
      raise Exception("Invalid source json file path: " + source_json_file_path)

    # Initialize instance variables.
    self.docdb = DocumentDbClient().get_instance("docdb", True)
    self.source_json_file_path = source_json_file_path
    self.db =  db_name
    self.collection = collection_name

  # This method should be implemented by the classes that extend this class.
  @abstractmethod
  def import_json(self):
    pass

  # @abstractmethod
  # def import_dir_json(self):
  #   pass

  # Set the given collection name as the current collection.
  def set_collection(self, collection_name):
    self.collection = collection_name

  # Set the given database name as the current database.
  def set_db(self, db_name):
    self.db = db_name

