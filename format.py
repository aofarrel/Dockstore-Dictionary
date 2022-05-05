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

			# print name and underline it
			f.write(f"{self.name}\n")
			for x in range(0,len(self.name)):
				f.write("-")
			f.write("\n")

			# print pronunciation
			if self.pronunciation is not "":
				f.write(f"[pronounced {self.pronunciation}]\n")

			# print full form of acronym or see also
			# for an acronym, seealso will replace the full form of the acronym
			# this section could probably be written cleaner
			if self.acronym_full is not "" and self.seealso is not "":
				f.write(f"see {self.seealso}\n")
			elif self.acronym_full is not "" and self.seealso is "":
				f.write(f"abbreviation for {self.acronym_full}\n")
			elif self.acronym_full is "" and self.seealso is not "":
				f.write(f"see {self.seealso}\n")
			else:
				pass


			if self.definition is not "":
				f.write(f"	{self.definition}\n")

			if self.institute is not "":
				f.write(f"This term as we define it here is associated with {self.institute} and may have different definitions in other contexts.\n")
			

			if self.furtherreading is not "":
				f.write(f"Further reading: {self.furtherreading}\n")

			f.write(self.updated.strftime("updated %Y-%m-%d\n"))


# please try to keep this in alphabetical order

# this is starting to veer into the territory of just replacing BDC's dictionary...

AnVIL = Gloss("AnVIL Project", 
	acronym_full="Analysis Visualization and Informatics Labspace", 
	definition="A cloud-based ecosystem funded by [NHGRI], bringing together Dockstore, [Gen3], [Terra], [NCPI], Galaxy, Jupyter, Seqr, and Bioconductor into an integrated platform. Sometimes refered to as just \"the AnVIL\" or \"AnVIL\".", 
	furtherreading="https://anvilproject.org/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

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

CancerGenomicsCloud = Gloss("Cancer Genomics Cloud", 
	acronym_full="", 
	definition="A cloud platform by [Seven Bridges] and funded by [NCI] for bioinformatics analysis.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

CGC = Gloss("CGC", 
	acronym_full="Cancer Genomics Cloud", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="Cancer Genomics Cloud")

CommonWorkflowLanguage = Gloss("Common Workflow Language", 
	acronym_full="", 
	definition="", 
	furtherreading="https://www.commonwl.org/user_guide/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

Cromwell = Gloss("Cromwell", 
	acronym_full="", 
	definition="An open-source [WDL] executor managed by the Broad Institute. Cromwell is the default executor for the [Dockstore CLI] and is the executor used by [Terra].", 
	furtherreading="https://cromwell.readthedocs.io/en/stable/", 
	institute="Broad Institute", 
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

DAG = Gloss("DAG", 
	acronym_full="Directed Acyclic Graph", 
	definition="A directional graph like a flowchart that does not have any loops. On Dockstore we use DAGs to show the steps that a workflow takes.", 
	furtherreading="https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

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
	seealso="")

DockerLayer = Gloss("layer", 
	acronym_full="", 
	definition="In the context of Docker, a layer is a component of a Docker image. Each `RUN`, `COPY`, and `ADD` instruction in a [Dockerfile] will lead to the creation of a layer.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

DockstoreCLI = Gloss("Dockstore CLI", 
	acronym_full="Dockstore Command Line Interface", 
	definition="A command-line program developed by Dockstore. It is not required to use Dockstore, but it has many features to make running and developing workflows easier.", 
	furtherreading="https://docs.dockstore.org/en/stable/advanced-topics/dockstore-cli/dockstore-cli-faq.html", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

DOI = Gloss("DOI", 
	acronym_full="Digital Object Identifiers", 
	definition="An identifier that provides a long-lasting link to some sort of digital object. On Docktore, you can use Zenodo to mint a DOI of your workflows and tools to increase reproducibility.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

Elwazi = Gloss("eLwazi", 
	acronym_full="", 
	definition="An African-lead open data science platform funded as part of the [NIH]'s [DSI-Africa] program. Leverages [Gen3] and [Terra].", 
	furtherreading="https://elwazi.org/",
	institute="", 
	internal=False, 
	pronunciation='"el-woz-ee", derived from Xhosa word for knowledge', 
	seealso="")

JSON = Gloss("JSON", 
	acronym_full="JavaScript Object Notation", 
	definition="A human-readible file format that orginated in JavaScript, but is now used by a variety of applications. Dockstore supports the inclusion of JSON and [YAML] files in entries to provide sample inputs for workflow and tool entries. Some workflow executors, such as [Cromwell], can use these files to configure their inputs rather than having to manually listing every input when calling the workflow on the command line.", 
	furtherreading="https://www.json.org/json-en.html", 
	institute="", 
	internal=False, 
	pronunciation='"jason"', 
	seealso="")

NCI = Gloss("NCI", 
	acronym_full="", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

NHGRI = Gloss("NHGRI", 
	acronym_full="National Human Genome Research Institute", 
	definition="A division of the [NIH] that focus on genomics research. Funds the [AnVIL Project].", 
	furtherreading="https://www.genome.gov/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

NHLBI = Gloss("NHLBI", 
	acronym_full="National Heart, Lungs, and Blood Institute", 
	definition="A division of the [NIH] that focuses on heart, lung, blood, and sleep health. Funds the [BioData Catalyst] platform.", 
	furtherreading="https://www.nhlbi.nih.gov/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

NIH = Gloss("NIH", 
	acronym_full="National Institute of Health", 
	definition="An American government institution, part of the Department of Health and Human Services, that engages in medical research.", 
	furtherreading="https://www.nih.gov/", 
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

Terra = Gloss("Terra", 
	acronym_full="", 
	definition="A cloud-based workflow execution platform developed by the Broad Institute. Terra supports the execution of [WDL] workflows, Jupyter/R notebooks, and integrated apps such as a DICOM-file viewer. The computational backend of Terra is based upon Google, allowing Google-specific features such as [preemptible] machines to be used in workflows. Dockstore supports directly importing [WDL] workflows into a Terra workspace. Terra is part of the [BioData Catalyst], [AnVIL Project], and [eLwazi] grants.", 
	furtherreading="https://terra.bio", 
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

# there's gotta be a way to do this automagically

for entry in [
	AnVIL,
	BDC, BDCat, BioDataCatalyst,
	CancerGenomicsCloud, CGC, CommonWorkflowLanguage, Cromwell, CWL,
	DAG, Docker, DockerContainer, Dockerfile, DockerImage, DockerLayer, DockstoreCLI, DOI,
	Elwazi,
	JSON,
	NCI, NHGRI, NHLBI, NIH
	OICR,
	Terra,
	WDL, Workflow_Description_Language, 
	UCSC, 
	YAML]:
	entry.generate_plaintext()


