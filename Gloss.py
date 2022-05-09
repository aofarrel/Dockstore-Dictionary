import datetime

class GlossEntry:
	def __init__(self, name, acronym_full="", definition="", furtherreading="", institute="", pronunciation="", seealso="", updated=datetime.date.today()):
		# name - entry's name, make sure to use correct capitalization/lack thereof
		# acronym_full - if acronym, what is the full name. if blank, assumed to not be an acronym.
		# 	if acronym_full contains [brackets], then the acronym's explanation should link to another
		#	entry instead of having its own definition.
		# further_reading - URL to a webpage, usually an "official" one associated with the term
		# institute - optional, which institution is the phrase associated with, if any?
		#	for instance, Terra is associated with the Broad Institute. GCP is associated with Google.
		# pronunciation - optional pronunciation (ex: wdl - "widdle")
		# seealso - related but not equivalent entries, such as CLI being related to Dockstore CLI. 
		#	should not be included if the entry lacks a definition (ie has acronym_full linking to another entry.)
		# updated - when the entry was last updated
		self.name: str = name
		self.acronym_full: str = acronym_full
		self.definition: str = definition
		self.furtherreading: str = furtherreading
		self.institute: bool = institute
		self.pronunciation: str = pronunciation
		self.seealso: str = seealso
		self.updated: datetime = updated

	def return_name(self): # for TOC
		return self.name

	def text_entry_title(self):
		'''Return underlined title. Same in RST, Markdown, and plaintext.'''
		entry_title = []
		entry_title.append("\n\n")               # space between entries
		entry_title.append(f"{self.name}\n")     # name
		entry_title.append("-" * len(self.name)) # underline of name
		entry_title.append("\n")                 # another newline
		return "".join(entry_title)

	def text_pronunciation(self):
		return f"[pronounced {self.pronunciation}]\n"

	def text_acronym(self, format="txt"):
		'''Return acronym's full form, in italics if RST'''
		if format == "txt":
			return f"abbreviation for {self.acronym_full}\n"
		elif format == "rst":
			return f"*abbreviation for* {self.acronym_full}\n"

	def text_definition(self):
		return f"	{self.definition}\n"

	def text_institute(self):
		return f"This term as we define it here is associated with {self.institute} and may have different definitions in other contexts.\n"

	def text_seealso(self):
		return f"see also {self.seealso}\n"

	def text_furtherreading(self, format="txt"):
		if format == "txt":
			return f"Further reading: {self.furtherreading}\n"
		elif format == "rst":
			return f"Further reading: `<{self.furtherreading}>`_\n"

	def text_updated(self, format="txt"):
		'''Ideally, should print when entry was last updated visibly if plaintext, as a comment if RST.
		But the current implementation of entries.py gives all entries the same timestamp.'''
		if format == "txt":
			return self.updated.strftime("updated %Y-%m-%d\n")
		elif format == "rst":
			return self.updated.strftime(".. updated %Y-%m-%d")
	
	def generate_plaintext(self):
		'''Generate plaintext output of this entry'''
		plaintext = []
		plaintext.append(self.text_entry_title())
		if self.pronunciation != "":
			plaintext.append(self.text_pronunciation())
		if self.acronym_full != "":
			plaintext.append(self.text_acronym())
		if self.definition != "":
			plaintext.append(self.text_definition())
		if self.institute != "":
			plaintext.append(self.text_institute())
		if self.seealso != "":
			plaintext.append(self.text_seealso())
		if self.furtherreading != "":
			plaintext.append(self.text_furtherreading())
		plaintext.append(self.text_updated())
		return "".join(plaintext)

	def generate_RST(self):
		'''Generate RST output of this entry'''
		rst = []
		rst.append(self.text_entry_title())
		if self.pronunciation != "":
			rst.append(self.text_pronunciation())
		if self.acronym_full != "":
			rst.append(self.text_acronym(format="rst"))
		if self.definition != "":
			rst.append(self.text_definition())
		if self.institute != "":
			rst.append(self.text_institute())
		if self.seealso != "":
			rst.append(self.text_seealso())
		if self.furtherreading != "":
			rst.append(self.text_furtherreading(format="rst"))
		rst.append(self.text_updated(format="rst"))
		return "".join(rst)


