# %%
"""Voorbeeld project mappenstructuur. Dit kan centraal op 1 plek gedefineerd worden
waarna het in alle scripts is te importeren.
"""

import os

import hhnk_research_tools as hrt


class Project(hrt.Folder):
    def __init__(self, base):
        super().__init__(base, create=False)

        self.input = inputDir(self.base, "input")  # Vullingsgraad\Input
        self.output = outputDir(self.base, "output")  # Vullingsgraad\Input


class inputDir(hrt.Folder):
    """Input directory"""

    def __init__(self, base, name):
        super().__init__(os.path.join(base, name))

        self.add_file("dem", "dem.tif")
        self.add_file("panden", "panden.gpkg")


class outputDir(hrt.Folder):
    """Input directory"""

    def __init__(self, base, name):
        super().__init__(os.path.join(base, name))

        self.add_file("interactive_map", "interactive_map.html")
