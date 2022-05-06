from entries import * 
import gc

list_entries = []
for glossary_object in gc.get_objects():
    if isinstance(glossary_object, GlossEntry):
        list_entries.append(glossary_object)

list_entries.sort(key=lambda x: x.name.upper())

for entry in list_entries:
    entry.generate_plaintext()