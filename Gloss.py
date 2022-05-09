import datetime

class GlossEntry:
	def __init__(self, name, acronym_full="", definition="", furtherreading="", institute="", internal=False, pronunciation="", seealso="", updated=datetime.date.today()):
		# name - entry's name, make sure to use correct capitalization/lack thereof
		# acronym_full - if acronym, what is the full name. if blank, assumed to not be an acronym
		# further_reading - URL to a webpage, usually an "official" one associated with the term
		# institute - optional, which institution is the phrase associated with, if any? For instance, Terra is associated with the Broad Institute. GCP is associated with Google. Does not necessarily imply a trademark or copyright.
		# internal- Is this only used internally? For acronyms this may imply the acronym is internal but the phrase it refers to is not(ex: gha - github app)
		# pronunciation - optional pronunciation (ex: wdl - "widdle")
		# updated - when the entry was last updated
		self.name: str = name
		self.acronym_full: str = acronym_full
		self.definition: str = definition
		self.furtherreading: str = furtherreading
		self.institute: bool = institute
		self.internal: str = internal
		self.pronunciation: str = pronunciation
		self.seealso: str = seealso
		self.updated: datetime = updated

	def return_name(self): # for TOC
		return self.name

	def text_entry_title(self):
		entry_title = []
		entry_title.append("\n\n")               # space between entries
		entry_title.append(f"{self.name}\n")     # name
		entry_title.append("-" * len(self.name)) # underline of name
		entry_title.append("\n")                 # another newline
		return "".join(entry_title)

	def text_pronunciation(self):
		return f"[pronounced {self.pronunciation}]\n"

	def text_acronymseealso(self):
		if self.acronym_full != "" and self.seealso != "":
			return(f"see {self.seealso}\n")
		elif self.acronym_full != "" and self.seealso == "":
			return(f"abbreviation for {self.acronym_full}\n")
		elif self.acronym_full == "" and self.seealso != "":
			return(f"see {self.seealso}\n")
		else:
			pass # should never happen
	
	def generate_plaintext(self):
		with open("output.txt", "a") as f:
			f.write(self.text_entry_title())

			# print pronunciation
			if self.pronunciation != "":
				f.write(self.text_pronunciation())

			# print full form of acronym or see also
			# for an acronym, seealso will replace the full form of the acronym
			# this section could probably be written cleaner
			if self.acronym_full != "" or self.seealso != "":
				f.write(self.text_acronymseealso())

			if self.definition != "":
				f.write(f"	{self.definition}\n")

			if self.institute != "":
				f.write(f"This term as we define it here is associated with {self.institute} and may have different definitions in other contexts.\n")
			

			if self.furtherreading != "":
				f.write(f"Further reading: {self.furtherreading}\n")

			f.write(self.updated.strftime("updated %Y-%m-%d\n"))


