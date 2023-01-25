import zipfile
import pathlib


def make_archive(filepath, destination):
    destination = pathlib.Path(destination, "compressed.zip")
    with zipfile.ZipFile(destination, "w") as archive:
        for file in filepath:
            file = pathlib.path(file)
            archive.write(file, arcname="file.name")
