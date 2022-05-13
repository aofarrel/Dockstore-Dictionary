# please try to keep this in alphabetical order

# due to RST limitations, do not make internal links plural
# acceptable: [WDL] [WDL], [WDL]. [WDL]'s [Seven Bridges] [Seven Bridges], [Seven Bridges]. [Seven Bridges]'s
# will break: [WDL]s [Seven Bridges]s

from Gloss import GlossEntry

AnVIL = GlossEntry("AnVIL Project", 
	acronym_full="Analysis Visualization and Informatics Labspace", 
	definition="A cloud-based ecosystem funded by [NHGRI], bringing together Dockstore, Gen3, [Terra], [NCPI], Galaxy, Jupyter, Seqr, and Bioconductor into an integrated platform. Sometimes referred to as just \"the AnVIL\" or \"AnVIL\".", 
	furtherreading="https://anvilproject.org/", 
	institute="", 
	pronunciation="", 
	seealso="")

API = GlossEntry("API", 
	acronym_full="Application Programmer Interface", 
	definition="A software-based intermediary used to exchange data, often between two different platforms. Communication between different cloud platforms is mediated by various APIs, such as [TES].", 
	furtherreading="", 
	institute="", 
	pronunciation="", 
	seealso="")

AWS = GlossEntry("AWS", 
	acronym_full="Amazon Web Services", 
	definition="A provider of cloud services, most notably cloud computing and cloud storage, available on-demand and hosted by Amazon. [Seven Bridges] is an example of a system that is powered by AWS, and can launch workflows on [EC2] instances.", 
	furtherreading="https://docs.aws.amazon.com/index.html?nc2=h_ql_doc_do", 
	institute="", 
	pronunciation="", 
	seealso="GCP")

BDC = GlossEntry("BDC", 
	acronym_full="[Biodata Catalyst]", 
	pronunciation='"bee-dee-see"')

BDCatalyst = GlossEntry("BD Catalyst", 
	acronym_full="[BioData Catalyst]")

BioDataCatalyst = GlossEntry("Biodata Catalyst", 
	acronym_full="", 
	definition="An initiative funded by [NHLBI] to connect several cloud-based bioinformatics platforms together to increase reproducibility in bioinformatics. Involves Dockstore, [Terra], Seven Bridges, Gen3, and PIC-SURE.", 
	furtherreading="https://biodatacatalyst.nhlbi.nih.gov/", 
	institute="", 
	pronunciation="", 
	seealso="")

CancerGenomicsCloud = GlossEntry("Cancer Genomics Cloud", 
	acronym_full="", 
	definition="A cloud platform by [Seven Bridges] and funded by [NCI] for bioinformatics analysis.", 
	furtherreading="", 
	institute="", 
	pronunciation="", 
	seealso="")

CGC = GlossEntry("CGC", 
	acronym_full="[Cancer Genomics Cloud]")

CLI = GlossEntry("CLI", 
	acronym_full="Command Line Interface", 
	definition="A program that can be interacted with on the command line, usually via \"Terminal\" on MacOS and Linux or \"cmd\"/Command Prompt on Windows. CLI programs generally do not have a graphical user interface.", 
	furtherreading="https://en.wikipedia.org/wiki/Command-line_interface", 
	institute="", 
	pronunciation="", 
	seealso="")

CloudComputing = GlossEntry("cloud computing", 
	acronym_full="", 
	definition="Doing computational tasks on a remote machine that is made available on-demand without the user having to manage all aspects of it. Generally implies that the user is essentially renting computational resources from someone else. Well-known cloud providers include [GCP], [AWS], Microsoft Azure, and Alibaba Cloud.", 
	furtherreading="https://en.wikipedia.org/wiki/Cloud_computing", 
	institute="", 
	pronunciation='', 
	seealso="")

CommonWorkflowLanguage = GlossEntry("Common Workflow Language", 
	acronym_full="", 
	definition="A workflow language that describes how to run command-line tools. CWL is based on Java and can use Java commands within its own commands. [WDL] and CWL are relatively similar in principle, and code written in one language can often be translated into the other with some workarounds, but they are two different standards and each have unique features.", 
	furtherreading="https://www.commonwl.org/user_guide/", 
	institute="", 
	pronunciation="", 
	seealso="CWL")

Container = GlossEntry("container", 
	acronym_full="", 
	definition="An emulated computer system that contains programs and their prerequisites, but does not contain the entire operating system. Unlike a [VM], a container shares the same kernel as the host OS. A well known type of container is a [Docker container].", 
	furtherreading="", 
	institute="", 
	pronunciation='', 
	seealso="")

Cromwell = GlossEntry("Cromwell", 
	acronym_full="", 
	definition="An open-source [WDL] executor managed by the Broad Institute. Cromwell is the default executor for the [Dockstore CLI] and is the executor used by [Terra].", 
	furtherreading="https://cromwell.readthedocs.io/en/stable/", 
	institute="Broad Institute", 
	pronunciation="", 
	seealso="")

CWL = GlossEntry("CWL", 
	acronym_full="[Common Workflow Language]")

DAG = GlossEntry("DAG", 
	acronym_full="Directed Acyclic Graph", 
	definition="A directional graph like a flowchart that does not have any loops. On Dockstore we use DAGs to show the steps that a workflow takes.", 
	furtherreading="https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html", 
	institute="", 
	pronunciation="", 
	seealso="")

DescriptorFile = GlossEntry("descriptor file", 
	acronym_full="", 
	definition="A file used to programmatically describe a tool or workflow. This file represents the instructions that will actually be executed. On Dockstore, we support .ga, .cwl, .wdl, and .nfl file extensions for [Galaxy], [CWL], [WDL], and [Nextflow] respectively.", 
	furtherreading="", 
	institute="", 
	pronunciation='', 
	seealso="")

Docker = GlossEntry("Docker", 
	acronym_full="", 
	definition="A program that can create \"images\" which are somewhat similar to virtual machines, as well as run those images. In the context of bioinformatics, this technology has two main benefits: First, a [Docker image] bundles up everything a given piece of software needs to run, meaning that someone who wants to run (for example) samtools via Docker only needs to install Docker, not samtools. Second, an instance of a Docker image is a relatively standardized environment even when running on different backends, meaning that two people running the same software in the same Docker image on two different computers are likely to get the exact same results. In other words, Docker is good for reproducibility and ease of use.", 
	furtherreading="https://docker-curriculum.com/", 
	institute="", 
	pronunciation='"daw-ker", rhymes with walker', 
	seealso="")

DockerContainer = GlossEntry("Docker container", 
	acronym_full="", 
	definition="In order to actually use the software inside a [Docker image] using the `docker run` command, the Docker program creates a writable [layer] on top of the image, which leads to the creation of a [Docker container]. You can think of a Docker image as an unchanging template, and a Docker container as a writable instance generated from that template. A Docker image can exist on its own, but a Docker container requires a Docker image.", 
	furtherreading="https://www.docker.com/resources/what-container/", 
	institute="", 
	pronunciation="", 
	seealso="")

Dockerfile = GlossEntry("Dockerfile", 
	acronym_full="", 
	definition="A file describing the creation of a [Docker image] by running commands that each form a [layer].", 
	furtherreading="https://docs.docker.com/engine/reference/builder/", 
	institute="", 
	pronunciation="", 
	seealso="")

DockerImage = GlossEntry("Docker image", 
	acronym_full="", 
	definition="A read-only file that represents a filesystem that contains some sort of code and that code's dependencies. A Docker image can be created using the `docker build` command in conjunction with a [Dockerfile]. If a workflow language references a Docker image, then the workflow executor will download that Docker image (unless was already downloaded previously) and add a writable layer onto the Docker image, which results in the creation of a [Docker container].", 
	furtherreading="", 
	institute="", 
	pronunciation="", 
	seealso="")

DockstoreCLI = GlossEntry("Dockstore CLI", 
	acronym_full="Dockstore Command Line Interface", 
	definition="A command-line program developed by Dockstore. It is not required to use Dockstore, but it has many features to make running and developing workflows easier.", 
	furtherreading="https://docs.dockstore.org/en/stable/advanced-topics/dockstore-cli/dockstore-cli-faq.html", 
	institute="", 
	pronunciation="", 
	seealso="CLI")

DOI = GlossEntry("DOI", 
	acronym_full="Digital Object Identifier", 
	definition="An identifier that provides a long-lasting link to some sort of [immutable] digital object. On Dockstore, you can use Zenodo to mint a DOI of your workflows and tools to increase reproducibility.", 
	furtherreading="", 
	institute="", 
	pronunciation="", 
	seealso="")

DSIAfrica = GlossEntry("DS-I Africa", 
	acronym_full="Data Science for health discovery and Innovation in Africa", 
	definition="An [NIH] initiative to leverage data science to address the African continent's public health needs.", 
	furtherreading="https://commonfund.nih.gov/africadata", 
	institute="", 
	pronunciation='', 
	seealso="")

EC2 = GlossEntry("EC2", 
	acronym_full="Elastic Compute Cloud", 
	definition="The cloud computing side of [AWS]. When running workflows on these backends, disk size will scale with your workflow requirements automatically. EC2 instances allow you to make use of Amazon's [spot instance] feature, which may reduce the cost of running workflows.", 
	furtherreading="https://docs.aws.amazon.com/ec2/index.html", 
	institute="", 
	pronunciation='', 
	seealso="")

Egress = GlossEntry("egress", 
	acronym_full="", 
	definition="The action of leaving a place. In the context of [cloud computing], an egress charge is a fee charged for downloading a file. Sometimes, the person hosting the file is charged for data egress. Other times, the person downloading the file is charged.", 
	furtherreading="", 
	institute="cloud computing", 
	pronunciation='"ee-gress", rhymes with aggress', 
	seealso="")

Elwazi = GlossEntry("eLwazi", 
	acronym_full="", 
	definition="An African-lead open data science platform funded as part of the [NIH]'s [DS-I Africa] program. Leverages Gen3 and [Terra].", 
	furtherreading="https://elwazi.org/",
	institute="", 
	pronunciation='"el-woz-ee", derived from Xhosa word for knowledge', 
	seealso="")

Entry = GlossEntry("entry", 
	acronym_full="", 
	definition="A [tool] or [workflow] on Dockstore. A single entry on Dockstore has a description, a link to the original source-control repository, and at least one [descriptor file] which does some sort of computational task using [CWL], [WDL], [Nextflow], or [Galaxy workflow] syntax. An entry can optionally include a [parameter file] that links to open-access test data. A single entry will include all versions of the tool or workflow that has been registered, with that versioning being based upon the versioning and branches of the source-control repository the descriptor file is hosted on (with the exception of [legacy tools], which have versioning based upon their Docker image tags), and any version can be pinned as the default. Entries can be added to [collections] associated with a particular [organization], or added to [categories] so they can be grouped with other entries that have a similar scientific purpose. Entries may also have [labels] attached to them to help them be found via Dockstore's [faceted search] feature. If the entry is registered using the [Dockstore GitHub App], then the entry will stay in sync automatically with the source-control repository. Additionally, if an entry is a valid [workflow], any user can use our [launch with] feature to import the workflow to one of our cloud compute partners.", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='', 
	seealso="")

FAIR = GlossEntry("FAIR", 
	acronym_full="Findable, Accessible, Interoperable, and Reusable", 
	definition="A set of guidelines to improve the Findability, Accessibility, Interoperability, and Reuse of digital assets. This concept is often applied to data, but can be applied to other assets such as workflows.", 
	furtherreading="https://www.go-fair.org/fair-principles/",
	institute="", 
	pronunciation='"fair", rhymes with pear', 
	seealso="")

GA4GH = GlossEntry("GA4GH", 
	acronym_full="Global Alliance For Genomics and Health", 
	definition="A network of public and private institutions which aims to accelerate progress in genomic research and human health by cultivating a common framework of standards and harmonized approaches for effective and responsible genomic and health-related data sharing.", 
	furtherreading="https://www.ga4gh.org/", 
	institute="", 
	pronunciation='', 
	seealso="")

Galaxy = GlossEntry("Galaxy", 
	acronym_full="", 
	definition="An open-source platform that uses [FAIR] principles, most well-known for its web-based UI which can be used to run a variety of bioinformatics tools.", 
	furtherreading="https://galaxyproject.org/", 
	institute="", 
	pronunciation='', 
	seealso="")

GCP = GlossEntry("GCP", 
	acronym_full="Google Cloud Platform", 
	definition="A backend used for cloud computing and cloud storage hosted by Google. [Terra] is an example of a system that runs on a GCP backend. When running workflows on these backends, make sure to account for the storage needed for your workflow, as GCP compute backends do not automatically scale their storage size at runtime. GCP backends allow you to make use of Google's [preemptible] feature, which may reduce the cost of running workflows.", 
	furtherreading="https://cloud.google.com/gcp", 
	institute="", 
	pronunciation="", 
	seealso="EC2")

Immutable = GlossEntry("immutable", 
	acronym_full="", 
	definition="Unchanging, unable to be modified. Immutability implies that an object cannot be updated.", 
	furtherreading="", 
	institute="", 
	pronunciation='', 
	seealso="")

Interoperable = GlossEntry("interoperable", 
	acronym_full="", 
	definition="The ability of data or tools from multiple resources to effectively integrate data, or operate processes, across all systems with a moderate degree of effort.", 
	furtherreading="", 
	institute="", 
	pronunciation="", 
	seealso="")

JSON = GlossEntry("JSON", 
	acronym_full="JavaScript Object Notation", 
	definition="A human-readable file format that originated in JavaScript, but is now used by a variety of applications. Dockstore supports the inclusion of JSON and [YAML] files in entries to provide sample inputs for workflow and tool entries. Some workflow executors, such as [Cromwell], can use these files to configure their inputs rather than having to manually listing every input when calling the workflow on the command line.", 
	furtherreading="https://www.json.org/json-en.html", 
	institute="", 
	pronunciation='"jason"', 
	seealso="YAML")

Kernel = GlossEntry("kernel", 
	acronym_full="", 
	definition="An operating system's core program that is always loaded in memory, and modulates interactions between software and physical hardware, including but not limited to managing memory access for any program currently in RAM.", 
	furtherreading="https://en.wikipedia.org/wiki/Kernel_(operating_system)", 
	institute="", 
	pronunciation='', 
	seealso="")

Layer = GlossEntry("layer", 
	acronym_full="", 
	definition="In the context of Docker, a layer is a component of a Docker image. Each `RUN`, `COPY`, and `ADD` instruction in a [Dockerfile] will lead to the creation of a layer.", 
	furtherreading="", 
	institute="Docker", 
	pronunciation="", 
	seealso="")

LegacyRegistration = GlossEntry("legacy registration", 
	acronym_full="", 
	definition="", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='', 
	seealso="")

LegacyTool = GlossEntry("legacy tool", 
	acronym_full="",
	definition="On Dockstore, we use this term to refer to a [tool] that is registered using a [legacy registration] method. Legacy tools are not automatically synchronized with their source control repository, but can be updated manually by the tool maintainer. Additionally, legacy tools require a [Dockerfile] to be registered, and are versioned based on the tags of their associated [Docker image]. A legacy tool can be converted into a [GitHub App tool] via the following process: <https://docs.dockstore.org/en/stable/getting-started/github-apps/migrating-tools-to-github-apps.html>", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='', 
	seealso="")

LegacyWorkflow = GlossEntry("legacy workflow", 
	acronym_full="", 
	definition="On Dockstore, we use this term to refer to a [workflow] that is registered using a [legacy registration] method. Legacy workflows are not automatically synchronized with their source control repository, but can be updated manually by the workflow maintainer. A legacy workflow can be converted into a [GitHub App workflow] via the following process: <https://docs.dockstore.org/en/stable/getting-started/github-apps/migrating-workflows-to-github-apps.html>", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='', 
	seealso="")

NCI = GlossEntry("NCI", 
	acronym_full="National Cancer Institute ", 
	definition="A division of the [NIH] focused on cancer research.", 
	furtherreading="https://www.nih.gov/about-nih/what-we-do/nih-almanac/national-cancer-institute-nci", 
	institute="", 
	pronunciation="", 
	seealso="")

NCPI = GlossEntry("NCPI", 
	acronym_full="NIH Cloud Platform Interoperability", 
	definition="An effort to connect five [NIH] cloud projects and ensure they are interoperable. The five projects covered under this are the [AnVIL Project], [BioData Catalyst], Cancer Research Data Commons, Kids First, and the National Center for Biotechnology Information.",
	furtherreading="https://datascience.nih.gov/nih-cloud-platform-interoperability-effort", 
	institute="NIH", 
	pronunciation='', 
	seealso="")

Nextflow = GlossEntry("Nextflow", 
	acronym_full="", 
	definition="A Java-based computational workflow engine. Dockstore supports the hosting of Nextflow workflows.", 
	furtherreading="https://www.nextflow.io/", 
	institute="", 
	pronunciation='', 
	seealso="")

NFL = GlossEntry("NFL", 
	acronym_full="[Nextflow]", 
	definition="An uncommon acronym for [Nextflow]. This abbreviation is not used as frequently as [CWL] or [WDL], but does see usage occasionally.", 
	furtherreading="", 
	institute="", 
	pronunciation='', 
	seealso="")

NHGRI = GlossEntry("NHGRI", 
	acronym_full="National Human Genome Research Institute", 
	definition="A division of the [NIH] that focus on genomics research. Funds the [AnVIL Project].", 
	furtherreading="https://www.genome.gov/", 
	institute="", 
	pronunciation="", 
	seealso="")

NHLBI = GlossEntry("NHLBI", 
	acronym_full="National Heart, Lungs, and Blood Institute", 
	definition="A division of the [NIH] that focuses on heart, lung, blood, and sleep health. Funds the [BioData Catalyst] platform.", 
	furtherreading="https://www.nhlbi.nih.gov/", 
	institute="", 
	pronunciation="", 
	seealso="")

NIH = GlossEntry("NIH", 
	acronym_full="National Institute of Health", 
	definition="An American government institution, part of the Department of Health and Human Services (HHS), that engages in medical research.", 
	furtherreading="https://www.nih.gov/", 
	institute="", 
	pronunciation="", 
	seealso="")

OICR = GlossEntry("OICR", 
	acronym_full="Ontario Institute for Cancer Research", 
	definition="A non-profit research institute based in Toronto that is focused on cancer detection and treatment. One of the two institutes involved in the development of Dockstore, the other being [UCSC].", 
	furtherreading="https://oicr.on.ca/", 
	institute="", 
	pronunciation="", 
	seealso="")

ORCID = GlossEntry("ORCID", 
	acronym_full="Open Researcher and Contributor ID", 
	definition="ID used to identify researchers and their work in a way that doesn't solely rely on names.", 
	furtherreading="https://info.orcid.org/what-is-orcid/", 
	institute="", 
	pronunciation='"or-kid", rhymes with kid', 
	seealso="")

ParameterFile = GlossEntry("parameter file", 
	acronym_full="", 
	definition="A [JSON] or [YAML] file that describes the inputs to a workflow. This usually includes internal links, or links to data in a Google or S3 bucket.", 
	furtherreading="", 
	institute="", 
	pronunciation='', 
	seealso="")

Preemptible = GlossEntry("preemptible", 
	acronym_full="", 
	definition="A type of [GCP] [VM] which may have its running jobs interrupted at any given time, and will be shut down if running for more than 24 hours. A preemptible machine is significantly cheaper than a standard VM, at the cost of possibly stopping before your computational work is finish. You can use preemptible machines when running workflows on GCP backends to save on compute costs.", 
	furtherreading="https://cloud.google.com/compute/docs/instances/preemptible", 
	institute="Google", 
	pronunciation='', 
	seealso="spot instance")

SevenBridges = GlossEntry("Seven Bridges", 
	acronym_full="", 
	definition="A cloud-based workflow execution platform developed by Seven Bridges Genomics. Seven Bridges supports the execution of [CWL] workflows and features a graph-based GUI to make workflow development easier. The computational backend of a Seven Bridges workspace can be selected by the user, with both [GCP] and [AWS] being supported. Dockstore supports directly importing [CWL] workflows into a Seven Bridges workspace. Seven Bridges is part of the [BioData Catalyst] grant.", 
	furtherreading="https://www.sevenbridges.com/platform/", 
	institute="", 
	pronunciation='', 
	seealso="Terra")

SpotInstance = GlossEntry("Spot Instance", 
	acronym_full="", 
	definition="A type of [EC2] instance which is usually much cheaper than the typical on-demand EC2 cost. A spot instance is not guaranteed to be available at any given time, as it is based upon currently unused EC2 availability.", 
	furtherreading="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html", 
	institute="Amazon", 
	pronunciation='', 
	seealso="preemptible")

TES = GlossEntry("TES", 
	acronym_full="Task Execution Service", 
	definition="A standardized API developed by [GA4GH] for describing and executing batch execution tasks.", 
	furtherreading="https://ga4gh.github.io/task-execution-schemas/docs/", 
	institute="", 
	pronunciation="", 
	seealso="")

Terra = GlossEntry("Terra", 
	acronym_full="", 
	definition="A cloud-based workflow execution platform developed by the Broad Institute. Terra supports the execution of [WDL] workflows, Jupyter/R notebooks, and integrated apps such as a DICOM-file viewer. The computational backend of a Terra workspace is based upon Google, allowing Google-specific features such as [preemptible] machines to be used in workflows. Dockstore supports directly importing [WDL] workflows into a Terra workspace. Terra is part of the [BioData Catalyst], [AnVIL Project], and [eLwazi] grants.", 
	furtherreading="https://terra.bio", 
	institute="", 
	pronunciation="", 
	seealso="Seven Bridges")

Tool = GlossEntry("tool", 
	acronym_full="", 
	definition="A single command line program wrapped in a descriptor language.  Languages that formally describe tools (such as [CWL]) may chain them together into a [workflow].", 
	furtherreading="https://docs.dockstore.org/en/stable/getting-started/intro-to-dockstore-tools-and-workflows.html",
	institute="", 
	pronunciation='', 
	seealso="workflow")

UCSC = GlossEntry("UCSC", 
	acronym_full="University of California, Santa Cruz", 
	definition="A public university located in Santa Cruz that is focused on undergraduate and graduate education and research. The Genomics Institute, a branch of UCSC's engineering department, is one of the two institutes involved in the development of Dockstore, the other being [OICR].", 
	furtherreading="https://ucsc.edu", 
	institute="", 
	pronunciation="", 
	seealso="")

VM = GlossEntry("VM", 
	acronym_full="virtual machine", 
	definition="An emulated computer system that runs on another computer system. Usually implies that an entire operating system(s) (the guest OS) is being run on top of another operating system (the host OS) via the host's hypervisor. The hypervisor manages the execution of processes of the guest operating system. This is in contrast to a [container], which do not involve hypervisors nor run entire guest operating systems.", 
	furtherreading="", 
	institute="", 
	pronunciation='', 
	seealso="container")

WDL = GlossEntry("WDL",
	acronym_full="[Workflow Description Language]",
	pronunciation='"widdle", rhymes with little')

WES = GlossEntry("Workflow Execution Service",
	definition="A standardized API developed by [GA4GH] for describing a standard programmatic way to run and manage workflows.",
	furtherreading="https://ga4gh.github.io/workflow-execution-service-schemas/")

Workflow = GlossEntry("workflow", 
	acronym_full="", 
	definition="A command line program wrapped in a descriptor language, which usually has multiple steps. In [CWL], a workflow is usually made up of multiple tools. Other languages consider a workflow to be the basic unit.", 
	furtherreading="https://docs.dockstore.org/en/stable/getting-started/intro-to-dockstore-tools-and-workflows.html", 
	institute="", 
	pronunciation='', 
	seealso="tool")

Workflow_Description_Language = GlossEntry("Workflow Description Language",
	furtherreading="https://openwdl.org/",
	definition="A workflow language managed by the Open WDL Project that is designed to describe command-line tools. Usually written as [WDL]. WDL and [CWL] are relatively similar in principle, and code written in one language can often be translated into the other with some workarounds, but they are two different standards and each have unique features.",
	seealso="WDL")

YAML = GlossEntry("YAML", 
	acronym_full="YAML Ain't Markup Language", 
	definition="Human-readable data-serialization language. Commonly used for configuration files.", 
	furtherreading="https://yaml.org/", 
	institute="", 
	pronunciation="", 
	seealso="JSON")
