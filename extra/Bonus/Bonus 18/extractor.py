import zipfile

def extractor(inputfile,extract_dir):
    with zipfile.ZipFile(inputfile, 'r') as file:
        file.extractall(extract_dir)


if __name__ == "__main__":
    extractor("/home/paul/Downloads/compressed.zip","/home/paul/PycharmProects/Pythonmegacourse/extra/Bonus/Bonus 18")