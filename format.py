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
			# print name
			f.write(f"{self.name}\n")

			# print pronunciation
			if self.pronunciation is not "":
				f.write(f"[pronounced {self.pronunciation}]")
			
			# generate underline (excludes pronunciation, which will be problematic in RST)
			for x in range(0,len(self.name)):
				f.write("-")
			f.write("\n")
			

			# print full form of acronym and see also
			# for an acronym, seealso will replace the full form of the acronym
			# currently seealso does not get printed if there is no acronym_full
			# this is by design... for now
			if self.acronym_full is not "" and self.seealso is not "":
				f.write(f"   see {self.seealso}\n")
			if self.acronym_full is not "" and self.seealso is "":
				f.write(f"   acronym for {self.acronym_full}\n")
			else:
				pass


			if self.definition is not "":
				f.write(f"{self.definition}\n")

			if self.institute is not "":
				f.write(f"This term as we define it here is associated with {self.institute} and may have different definitions in other contexts.\n")
			

			if self.furtherreading is not "":
				f.write(f"Further reading: {self.furtherreading}\n")

			f.write(self.updated.strftime("updated %Y-%m-%d\n"))


# please try to keep this in alphabetical order

BDC = Gloss("BDC", 
	acronym_full="Biodata Catalyst", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="Biodata Catalyst")

BDCat = Gloss("BDCat", 
	acronym_full="BioData Catalyst", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="Biodata Catalyst")

BioDataCatalyst = Gloss("Biodata Catalyst", 
	acronym_full="", 
	definition="An initiative funded by NHLBI to connect several cloud-based bioinformatics platforms together to increase reproducibility in bioinformatics. Involves Dockstore, Terra, Seven Bridges, Gen3, and PIC-SURE.", 
	furtherreading="https://biodatacatalyst.nhlbi.nih.gov/", 
	institute="NIH", 
	internal=False, 
	pronunciation="", 
	seealso="")

CommonWorkflowLanguage = Gloss("Common Workflow Language", 
	acronym_full="", 
	definition="", 
	furtherreading="https://www.commonwl.org/user_guide/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

CWL = Gloss("CWL", 
	acronym_full="Common Workflow Language", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="Common Workflow Language")

Docker = Gloss("Docker", 
	acronym_full="", 
	definition="A program that can create [Docker images], which are somewhat similiar to virutal machines, as well as run those images. In the context of bioinformatics, this technology has two main benefits: First, a Docker image bundles up everything a given piece of software needs to run, meaning that someone who wants to run (for example) samtools via Docker only needs to install Docker, not samtools. Second, an instance of a Docker image (called a [Docker container]) is a relatively standardized environment even when running on different backends, meaning that two people running the same software in the same Docker image on two different computers are likely to get the exact same results. In other words, Docker is good for reproducibility and ease of use.", 
	furtherreading="https://docs.docker.com/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

DockerContainer = Gloss("Docker container", 
	acronym_full="", 
	definition="In order to actually use the software inside a [Docker image] using the `docker run` command, the Docker program creates a writeable [layer] on top of the image, which leads to the creation of a [Docker container]. You can think of a Docker image as an unchanging template, and a Docker container as a writeable instance generated from that template. A Docker image can exist on its own, but a Docker container requires a Docker image.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

Dockerfile = Gloss("Dockerfile", 
	acronym_full="", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

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
	seealso="")

OICR = Gloss("OICR", 
	acronym_full="Ontario Institute for Cancer Research", 
	definition="A non-profit research institute based in Toronto that is focused on cancer detection and treatment. One of the two institutes involved in the development of Dockstore, the other being [UCSC].", 
	furtherreading="https://oicr.on.ca/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

WDL = Gloss("WDL",
	acronym_full="Workflow Description Language",
	pronunciation='"widdle", rhymes with little',
	seealso="Workflow Description Language")

Workflow_Description_Language = Gloss("Workflow Description Language",
	furtherreading="https://openwdl.org/",
	definition="A workflow language managed by the Open WDL Project. Usually written as [WDL].",
	seealso="WDL")

UCSC = Gloss("UCSC", 
	acronym_full="University of California, Santa Cruz", 
	definition="A public university located in Santa Cruz that is focused on undergraduate and graduate education and research. The Genomics Institute, a branch of UCSC's engineering department, is one of the two institutes involved in the development of Dockstore, the other being [OICR].", 
	furtherreading="https://ucsc.edu", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

YAML = Gloss("YAML", 
	acronym_full="YAML Ain't Markup Language", 
	definition="Human-readable data-serialization lanaguage. Commonly used for configuration files.", 
	furtherreading="https://yaml.org/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")


for entry in [
	BDC, BDCat, BioDataCatalyst,
	CommonWorkflowLanguage, CWL,
	Docker, DockerContainer, Dockerfile, DockerImage, DockerLayer, 
	OICR,
	WDL, Workflow_Description_Language, 
	UCSC, 
	YAML]:
	entry.generate_plaintext()


