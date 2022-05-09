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

	def return_name(self, nospaces=False):
		'''Can be used to generate an RST bookmark, or, if entry is in a list, a quick way to make rudimentary TOC'''
		if nospaces==False:
			return self.name
		else:
			processed_characters = []
			for character in self.return_name(nospaces=False):
				if character==" ":
					character = "-"
				processed_characters.append(character)
			return "".join(processed_characters)

	def text_rst_bookmark(self):
		'''Generates an RST bookmark for the entry'''
		return f".. _dict {self.return_name(nospaces=False)}:"

	def text_entry_title(self):
		'''Return underlined title. Same in RST, Markdown, and plaintext.'''
		entry_title = []
		entry_title.append("\n\n")               # space between entries
		entry_title.append(f"{self.name}\n")     # name
		entry_title.append("-" * len(self.name)) # underline of name
		entry_title.append("\n")                 # another newline
		return "".join(entry_title)

	def text_pronunciation(self, format="txt"):
		if format == "txt":
			return f"[pronounced {self.pronunciation}]\n"
		elif format == "rst":
			return f"pronounced {self.pronunciation}  \n\n"

	def text_acronym(self, format="txt"):
		'''Return acronym's full form, in italics if RST. We need an extra newline in RST to stop the acronym from being considered the header title of the definition.'''
		if format == "txt":
			return f"abbreviation for {self.acronym_full}\n"
		elif format == "rst":
			return f"*abbreviation for* {self.acronym_full}  \n\n"

	def text_definition(self, format="txt"):
		'''If RST, we need to make the [references to other entries] into internal links.
		Limitations: Brackets followed by punctuation besides , or . currently not supported.'''
		if format == "txt":
			return f"	{self.definition}\n"
		elif format == "rst":
			words = self.definition.split()
			words_processed = []
			for word in words:
				if word.startswith("["):
					word = word[1:]  # strip [

					# This is where things get icky. The sentence "WDL is sometimes compared to [CWL]." will
					# split into ["[WDL]", "is", "sometimes", "compared", "to", "[CWL]."]
					# "[WDL]" could be handled by word = word[1:-1], but "[CWL]." would just strip the period.
					# So we have to do this instead (or rstrip, but this is a little clearer)
					word = word.replace("]", "")

					# But "[CWL]." is now "CWL." which will not match the "dict CWL" RST bookmark,
					# so we have to account for commas and periods. Instead of just deleting them,
					# we shove them after the :ref: in order to keep the definition's punctuation.
					if word.endswith(","):
						word = word[:-1]
						word = f":ref:`dict {word}`,"
					elif word.endswith("."):
						word = word[:-1]
						word = f":ref:`dict {word}`."
					else:
						word = f":ref:`dict {word}`"
					words_processed.append(word)
				else:
					words_processed.append(word)
			final = " ".join(words_processed)
			return f"	{final}  \n\n"

	def text_institute(self, format="txt"):
		if format == "txt":
			return f"This term as we define it here is associated with {self.institute} and may have different definitions in other contexts.\n"
		elif format == "rst":
			return f"This term as we define it here is associated with {self.institute} and may have different definitions in other contexts.  \n"
		
	def text_seealso(self, format="txt"):
		'''There is a supposedly simplier way to do this with sphinx.ext.autosectionlabel, via:
			see also :ref:`{self.seealso}`
		...but that would require we reformat piles of documentation (175 errors!)'''
		if format == "txt":
			return f"see also {self.seealso}\n"
		elif format == "rst":
			return f"see also :ref:`dict {self.seealso}`  \n"

	def text_furtherreading(self, format="txt"):
		'''If there is a see also, we need an extra newline. If not, avoid the extra newline.'''
		if format == "txt":
			return f"Further reading: {self.furtherreading}\n"
		elif format == "rst" and self.seealso == "":
			return f"Further reading: `<{self.furtherreading}>`_  \n"
		elif format == "rst" and self.seealso != "":
			return f"Further reading: `<{self.furtherreading}>`_  \n"

	def text_updated(self, format="txt"):
		'''Ideally, should print when entry was last updated visibly if plaintext, as a comment if RST.
		But the current implementation of entries.py gives all entries the same timestamp.'''
		if format == "txt":
			return self.updated.strftime("updated %Y-%m-%d\n")
		elif format == "rst":
			return self.updated.strftime("\n.. updated %Y-%m-%d  \n\n\n\n")
	
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
		rst.append(self.text_rst_bookmark())
		rst.append(self.text_entry_title())
		if self.pronunciation != "":
			rst.append(self.text_pronunciation(format="rst"))
		if self.acronym_full != "":
			rst.append(self.text_acronym(format="rst"))
		if self.definition != "":
			rst.append(self.text_definition(format="rst"))
		if self.institute != "":
			rst.append(self.text_institute(format="rst"))
		if self.seealso != "":
			rst.append(self.text_seealso(format="rst"))
		if self.furtherreading != "":
			rst.append(self.text_furtherreading(format="rst"))
		rst.append(self.text_updated(format="rst"))
		return "".join(rst)


