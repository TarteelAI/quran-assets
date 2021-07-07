import argparse
import csv
import io
import json
import logging
from pathlib import Path

import requests
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class QuranEncTranslationScraper(Spider):
    name = 'quranenc-translation-scraper'
    start_urls = ['https://quranenc.com/en/home/']
    download_urls = [r"(?:^|\W)download\/csv(?:$|\W)"]

    def _process_response(self, response):
        fd = io.StringIO(response.text)
        reader = list(csv.reader(fd, delimiter=','))
        if len(reader) < 1:
            print(f"Unable to process {response.url}")
            return
        # row: ['id', 'sura', 'aya', 'translation', 'footnotes']
        filename = f"{response.url.split('/')[-1]}.json"
        json_data = []
        curr_surah = 1
        curr_ayahs = []
        # Skip the first two rows since it includes info and header
        for row in reader[2:]:
            # New surah
            if curr_surah < int(row[1]):
                json_data.append(curr_ayahs)
                curr_surah = int(row[1])
                curr_ayahs = []
            curr_ayahs.append(row[3])
        json_data.append(curr_ayahs)

        json_path = Path(self.settings.get('output')).absolute() / filename
        with open(json_path, "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False)

    def parse(self, response, **kwargs):
        for link in LinkExtractor(allow=self.download_urls).extract_links(response):
            response = requests.get(link.url)
            self._process_response(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape QuranEnc Translations.')
    parser.add_argument(
        '-o', '--output', type=str, default="./translations/quranenc", help='Output directory for JSON files.'
    )
    args = parser.parse_args()

    process = CrawlerProcess(settings={
        'output': args.output
    })
    process.crawl(QuranEncTranslationScraper)
    process.start()
