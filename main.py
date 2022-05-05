from entries import * 
import gc

for glossary_object in gc.get_objects():
    if isinstance(glossary_object, GlossEntry):
        glossary_object.generate_plaintext()