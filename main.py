from entries import * 
import gc

outfile  = "outputs/output.rst"
contents = "outputs/toc.txt"

# this feels dodgy, but it hasn't failed yet
list_entries = []
for glossary_object in gc.get_objects():
    if isinstance(glossary_object, GlossEntry):
        list_entries.append(glossary_object)

list_entries.sort(key=lambda x: x.name.upper())

with open(outfile, "a") as f:
    # generate RST page title
    f.write("Dockstore Dictionary\n")
    f.write("====================\n")
    # tell RST to make a local TOC
    f.write(".. contents:: Table of Contents\n\t:local:\n\n")
    f.write(".. hlist:: \n\t:columns: 3\n\n\t* A list of\n\t* short items\n\t* to display horizontally\n\n")
    # generate main body text
    for entry in list_entries:
        f.write(entry.generate_RST())

with open(contents, "a") as g:
    for entry in list_entries:
        g.write(f"{entry.return_name()}\n") 