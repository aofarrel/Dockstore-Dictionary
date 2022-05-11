# Dockstore Dictionary
 An unofficial dictionary/glossary for Dockstore. Uses Python to generate a formatted dictionary, to the extent plaintext can be considered formatted. *The content of these entries have not gone through formal review yet and there may be inaccuracies/missing content at this time.*

## Usage
 Add entries to entries.py using template in entry_template.py, making sure to keep them in alphabetical order. To generate the actual glossary, run `python3 main.py` to generate RST output as output.txt

 The "definition" argument in GlossEntry can reference other entries. To do so, encapsulate the entry title you which to reference with brackets, such as "[WDL]", which will become a working internal link when outputting to RST. Do not put any alphanumeric characters immediately before or after either bracket.

 Upon committing, `outputs/output.rst` and `output/toc.txt` will be updated; see `hooks/pre-commit`

## Style Guide
 * Every GlossEntry object variable name should be capitalized, and may be referred to with shorthand, such as:
    * GCP
    * AnVIL
    * Elwazi
    * SpotInstance
    * Container
 * The actual name of each term should follow the official capitalization for the word they represent, such as:
    * GCP <-- acronym that Google writes as capitalized
    * AnVIL Project <-- entire thing is a proper noun, first word is an acronym officially written in this manner
    * eLwazi <-- officially written in this manner; follows non-English capitalization rules
    * Spot Instance <-- trademark that Amazon writes as capitalized
    * container <-- not a proper noun nor a trademark, so not capitalized
* If acronym_full contains [brackets], then the acronym's explanation should link to another entry instead of having its own definition.
* seealso should not be included if the entry lacks a definition (ie has acronym_full linking to another entry.)

## Future Plans
 Make a superobject for GlossEntry