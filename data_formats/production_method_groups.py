from data_formats import DataFormat
import os


class ProductionMethodGroups(DataFormat):
    prefixes = ["building_"]
    relative_file_location = os.path.normpath("common/production_method_groups")
    data_links = {"ProductionMethods": "production_methods"}

    def __init__(self, game_folder: str, mod_folder: str, prefixes: list = None, link_data: list = None):
        if not prefixes:
            prefixes = ProductionMethodGroups.prefixes
        else:
            prefixes += ProductionMethodGroups.prefixes

        game_version = os.path.join(game_folder, ProductionMethodGroups.relative_file_location)
        mod_version = os.path.join(mod_folder, ProductionMethodGroups.relative_file_location)
        super().__init__(game_version, mod_version, prefixes=prefixes)
        self.interpret()

        if link_data:
            for external_data in link_data:
                self.link(ProductionMethodGroups.data_links[type(external_data).__name__], external_data)


if __name__ == '__main__':
    import os
    from constants import Test
    from data_formats import ProductionMethods

    production_methods = ProductionMethods(Test.game_directory, Test.mod_directory)
    production_method_groups = ProductionMethodGroups(Test.game_directory, Test.mod_directory, link_data=[production_methods])

    print("\n GAME FILES \n")
    for name, element in production_method_groups.items():
        if Test.game_directory in element["_source"]:
            print(name, element)

    print("\n MOD FILES \n")
    for name, element in production_method_groups.items():
        if Test.mod_directory in element["_source"]:
            print(name, element)

