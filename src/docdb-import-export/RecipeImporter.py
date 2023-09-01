from DocDbClient import DocDbClient
from DocDbJsonImporter import DocDbJsonImporter
import json

class RecipeImporter(DocDbJsonImporter):

  def __init__(self, source_json_file_path, db_name, collection_name):
    try:
      super().__init__(source_json_file_path, db_name, collection_name)
    except Exception as e:
      print("ERROR: Failed to initialize RecipeImporter: " + str(e))
      exit(1)

  def import_json(self):
    # self.docdb[self.db][self.collection].drop()
    try:
      # Read the recipes json data from the file.
      with open(self.source_json_file_path) as f:
        recipes = json.load(f)

      for id in recipes["food_info"]:
        # Transform the recipes json data into the format that can be imported
        # into DocumentDB.
        recipe = self.__transform_item(recipes["food_info"][id])
        # print(id, recipes["food_info"][id])
        # Insert the recipe into DocumentDB.
        self.docdb[self.db][self.collection].insert_one(recipe)
      print("Successfully imported json file: " + self.source_json_file_path)

    except Exception as e:
      print("ERROR: Failed to import json file: ", e)

  # This method transforms the recipes json data into the format that can be
  # imported into DocumentDB.
  def __transform_item(self, recipe):
      # Transform the recipes json data into the format that can be imported
      # into DocumentDB.
      return recipe
        # recipe["_id"] = recipe["id"]
        # del recipe["id"]
        # yield recipe


