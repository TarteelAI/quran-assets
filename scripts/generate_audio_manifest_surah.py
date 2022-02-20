# This script pulls data from the QDC api to generate standardized data files
# for each page of the Quran


import io
import json
import os
import requests

BASE_API_URL = "https://staging.quran.com/api/qdc/audio/reciters/7/audio_files?segments=true"


def main():
    dirname = os.path.dirname(__file__)
    source_data = requests.get(BASE_API_URL).json()
    manifest = []

    for surah in source_data["audio_files"]:
        verse_timings = []
        for verse in surah["verse_timings"]:
            segments = []
            for s in verse["segments"]:
                try:
                    segments.append([s[0], s[1], s[2]])
                except:
                    print(verse["verse_key"], s)
            verse_timings.append(segments)
        manifest.append({
            "duration": surah["duration"],
            "fileSize": surah["file_size"],
            "verseTimings": verse_timings,
        })


    with io.open(os.path.join(dirname, '../audio/mishari-manifest.json'), 'w', encoding='utf8') as json_file:
        data = json.dumps(manifest, ensure_ascii=False)
        json_file.write(data)


if __name__ == "__main__":
    main()
