from entries import * 
import gc

outfile = "output.txt"

list_entries = []
for glossary_object in gc.get_objects():
    if isinstance(glossary_object, GlossEntry):
        list_entries.append(glossary_object)

list_entries.sort(key=lambda x: x.name.upper())

with open(outfile, "a") as f:
    # generate RST page title
    f.write("Dockstore Dictionary\n")
    f.write("====================\n")
    # generate main body text
    for entry in list_entries:
        f.write(entry.generate_plaintext())