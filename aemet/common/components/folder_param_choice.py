import os
import click

class FolderParamChoice(click.ParamType):
    name = "folder_choice"

    def __init__(self, base_folder):
        self.base_folder = base_folder

    def shell_complete(self, ctx, param, incomplete):
        if not os.path.exists(self.base_folder):
            return []

        folders = [f for f in os.listdir(self.base_folder) if os.path.isdir(os.path.join(self.base_folder, f))]

        return [click.shell_completion.CompletionItem(f) for f in folders if f.startswith(incomplete)]

    def convert(self, value, param, ctx):
        full_path = os.path.join(self.base_folder, value)
        if os.path.isdir(full_path):
            return value
        self.fail(f"'{value}' is not a valid folder in '{self.base_folder}'", param, ctx)