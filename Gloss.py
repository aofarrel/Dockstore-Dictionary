import datetime
import re

# Questions about best practices
#
# I want the user to be able to initalize objects without specifying all possible variables. Is it
# more correct to initalize the variables as None and later check if they are None, or to initalize
# them as empty strings (all are str type) and later check if they == ""?

class GlossEntry:
	'''Object for an individual glossary entry'''
	def __init__(self, name, acronym_full="", definition="", furtherreading="", institute="", pronunciation="", seealso="", updated=datetime.date.today()):
		'''
		name - entry's name
		acronym_full - if acronym, what is the full name. if blank, assumed to not be an acronym.
		further_reading - URL to a webpage, usually an "official" one associated with the term
		institute - which institution is the phrase associated with?
		pronunciation - optional pronunciation (ex: wdl - "widdle")
		seealso - related but not equivalent entries, such as CLI being related to Dockstore CLI. 
		updated - when the entry was last updated

		When outputting to RST, acronym_full, seealso, & definition will replace text in [brackets] 
		with a working internal hyperlink to another entry. For example, if self.definition="I use 
		[Seven Bridges]", then the RST out will be "I use :ref:`dict Seven Bridges`" (although the
		link will not be clickable if there is no
		'''
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

	def _process_internal_link_brackets_(self, words:list):
		'''For RST formatting, process internal hyperlinks, marked in entries.py as [this]'''
		words_processed = []
		multi_word_flag = False
		for word in words:
			if re.search("][a-zA-Z]+", word):
				print(f"Warning: {self.return_name()} will have an invalid internal link due RST limitations. Put some sort of whitespace or punctuation before any additional letters after the ending bracket. Problematic word: {word}")
			
			# This is the beginning of an internal RST link
			elif word.startswith("["):
				word = word[1:]  # strip [
				if "]" in word:
					multi_word_flag = False
					word = word.replace("]", "`")
					word = f":ref:`dict {word}"
				else:
					multi_word_flag = True
					word = f":ref:`dict {word}"
				
				words_processed.append(word)
			
			# This is a continuation of a previous word's RST link
			# will break on [Seven Br]idges] but that's not my problem
			elif multi_word_flag == True:

				if "]" in word:
					multi_word_flag = False
					word = word.replace("]", "`")
					word = f"{word}"
				else:
					word = f"{word}"
				
				words_processed.append(word)

			else:
				words_processed.append(word)
		
		return " ".join(words_processed)

	def _underline_text_(self, text:str, underlinechar="-"):
		'''Underlines text in a RST-supported way'''
		return [f"{text}\n", underlinechar * len(text)+"\n"]

	def text_rst_bookmark(self):
		'''Generates an RST bookmark for the entry'''
		return f".. _dict {self.return_name(nospaces=False)}:"

	def text_entry_title(self):
		'''Return underlined title. Same in RST, Markdown, and plaintext.'''
		entry_title = []
		entry_title.append("\n\n")  # keep space between entries big enough to keep RST happy
		entry_title.extend(self._underline_text_(self.name))
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
			words = self.acronym_full.split()
			return f"*abbreviation for* {self._process_internal_link_brackets_(words)}  \n\n"

	def text_definition(self, format="txt"):
		'''If RST, we need to make the [references to other entries] into internal links.
		Limitations: RST does not support letters coming after a link without a puncuation mark.'''

		if format == "txt":
			return f"	{self.definition}\n"
		elif format == "rst":
			words = self.definition.split()
			processed_with_links = self._process_internal_link_brackets_(words)
			return f"	{processed_with_links}  \n\n"

	def text_institute(self, format="txt"):
		'''In RST form this becomes a note block.'''
		if format == "txt":
			return f"This term as we define it here is associated with {self.institute} and may have different definitions in other contexts.\n"
		elif format == "rst":
			return f".. note:: This term as we define it here is associated with {self.institute} and may have different definitions in other contexts.  \n"
		
	def text_seealso(self, format="txt"):
		'''There is a supposedly simplier way to do this with sphinx.ext.autosectionlabel, via:
			see also :ref:`{self.seealso}`
		...but that would require we reformat piles of documentation (175 errors!)'''
		if format == "txt":
			return f"see also {self.seealso}\n"
		elif format == "rst":
			if self.institute == "":
				return f"see also :ref:`dict {self.seealso}`  \n"
			else:  # not strictly necessary to render correctly, but without this warning will be thrown
				return f"\nsee also :ref:`dict {self.seealso}`  \n"

	def text_furtherreading(self, format="txt"):
		'''If there is a see also, we need an extra newline. If not, avoid the extra newline.'''
		if format == "txt":
			return f"Further reading: {self.furtherreading}\n"
		elif format == "rst":
			if self.seealso == "" and self.institute == "":
				return f"Further reading: `<{self.furtherreading}>`_  \n"
			else:
				return f"\nFurther reading: `<{self.furtherreading}>`_  \n"

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


class GreatGloss:
	'''Object for an entire glossary'''
	def __init__(self, title, outfile="", outtoc="", updated=datetime.date.today()):
		self.title: str = title
		self.outfile: str = outfile
		self.outtoc: str = outtoc
		self.updated: datetime = updated
		self.glosslist: list[GlossEntry] = []
		self._gentries_: generator = self._generate_entries_()

	def add_entry(self, entry:GlossEntry):
		self.glosslist.append(entry)

	def _generate_entries_(self, asRSTlinks=False):
		for entry in self.glosslist:
			if asRSTlinks:
				# remember: _process_internal_link_brackets_() expects input as a list, not str!
				yield entry._process_internal_link_brackets_([f"[{entry.return_name()}]"])
			else:
				yield f"{entry.return_name()}\n"

	def sort_entries(self, ignorecase=True):
		if ignorecase:
			self.glosslist.sort(key=lambda x: x.name.upper())
		else:
			self.glosslist.sort(key=lambda x: x.name)

	def make_toc(self, format="rst", columns=3):
		'''generates a TOC
		if columns>=1 && format=="rst": number of hlist columns to use
		if columns<=0 && format=="rst": use Sphinx built in local TOC instead of hlist'''
		TOC = []
		if format=="rst" or format=="RST":
			if columns<=0:
				TOC.append(".. contents:: Table of Contents \n\t:local:\n\n")
			else:
				TOC.append(f".. hlist:: \n\t:columns: {columns}\n\n")
			for entry in self._generate_entries_(asRSTlinks=True):
				TOC.append(f"\t* {entry}\n")
		else:
			for entry in self._generate_entries_(asRSTlinks=False):
				TOC.append(entry)
		print(TOC)
		return TOC


	def write_glossary(self, outfile="", format="rst", skipTOC=False):
		'''write a glossary to a file, in plaintext or RST formatting'''
		if outfile=="" and self.outfile=="":
			raise RuntimeError("No output file for glossary specified")
		with open(outfile if outfile!="" else self.outfile, "a") as f:
			f.write("".join(self.text_glossary_title()))
			if not skipTOC:
				f.write("".join(self.make_toc()))
				#
				#
				# toc stuff
				#
				#
				f.write("\n")  # needed to keep RST from getting mad
			for entry in self.glosslist:
				entry.generate_RST()

	def write_toc(self, outtoc="", format="txt"):
		'''write a TOC to a file'''
		if outtoc=="" and self.outtoc=="":
			raise RuntimeError("No output file for TOC specified")
		with open(outtoc if outtoc!="" else self.outtoc, "a") as f:
			f.write("".join(self.make_toc(format=format)))

	def text_glossary_title(self):
		return self._underline_text_(self.title, underlinechar="=")

	def _underline_text_(self, text:str, underlinechar="-"):
		return [f"{text}\n", underlinechar * len(text)+"\n"]
