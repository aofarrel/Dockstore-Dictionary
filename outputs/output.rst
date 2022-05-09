Dockstore Dictionary
====================
.. contents:: Table of Contents
	:local:

.. _dict AnVIL Project:

AnVIL Project
-------------
*abbreviation for* Analysis Visualization and Informatics Labspace  

	A cloud-based ecosystem funded by :ref:`dict NHGRI`, bringing together Dockstore, Gen3, :ref:`dict Terra`, :ref:`dict NCPI`, Galaxy, Jupyter, Seqr, and Bioconductor into an integrated platform. Sometimes refered to as just "the AnVIL" or "AnVIL".  

Further reading: `<https://anvilproject.org/>`_  

.. updated 2022-05-09  



.. _dict BDC:

BDC
---
pronounced "bee-dee-see"  

*abbreviation for* [Biodata Catalyst]  


.. updated 2022-05-09  



.. _dict BDCat:

BDCat
-----
pronounced "bee-dee-cat"  

*abbreviation for* [BioData Catalyst]  


.. updated 2022-05-09  



.. _dict Biodata Catalyst:

Biodata Catalyst
----------------
	An initiative funded by :ref:`dict NHLBI` to connect several cloud-based bioinformatics platforms together to increase reproducibility in bioinformatics. Involves Dockstore, :ref:`dict Terra`, Seven Bridges, Gen3, and PIC-SURE.  

This term as we define it here is associated with NIH and may have different definitions in other contexts.  
Further reading: `<https://biodatacatalyst.nhlbi.nih.gov/>`_  

.. updated 2022-05-09  



.. _dict Cancer Genomics Cloud:

Cancer Genomics Cloud
---------------------
	A cloud platform by :ref:`dict Seven Bridges` and funded by :ref:`dict NCI` for bioinformatics analysis.  


.. updated 2022-05-09  



.. _dict CGC:

CGC
---
*abbreviation for* [Cancer Genomics Cloud]  


.. updated 2022-05-09  



.. _dict CLI:

CLI
---
*abbreviation for* Command Line Interface  

	A program that can be interacted with on the command line, usually via "Terminal" on MacOS and Linux or "cmd"/Command Prompt on Windows. CLI programs generally do not have a graphical user interface.  

Further reading: `<https://en.wikipedia.org/wiki/Command-line_interface>`_  

.. updated 2022-05-09  



.. _dict Common Workflow Language:

Common Workflow Language
------------------------
	A workflow language that describes how to run command-line tools. CWL is based on Java and can use Java commands within its own commands. :ref:`dict WDL` and CWL are relatively similiar in principle, and code written in one language can often be translated into the other with some workarounds, but they are two different standards and each have unique features.  

see also :ref:`dict CWL`  
Further reading: `<https://www.commonwl.org/user_guide/>`_  

.. updated 2022-05-09  



.. _dict Cromwell:

Cromwell
--------
	An open-source :ref:`dict WDL` executor managed by the Broad Institute. Cromwell is the default executor for the :ref:`dict Dockstore CLI` and is the executor used by :ref:`dict Terra`.  

This term as we define it here is associated with Broad Institute and may have different definitions in other contexts.  
Further reading: `<https://cromwell.readthedocs.io/en/stable/>`_  

.. updated 2022-05-09  



.. _dict CWL:

CWL
---
*abbreviation for* [Common Workflow Language]  


.. updated 2022-05-09  



.. _dict DAG:

DAG
---
*abbreviation for* Directed Acyclic Graph  

	A directional graph like a flowchart that does not have any loops. On Dockstore we use DAGs to show the steps that a workflow takes.  

Further reading: `<https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html>`_  

.. updated 2022-05-09  



.. _dict Docker:

Docker
------
pronounced "daw-ker", rhymes with walker  

	A program that can create "images" which are somewhat similiar to virutal machines, as well as run those images. In the context of bioinformatics, this technology has two main benefits: First, a :ref:`dict Docker image` bundles up everything a given piece of software needs to run, meaning that someone who wants to run (for example) samtools via Docker only needs to install Docker, not samtools. Second, an instance of a Docker image is a relatively standardized environment even when running on different backends, meaning that two people running the same software in the same Docker image on two different computers are likely to get the exact same results. In other words, Docker is good for reproducibility and ease of use.  

Further reading: `<https://docker-curriculum.com/>`_  

.. updated 2022-05-09  



.. _dict Docker container:

Docker container
----------------
	In order to actually use the software inside a :ref:`dict Docker image` using the `docker run` command, the Docker program creates a writeable :ref:`dict layer` on top of the image, which leads to the creation of a :ref:`dict Docker container`. You can think of a Docker image as an unchanging template, and a Docker container as a writeable instance generated from that template. A Docker image can exist on its own, but a Docker container requires a Docker image.  

Further reading: `<https://www.docker.com/resources/what-container/>`_  

.. updated 2022-05-09  



.. _dict Docker image:

Docker image
------------
	A read-only file that represents a filesystem that contains some sort of code and that code's depedencies. A Docker image can be created using the `docker build` command in conjunction with a :ref:`dict Dockerfile`. If a workflow language references a Docker image, then the workflow executor will download that Docker image (unless was already downloaded previously) and add a writeable layer onto the Docker image, which results in the creation of a :ref:`dict Docker container`.  


.. updated 2022-05-09  



.. _dict Dockerfile:

Dockerfile
----------
	A file describing the creation of a :ref:`dict Docker image` by running commands that each form a :ref:`dict layer`.  

Further reading: `<https://docs.docker.com/engine/reference/builder/>`_  

.. updated 2022-05-09  



.. _dict Dockstore CLI:

Dockstore CLI
-------------
*abbreviation for* Dockstore Command Line Interface  

	A command-line program developed by Dockstore. It is not required to use Dockstore, but it has many features to make running and developing workflows easier.  

see also :ref:`dict CLI`  
Further reading: `<https://docs.dockstore.org/en/stable/advanced-topics/dockstore-cli/dockstore-cli-faq.html>`_  

.. updated 2022-05-09  



.. _dict DOI:

DOI
---
*abbreviation for* Digital Object Identifier  

	An identifier that provides a long-lasting link to some sort of digital object. On Docktore, you can use Zenodo to mint a DOI of your workflows and tools to increase reproducibility.  


.. updated 2022-05-09  



.. _dict eLwazi:

eLwazi
------
pronounced "el-woz-ee", derived from Xhosa word for knowledge  

	An African-lead open data science platform funded as part of the :ref:`dict NIH`'s :ref:`dict DSI-Africa` program. Leverages :ref:`dict Gen3` and :ref:`dict Terra`.  

Further reading: `<https://elwazi.org/>`_  

.. updated 2022-05-09  



.. _dict GCP:

GCP
---
*abbreviation for* Google Cloud Platform  

	A backend used for cloud computing and cloud storage. Terra is an example of a system that runs on a GCP backend. When running workflows on these backends, make sure to account for the storage needed for your workflow, as GCP compute backends do not automatically scale their storage size at runtime. GCP backends allow you to make use of Google's preemptible feature, which may reduce the cost of running workflows.  

Further reading: `<https://cloud.google.com/gcp>`_  

.. updated 2022-05-09  



.. _dict JSON:

JSON
----
pronounced "jason"  

*abbreviation for* JavaScript Object Notation  

	A human-readible file format that orginated in JavaScript, but is now used by a variety of applications. Dockstore supports the inclusion of JSON and :ref:`dict YAML` files in entries to provide sample inputs for workflow and tool entries. Some workflow executors, such as :ref:`dict Cromwell`, can use these files to configure their inputs rather than having to manually listing every input when calling the workflow on the command line.  

see also :ref:`dict YAML`  
Further reading: `<https://www.json.org/json-en.html>`_  

.. updated 2022-05-09  



.. _dict layer:

layer
-----
	In the context of Docker, a layer is a component of a Docker image. Each `RUN`, `COPY`, and `ADD` instruction in a :ref:`dict Dockerfile` will lead to the creation of a layer.  


.. updated 2022-05-09  



.. _dict NCI:

NCI
---
*abbreviation for* National Cancer Institute   

	A division of the :ref:`dict NIH` focused on cancer research.  


.. updated 2022-05-09  



.. _dict NHGRI:

NHGRI
-----
*abbreviation for* National Human Genome Research Institute  

	A division of the :ref:`dict NIH` that focus on genomics research. Funds the :ref:`dict AnVIL Project`.  

Further reading: `<https://www.genome.gov/>`_  

.. updated 2022-05-09  



.. _dict NHLBI:

NHLBI
-----
*abbreviation for* National Heart, Lungs, and Blood Institute  

	A division of the :ref:`dict NIH` that focuses on heart, lung, blood, and sleep health. Funds the :ref:`dict BioData Catalyst` platform.  

Further reading: `<https://www.nhlbi.nih.gov/>`_  

.. updated 2022-05-09  



.. _dict NIH:

NIH
---
*abbreviation for* National Institute of Health  

	An American government institution, part of the Department of Health and Human Services, that engages in medical research.  

Further reading: `<https://www.nih.gov/>`_  

.. updated 2022-05-09  



.. _dict OICR:

OICR
----
*abbreviation for* Ontario Institute for Cancer Research  

	A non-profit research institute based in Toronto that is focused on cancer detection and treatment. One of the two institutes involved in the development of Dockstore, the other being :ref:`dict UCSC`.  

Further reading: `<https://oicr.on.ca/>`_  

.. updated 2022-05-09  



.. _dict ORCID:

ORCID
-----
pronounced "or-kid", rhymes with kid  

*abbreviation for* Open Researcher and Contributor ID  

	ID used to identify researchers and their work in a way that doesn't solely rely on names.  

Further reading: `<https://info.orcid.org/what-is-orcid/>`_  

.. updated 2022-05-09  



.. _dict Terra:

Terra
-----
	A cloud-based workflow execution platform developed by the Broad Institute. Terra supports the execution of :ref:`dict WDL` workflows, Jupyter/R notebooks, and integrated apps such as a DICOM-file viewer. The computational backend of Terra is based upon Google, allowing Google-specific features such as :ref:`dict preemptible` machines to be used in workflows. Dockstore supports directly importing :ref:`dict WDL` workflows into a Terra workspace. Terra is part of the :ref:`dict BioData Catalyst`, :ref:`dict AnVIL Project`, and :ref:`dict eLwazi` grants.  

Further reading: `<https://terra.bio>`_  

.. updated 2022-05-09  



.. _dict TES:

TES
---
*abbreviation for* Task Execution Service  

	A standardized API developed by :ref:`dict GA4GH` for describing and executing batch execution tasks.  

Further reading: `<https://ga4gh.github.io/task-execution-schemas/docs/>`_  

.. updated 2022-05-09  



.. _dict UCSC:

UCSC
----
*abbreviation for* University of California, Santa Cruz  

	A public university located in Santa Cruz that is focused on undergraduate and graduate education and research. The Genomics Institute, a branch of UCSC's engineering department, is one of the two institutes involved in the development of Dockstore, the other being :ref:`dict OICR`.  

Further reading: `<https://ucsc.edu>`_  

.. updated 2022-05-09  



.. _dict WDL:

WDL
---
pronounced "widdle", rhymes with little  

*abbreviation for* [Workflow Description Language]  


.. updated 2022-05-09  



.. _dict Workflow Description Language:

Workflow Description Language
-----------------------------
	A workflow language managed by the Open WDL Project that is designed to describe command-line tools. Usually written as :ref:`dict WDL`. WDL and :ref:`dict CWL` are relatively similiar in principle, and code written in one language can often be translated into the other with some workarounds, but they are two different standards and each have unique features.  

see also :ref:`dict WDL`  
Further reading: `<https://openwdl.org/>`_  

.. updated 2022-05-09  



.. _dict YAML:

YAML
----
*abbreviation for* YAML Ain't Markup Language  

	Human-readable data-serialization lanaguage. Commonly used for configuration files.  

see also :ref:`dict JSON`  
Further reading: `<https://yaml.org/>`_  

.. updated 2022-05-09  



