import os


class Mappavalto:
    def __init__(self, destination):
        self.destination = destination
        self.original = os.getcwd()

    def __enter__(self):
        os.chdir(os.path.abspath(self.destination))

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(os.path.abspath(self.original))


with Mappavalto("../"):
    pass

