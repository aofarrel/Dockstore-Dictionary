# Dockstore Dictionary
 An unofficial dictionary/glossary for Dockstore. Uses Python to generate a formatted dictionary, to the extent plaintext can be considered formatted. *The content of these entries have not gone through formal review yet and there may be inaccuracies/missing content at this time.*

## Usage
 Add entries to entries.py using template in entry_template.py, making sure to keep them in alphabetical order. To generate the actual glossary, run `python3 main.py` to generate RST output as output.txt

 The "definition" argument in GlossEntry can reference other entries. To do so, encapsulate the entry title you which to reference with brackets, such as "[WDL]", which will become a working internal link when outputting to RST.

## Future Plans
 Fix bugs