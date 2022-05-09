from entries import * 
import gc

list_entries = []
for glossary_object in gc.get_objects():
    if isinstance(glossary_object, GlossEntry):
        list_entries.append(glossary_object)

list_entries.sort(key=lambda x: x.name.upper())

# generate RST page title
print("Dockstore Dictionary")
print("====================")

# generate TOC
for entry in list_entries:
    print(entry.return_name())

# generate main body text
for entry in list_entries:
    entry.generate_plaintext()