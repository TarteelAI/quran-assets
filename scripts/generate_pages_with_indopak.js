import { readFile, writeFile } from "fs/promises";
const NUMBER_OF_PAGES = 604;

try {
  for (let pageNumber = 1; pageNumber <= NUMBER_OF_PAGES; pageNumber++) {
    const uthmaniPage = JSON.parse(
      await readFile(`./pages/${pageNumber}.json`, "utf8")
    );

    for (let uthmaniSurah of uthmaniPage.surahs) {
      if (!uthmaniSurah.surahNum) continue;
      const indopakSurah = JSON.parse(
        await readFile(
          `./indopak-word-by-word/${uthmaniSurah.surahNum}.json`,
          "utf8"
        )
      );
      for (let uthmaniAyah of uthmaniSurah.ayahs) {
        const ayahNum = uthmaniAyah.ayahNum;
        for (let [i, uthmaniWord] of uthmaniAyah.words.entries()) {
          uthmaniWord["indopak"] = indopakSurah[ayahNum].words[i];
        }
      }
    }
    await writeFile(
      `./pages/${pageNumber}.json`,
      JSON.stringify(uthmaniPage, null, 2),
      "utf8"
    );
  }
} catch (error) {
  console.log(
    "🚀 ~ file: generate_pages_with_indopak.js ~ line 26 ~ error",
    error
  );
}
