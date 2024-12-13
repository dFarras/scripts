import click
import os
import aemet.constants.aemet_constants as constants
from aemet.configuration.components.configuration_folder_initializer import validate_paths

base_data_folder = constants.base_data_folder
configuration_file_path = os.path.join(constants.configuration_folder, constants.configuration_file)

@click.group()
def configuration():
    pass

@configuration.command()
@click.argument("base_folder", default="data", required=False)
def initialize(base_folder):
    validate_paths()
    with open(configuration_file_path, "w") as file:
        file.write(f"base_folder={base_folder}")

@configuration.command()
@click.argument("base_folder")
def set_base_folder(base_folder):
    validate_paths()
    if not os.path.exists(constants.configuration_folder):
        print("Found no configuration, please execute aemet cli initialization command first.")
    if not os.path.exists(configuration_file_path):
        with open(configuration_file_path, "w") as file:
            file.write(f"base_folder={base_folder}")
    else:
        os.remove(configuration_file_path)
        with open(configuration_file_path, "w") as file:
            file.write(f"base_folder={base_folder}")

@configuration.command()
def get():
    validate_paths()
    try:
        with open(configuration_file_path, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"{configuration_file_path} does not exist.")
    except PermissionError:
        print(f"Permission denied: {configuration_file_path}")