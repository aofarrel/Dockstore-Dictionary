import datetime

class Gloss:
	def __init__(self, name, acronym_full="", definition="", furtherreading="", institute="", internal=False, pronunciation="", seealso="", updated=datetime.date.today()):
		self.name = name
		self.acronym_full = acronym_full
		self.definition = definition
		self.furtherreading = furtherreading
		self.institute = institute
		self.internal = internal
		self.pronunciation = pronunciation
		self.seealso = seealso
		self.updated = updated

	def generate_plaintext(self):
		with open("gloss.txt", "a") as f:
			f.write("\n\n")
			# print name and prounciation
			if self.pronunciation is not "":
				f.write(f"{self.name}    (pronounced {self.pronunciation})\n")
			else:
				f.write(f"{self.name}\n")
			
			# generate underline (excludes pronunciation, which will be problematic in RST)
			for x in range(0,len(self.name)):
				f.write("-")
			f.write("\n")
			

			# print full form of acronym and see also
			# for an acronym, seealso will replace the full form of the acronym
			# maybe this means we don't need an acronym argument...
			# but I don't want to commit until I have a good few entries
			if self.acronym_full is not "" and self.seealso is not "":
				f.write(f"   see {self.seealso}\n")
			if self.acronym_full is not "" and self.seealso is "":
				f.write(f"   {self.acronym_full}\n")
			else:
				pass

			# currently seealso does not get printed if there is no acronym_full
			# this is by design... for now

			if self.definition is not "":
				f.write(f"{self.definition}\n")

			if self.institute is not "":
				f.write(f"This term as we define it here is associated with {self.institute} and may have different definitions in other contexts.\n")
			

			if self.furtherreading is not "":
				f.write(f"Further reading: {self.furtherreading}\n")

			f.write(self.updated.strftime("updated %Y-%m-%d\n"))



WDL = Gloss("WDL",
	acronym_full="Workflow Description Language",
	pronunciation='"widdle", rhymes with little',
	seealso="Workflow Description Language")
Workflow_Description_Language = Gloss("Workflow Description Language",
	furtherreading="https://openwdl.org/",
	definition="A workflow language managed by the Open WDL Project. Usually written as [WDL].",
	seealso="WDL")

WDL.generate_plaintext()
Workflow_Description_Language.generate_plaintext()


# name (string) - entry's name, make sure to use correct capitalization/lack thereof
# acronym_full (string) - if acronym, what is the full name. if blank, assumed to not be an acronym
# further_reading (string) - URL to a webpage, usually an "official" one associated with the term
# institute (string) - optional, which institution is the phrase associated with, if any? For instance, Terra is associated with the Broad Institute. GCP is associated with Google. Does not necessarily imply a trademark or copyright.
# internal (bool) - Is this only used internally? For acronyms this may imply the acronym is internal but the phrase it refers to is not (ex: gha - github app)
# pronunciation (string) - optional pronunciation (ex: wdl - "widdle")
# updated (date) - when the entry was last updated
