"""JSON DocumentDb Importer.

Usage:
  main.py import --fromjson=<path-to-file.json> --db=<db> --collection=<collection>
  main.py import --fromjsondir=<path-to-dir> --db=<db> --collection=<collection>
  main.py (-h | --help)
  main.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --fromjson=<path-to-file.json>  Path to the json file to import.
  --fromjsondir=<path-to-dir>  Path to dir of json files to import. It will only
  import files with .json extension and only one level deep. If this option is
  specified, --fromjson option will be ignored.

"""

from RecipeImporter import RecipeImporter
from docopt import docopt
import utils

def recipeImportFromJson(arguments):
  prompt = f'This will import the provided json file to the "{arguments["--db"]}" database and "{arguments["--collection"]}" collection. Are you sure you want to continue? [y/N]: '
  if utils.confirm(prompt):
    print("Importing json file: " + arguments["--fromjson"])
    recipe_importer = RecipeImporter(arguments["--fromjson"], arguments["--db"], arguments["--collection"])
    recipe_importer.import_json()

def recipeImportFromJsonDir(arguments):
  prompt = f'This will import all the json files in the directory to the "{arguments["--db"]}" database and "{arguments["--collection"]}" collection. Are you sure you want to continue? [y/N]: '
  if utils.confirm(prompt):
    print("Importing json files in the directory: " + arguments["--fromjsondir"])
    recipe_importer = RecipeImporter(arguments["--fromjsondir"], arguments["--db"], arguments["--collection"])
    recipe_importer.import_dir_json()

if __name__ == "__main__":
  # Import recipes json data into DocumentDB.
  arguments = docopt(__doc__, version='JSON DocumentDb Importer 2.0')
  if arguments["import"] and arguments["--fromjson"]:
    recipeImportFromJson(arguments)
  elif arguments["import"] and arguments["--fromjsondir"]:
    recipeImportFromJsonDir(arguments)
