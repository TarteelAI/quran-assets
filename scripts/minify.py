# This script pulls data from the QDC api to generate standardized data files
# for each page of the Quran


import io
import json
import os
import requests

file_path = '../audio/alafasy-ayah-manifest.json'

def main():
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, file_path), "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    with io.open(os.path.join(dirname, file_path), 'w', encoding='utf8') as json_file:
        formatted_data = json.dumps(data, ensure_ascii=False)
        json_file.write(formatted_data)


if __name__ == "__main__":
    main()
