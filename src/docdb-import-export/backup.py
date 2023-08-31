# This function will read the given json file and import it into the given
# document db. The json file is expected to be a list of json objects.The json
# object is in the format as given below.
#
# {
#  "food_info": {
#     "252774347": {
#       ... detail of the recipe
#     },
#     "252774348": {
#       ... detail of the recipe
#     }
#   },
#  "search_index": {
#    "search_term_id": [
#     ],
#    "food_id": [
#     ]
#   }
def docdb_import_recipes_from_json_file_to_recipe_collection(json_file_path, docdb_instance, docdb_database_name, docdb_collection_name):





# This function that will read the json files from a give directory path
# recursively and import them into a given document db. The directory structure
# is as give below.
#
# JSON_DATA_DIR
#  - <userid>
#    - meal_plans.json
#    - history.json
#    - favourites.json
