# chinese-wordlist-extractor

Script to make word frequency list (CSV) from a text.

The script reads **input.txt** and writes **output.csv** with the following columns: **chinese word, frequency, pinyin, definition.**

You can use this frequency list to study the most common words from a text to be able to understand it more easily.

## Requirements

```
pip install tqdm
```

## Tips
  * if the imput has garbage (HTML, other language texts) it doesn't matter
  * just mirror your favorite (wanna to understand website) then concatenate all the html files to an input.txt then you can learn the frequent words for that particular website
  * run it on your book to read, or on the SRT of your movie

## Credits

This script uses the CC-CEDICT dictionary from https://cc-cedict.org/wiki/ that is licensed under the Creative Commons Attribution-Share Alike 3.0 License.
