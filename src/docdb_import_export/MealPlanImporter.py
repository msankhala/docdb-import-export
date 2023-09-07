import json
import os
import sys
from dotenv import load_dotenv
from docdb_import_export.docdb_client import DocDbClient
from docdb_import_export.docdb_json_importer import DocDbDefaultJsonImporter

load_dotenv()

class MealPlanImporter(DocDbDefaultJsonImporter):

  def __init__(self, source_json_file_path, db_name, collection_name, drop_collection):
    try:
      super().__init__(source_json_file_path, db_name, collection_name, drop_collection)
    except Exception as e:
      print("ERROR: Failed to initialize MealPlanImporter: " + str(e))
      exit(1)

  def import_dir_json(self):
    self.delete_collection()

    # Read the json files from the directory, the json files are under the
    # sub-directory of the given directory. Each sub-directory is named after
    # the user id. Inside each sub-directory, there is json file with name
    # meal_plans.json.
    items = []
    for subdir, dirs, files in os.walk(self.source_json_file_path):
      for file in files:
        if file == "meal_plans.json":
          meal_plans_file_path = os.path.join(subdir, file)
          with open(meal_plans_file_path) as f:
            mealplans = json.load(f)
            # Get the user id from the sub-directory name.
            user = {}
            user["_id"] = os.path.basename(subdir)
            user["meal_plans"] = self.transform_item(mealplans)
            items.append(user)

    # Insert the recipe into DocumentDB.
    self.docdb[self.db][self.collection].insert_many(items)
    print("Successfully imported json file: " + self.source_json_file_path)

  # This method transforms the mealplans json data into the format that can be
  # imported into DocumentDB.
  def transform_item(self, mealplans):
    return mealplans
