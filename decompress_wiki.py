import bz2
import shutil

# Decompress the file
with bz2.BZ2File('wikidatawiki-20240720-pages-articles-multistream.xml.bz2') as file, open('wikidata.xml', 'wb') as decompressed:
    shutil.copyfileobj(file, decompressed)