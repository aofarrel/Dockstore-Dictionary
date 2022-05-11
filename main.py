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
dockstore_dictionary = GreatGloss("Dockstore Dictionary")
for glossary_object in gc.get_objects():
    if isinstance(glossary_object, GlossEntry):
        dockstore_dictionary.add_entry(glossary_object)

dockstore_dictionary.sort_entries()

dockstore_dictionary.write_toc(contents)

with open(contents, "a") as f:
    for entry in list_entries:
        # not using text_rst_bookmark() to make this more human-readable
        # and so RST TOC doesn't have to process `.. _` and `:` bits
        # if bookmark format ever changes this may need be adjusted
        f.write(f"{entry.return_name()}\n") 

with open(outfile, "a") as g:
    # generate RST page title
    g.write("Dockstore Dictionary\n")
    g.write("====================\n")
    # tell RST to make a local TOC from toc.txt
    g.write(".. hlist:: \n\t:columns: 3\n\n")
    with open(contents, "r") as h:
        for line in h.readlines():
            g.write(f"\t* :ref:`dict {line[:-1]}`\n")
    g.write("\n") #needed to avoid RST getting mad
    # generate main body text
    for entry in list_entries:
        g.write(entry.generate_RST())