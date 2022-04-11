import datetime

class Gloss:
	def __init__(self, name, acronym=False, acronym_full="", definition="", institute="", internal=False, pronunciation="", seealso=None, updated=datetime.date.today()):
		self.name = name
		self.acronym = acronym
		self.acronym_full = acronym_full
		self.definition = definition
		self.institute = institute
		self.internal = internal
		self.pronunciation = pronunciation
		self.seealso = seealso
		self.updated = updated

WDL = Gloss("WDL", True, "Workflow Description Language")
Workflow_Description_Language = Gloss("Workflow Description Language", definition="A workflow language managed by the Open WDL Project.", seealso=WDL)

print(WDL)




# acronym (bool) - Is this an acronym?
# acronym_full (string) - if acronym, what is the full name
# institute (string) - optional, which institution is the phrase associated with, if any? For instance, Terra is associated with the Broad Institute. GCP is associated with Google. Does not necessarily imply a trademark or copyright.
# internal (bool) - Is this only used internally? For acronyms this may imply the acronym is internal but the phrase it refers to is not (ex: gha - github app)
# pronunciation (string) - optional pronunciation (ex: wdl - "widdle")
# updated (date) - when the entry was last updated