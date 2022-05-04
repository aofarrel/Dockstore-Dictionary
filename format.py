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
		# name (string) - entry's name, make sure to use correct capitalization/lack thereof
		# acronym_full (string) - if acronym, what is the full name. if blank, assumed to not be an acronym
		# further_reading (string) - URL to a webpage, usually an "official" one associated with the term
		# institute (string) - optional, which institution is the phrase associated with, if any? For instance, Terra is associated with the Broad Institute. GCP is associated with Google. Does not necessarily imply a trademark or copyright.
		# internal (bool) - Is this only used internally? For acronyms this may imply the acronym is internal but the phrase it refers to is not (ex: gha - github app)
		# pronunciation (string) - optional pronunciation (ex: wdl - "widdle")
		# updated (date) - when the entry was last updated


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


# please try to keep this in alphabetical order

Docker = Gloss("Docker", 
	acronym_full="", 
	definition="A program that can create [Docker images], which are somewhat similiar to virutal machines, as well as run those images. In the context of bioinformatics, this technology has two main benefits: First, a Docker image bundles up everything a given piece of software needs to run, meaning that someone who wants to run (for example) samtools via Docker only needs to install Docker, not samtools. Second, an instance of a Docker image (called a [Docker container]) is a relatively standardized environment even when running on different backends, meaning that two people running the same software in the same Docker image on two different computers are likely to get the exact same results. In other words, Docker is good for reproducibility and ease of use.", 
	furtherreading="https://docs.docker.com/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso=None)

DockerContainer = Gloss("Docker container", 
	acronym_full="", 
	definition="In order to actually use the software inside a [Docker image] using the `docker run` command, the Docker program creates a writeable [layer] on top of the image, which leads to the creation of a [Docker container]. You can think of a Docker image as an unchanging template, and a Docker container as a writeable instance generated from that template. A Docker image can exist on its own, but a Docker container requires a Docker image.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso=None)

Dockerfile = Gloss("Dockerfile", 
	acronym_full="", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso=None)

DockerImage = Gloss("Docker image", 
	acronym_full="", 
	definition="A read-only file that represents a filesystem that contains some sort of code and that code's depedencies. A Docker image can be created using the `docker build` command in conjunction with a [Dockerfile]. If a workflow language references a Docker image, then the workflow executor will download that Docker image (unless was already downloaded previously) and add a writeable layer onto the Docker image, which results in the creation of a [Docker container].", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso=None)

DockerLayer = Gloss("layer", 
	acronym_full="", 
	definition="In the context of Docker, a layer is a component of a Docker image. Each `RUN`, `COPY`, and `ADD` instruction in a [Dockerfile] will lead to the creation of a layer.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso=None)

WDL = Gloss("WDL",
	acronym_full="Workflow Description Language",
	pronunciation='"widdle", rhymes with little',
	seealso="Workflow Description Language")

Workflow_Description_Language = Gloss("Workflow Description Language",
	furtherreading="https://openwdl.org/",
	definition="A workflow language managed by the Open WDL Project. Usually written as [WDL].",
	seealso="WDL")






for entry in [Docker, DockerContainer, Dockerfile, DockerImage, DockerLayer, WDL, Workflow_Description_Language]:
	entry.generate_plaintext()


