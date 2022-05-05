# please try to keep this in alphabetical order

from Gloss import GlossEntry

AnVIL = GlossEntry("AnVIL Project", 
	acronym_full="Analysis Visualization and Informatics Labspace", 
	definition="A cloud-based ecosystem funded by [NHGRI], bringing together Dockstore, [Gen3], [Terra], [NCPI], Galaxy, Jupyter, Seqr, and Bioconductor into an integrated platform. Sometimes refered to as just \"the AnVIL\" or \"AnVIL\".", 
	furtherreading="https://anvilproject.org/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

BDC = GlossEntry("BDC", 
	acronym_full="Biodata Catalyst", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="Biodata Catalyst")

BDCat = GlossEntry("BDCat", 
	acronym_full="BioData Catalyst", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="Biodata Catalyst")

BioDataCatalyst = GlossEntry("Biodata Catalyst", 
	acronym_full="", 
	definition="An initiative funded by NHLBI to connect several cloud-based bioinformatics platforms together to increase reproducibility in bioinformatics. Involves Dockstore, Terra, Seven Bridges, Gen3, and PIC-SURE.", 
	furtherreading="https://biodatacatalyst.nhlbi.nih.gov/", 
	institute="NIH", 
	internal=False, 
	pronunciation="", 
	seealso="")

CancerGenomicsCloud = GlossEntry("Cancer Genomics Cloud", 
	acronym_full="", 
	definition="A cloud platform by [Seven Bridges] and funded by [NCI] for bioinformatics analysis.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

CGC = GlossEntry("CGC", 
	acronym_full="Cancer Genomics Cloud", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="Cancer Genomics Cloud")

CommonWorkflowLanguage = GlossEntry("Common Workflow Language", 
	acronym_full="", 
	definition="", 
	furtherreading="https://www.commonwl.org/user_guide/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

Cromwell = GlossEntry("Cromwell", 
	acronym_full="", 
	definition="An open-source [WDL] executor managed by the Broad Institute. Cromwell is the default executor for the [Dockstore CLI] and is the executor used by [Terra].", 
	furtherreading="https://cromwell.readthedocs.io/en/stable/", 
	institute="Broad Institute", 
	internal=False, 
	pronunciation="", 
	seealso="")

CWL = GlossEntry("CWL", 
	acronym_full="Common Workflow Language", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="Common Workflow Language")

DAG = GlossEntry("DAG", 
	acronym_full="Directed Acyclic Graph", 
	definition="A directional graph like a flowchart that does not have any loops. On Dockstore we use DAGs to show the steps that a workflow takes.", 
	furtherreading="https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

Docker = GlossEntry("Docker", 
	acronym_full="", 
	definition="A program that can create [Docker images], which are somewhat similiar to virutal machines, as well as run those images. In the context of bioinformatics, this technology has two main benefits: First, a Docker image bundles up everything a given piece of software needs to run, meaning that someone who wants to run (for example) samtools via Docker only needs to install Docker, not samtools. Second, an instance of a Docker image (called a [Docker container]) is a relatively standardized environment even when running on different backends, meaning that two people running the same software in the same Docker image on two different computers are likely to get the exact same results. In other words, Docker is good for reproducibility and ease of use.", 
	furtherreading="https://docs.docker.com/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

DockerContainer = GlossEntry("Docker container", 
	acronym_full="", 
	definition="In order to actually use the software inside a [Docker image] using the `docker run` command, the Docker program creates a writeable [layer] on top of the image, which leads to the creation of a [Docker container]. You can think of a Docker image as an unchanging template, and a Docker container as a writeable instance generated from that template. A Docker image can exist on its own, but a Docker container requires a Docker image.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

Dockerfile = GlossEntry("Dockerfile", 
	acronym_full="", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

DockerImage = GlossEntry("Docker image", 
	acronym_full="", 
	definition="A read-only file that represents a filesystem that contains some sort of code and that code's depedencies. A Docker image can be created using the `docker build` command in conjunction with a [Dockerfile]. If a workflow language references a Docker image, then the workflow executor will download that Docker image (unless was already downloaded previously) and add a writeable layer onto the Docker image, which results in the creation of a [Docker container].", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

DockerLayer = GlossEntry("layer", 
	acronym_full="", 
	definition="In the context of Docker, a layer is a component of a Docker image. Each `RUN`, `COPY`, and `ADD` instruction in a [Dockerfile] will lead to the creation of a layer.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

DockstoreCLI = GlossEntry("Dockstore CLI", 
	acronym_full="Dockstore Command Line Interface", 
	definition="A command-line program developed by Dockstore. It is not required to use Dockstore, but it has many features to make running and developing workflows easier.", 
	furtherreading="https://docs.dockstore.org/en/stable/advanced-topics/dockstore-cli/dockstore-cli-faq.html", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

DOI = GlossEntry("DOI", 
	acronym_full="Digital Object Identifiers", 
	definition="An identifier that provides a long-lasting link to some sort of digital object. On Docktore, you can use Zenodo to mint a DOI of your workflows and tools to increase reproducibility.", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

Elwazi = GlossEntry("eLwazi", 
	acronym_full="", 
	definition="An African-lead open data science platform funded as part of the [NIH]'s [DSI-Africa] program. Leverages [Gen3] and [Terra].", 
	furtherreading="https://elwazi.org/",
	institute="", 
	internal=False, 
	pronunciation='"el-woz-ee", derived from Xhosa word for knowledge', 
	seealso="")

JSON = GlossEntry("JSON", 
	acronym_full="JavaScript Object Notation", 
	definition="A human-readible file format that orginated in JavaScript, but is now used by a variety of applications. Dockstore supports the inclusion of JSON and [YAML] files in entries to provide sample inputs for workflow and tool entries. Some workflow executors, such as [Cromwell], can use these files to configure their inputs rather than having to manually listing every input when calling the workflow on the command line.", 
	furtherreading="https://www.json.org/json-en.html", 
	institute="", 
	internal=False, 
	pronunciation='"jason"', 
	seealso="")

NCI = GlossEntry("NCI", 
	acronym_full="", 
	definition="", 
	furtherreading="", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

NHGRI = GlossEntry("NHGRI", 
	acronym_full="National Human Genome Research Institute", 
	definition="A division of the [NIH] that focus on genomics research. Funds the [AnVIL Project].", 
	furtherreading="https://www.genome.gov/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

NHLBI = GlossEntry("NHLBI", 
	acronym_full="National Heart, Lungs, and Blood Institute", 
	definition="A division of the [NIH] that focuses on heart, lung, blood, and sleep health. Funds the [BioData Catalyst] platform.", 
	furtherreading="https://www.nhlbi.nih.gov/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

NIH = GlossEntry("NIH", 
	acronym_full="National Institute of Health", 
	definition="An American government institution, part of the Department of Health and Human Services, that engages in medical research.", 
	furtherreading="https://www.nih.gov/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

OICR = GlossEntry("OICR", 
	acronym_full="Ontario Institute for Cancer Research", 
	definition="A non-profit research institute based in Toronto that is focused on cancer detection and treatment. One of the two institutes involved in the development of Dockstore, the other being [UCSC].", 
	furtherreading="https://oicr.on.ca/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

Terra = GlossEntry("Terra", 
	acronym_full="", 
	definition="A cloud-based workflow execution platform developed by the Broad Institute. Terra supports the execution of [WDL] workflows, Jupyter/R notebooks, and integrated apps such as a DICOM-file viewer. The computational backend of Terra is based upon Google, allowing Google-specific features such as [preemptible] machines to be used in workflows. Dockstore supports directly importing [WDL] workflows into a Terra workspace. Terra is part of the [BioData Catalyst], [AnVIL Project], and [eLwazi] grants.", 
	furtherreading="https://terra.bio", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

WDL = GlossEntry("WDL",
	acronym_full="Workflow Description Language",
	pronunciation='"widdle", rhymes with little',
	seealso="Workflow Description Language")

Workflow_Description_Language = GlossEntry("Workflow Description Language",
	furtherreading="https://openwdl.org/",
	definition="A workflow language managed by the Open WDL Project. Usually written as [WDL].",
	seealso="WDL")

UCSC = GlossEntry("UCSC", 
	acronym_full="University of California, Santa Cruz", 
	definition="A public university located in Santa Cruz that is focused on undergraduate and graduate education and research. The Genomics Institute, a branch of UCSC's engineering department, is one of the two institutes involved in the development of Dockstore, the other being [OICR].", 
	furtherreading="https://ucsc.edu", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")

YAML = GlossEntry("YAML", 
	acronym_full="YAML Ain't Markup Language", 
	definition="Human-readable data-serialization lanaguage. Commonly used for configuration files.", 
	furtherreading="https://yaml.org/", 
	institute="", 
	internal=False, 
	pronunciation="", 
	seealso="")