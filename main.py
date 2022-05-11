from entries import * 
from Gloss import *
import gc

## debug ##
import os
outfile  = "outputs/output.rst"
contents = "outputs/toc.txt"
try:
    os.remove(outfile)
    os.remove(contents)
except FileNotFoundError:
    pass


# this feels dodgy, but it hasn't failed yet
# todo: read entries.py instead of importing it (maybe)
dockstore_dictionary = GreatGloss("Dockstore Dictionary")
for glossary_object in gc.get_objects():
    if isinstance(glossary_object, GlossEntry):
        dockstore_dictionary.add_entry(glossary_object)

dockstore_dictionary.sort_entries()
dockstore_dictionary.write_toc(contents)
dockstore_dictionary.write_glossary(outfile)