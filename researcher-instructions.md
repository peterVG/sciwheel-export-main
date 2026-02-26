# SciWheel to Wikibase
## Researcher instructions

The following document outlines the process that Researchers must follow to enable consistent capture of citation metadata and transfer of data from [SciWheel](https://sciwheel.com) to the Wikibase deployed at [requirements.landano.io](https://requirements.landano.io)

For technical instructions on exporting Sciwheel data into Wikibase see the [README](https://github.com/landano/sciwheel-export/blob/main/README.md) instructions for this repository.

## Nominate a new Resource
To nominate a new Resource to be added to a SciWheel project collection:
1. Add a Reference record to the INBOX project. 
1. Add a tag with name of the project you think this Resource should be added to.
1. Add a note with reasons on why this Resource should be added.
1. The Editor will check the Reference record for compliance with the guidelines on this page.
1. The Editor will move the Resource to the appropriate collection if approved and add two tags. The first tag asssigned will name the assigned Researcher and the second will be the TODO tag.

## Create a SciWheel Reference record
1. Add as much metadata as possible for each Reference.
1. Add a URL for the Resource source webpage.
1. Add an Abstract for each Resource. Copy verbatim Abstracts from journal articles. Copy and/or paraphrase Prefaces or Introductions from other sources to use as an Abstract.
1. Upload a PDF copy of the Resource if available. 
1. Use the following PDF file name convention: [primary author last name] [double dash] [year of publication] [double dash] [full title with each word seperated by a single dash] e.g. `Baars--2016--Towards-Self-Sovereign-Identity-Using-Blockchain.pdf`
1. If uploading a standard, use the "Report" reference type not "PDF"
1. If uploading a PDF file for a standard, use the following file name convention: [standards body abbreviation] [dash] [Standard Number] [dash] [Year of Publication] [dash] [full title with each word seperated by a dash] e.g. `ISO-10789-2011-Space-systems-Programme-management-information-and-documentation-management.pdf`
1. If uploading standard, name the committee responsible using the Author last name field. Add the name of the standards body as the publisher. If provided, include the day and month of publication in addition to the publication year.

## Capture Quotations from Resources
1. A Researcher will be assigned a Resource for analysis by the Editor using a [`Trello`](https://trello.com/b/iUu7NZ8y/landano-tasks) card. The Editor will add a tag with the Researcher name to the SciWheel Reference record.
1. Upload a copy of the PDF file to the project's [`Google Drive/Resources`](https://drive.google.com/drive/folders/1_oUTGB-AkjfJfx9FeNTEJjKbS_nEUkBp?usp=sharing) folder.
1. If the PDF copy does not support the SciWheel highlighting feature (e.g. in the case of ISO DRM protected PDFs), create a text file transcript of the PDF document using the [`EasyPDF`](https://easypdf.com/pdf-to-text) service. Attach the text file to Reference record using the SciWheel "Supplementary File" feature. Upload a copy of the text file (same naming convention, just with a `.txt` extension) to the Google Drive Resources folder.
1. Read the Resource and use the SciWheel highlighting feature to capture Quotations that state a Requirement or a Definition for a Concept.
1. Add structured markup in the Note associated with each quotation.
1. Ensure that the "shared" option is enabled for the Note and/or highlighed text.
1. Use the following markup structure, wherein the ":" character is the key/value separator and the " | " character is the field separator
  - `section:2.1 | page:12 | definition:archivist`
  - `section:1.5 | page:3 | scope_note:archivist`
  - `section:1.3 | page:45 | requirement:functional | level:mandatory` 
  - `section:chapter 2 | page:233 | statement:fact`
  - `section:2.3 | page:12 | requirement:data | level:optional`
  - `section:4.1 | page:16 | requirement:quality`
  - `section:33 | page:39 | statement:argument`

8. The above structure can be populated with the following key:value types:

**Location**

| Key | Value |
|:---:|:---|
| section: | Can be represented with:<br>    - Numeral (eg section:1.3)<br>    - Cardinal (eg section:Two)<br>    - Ordinal (eg section:First)<br>    - or a combination of expressions (eg section:Chapter One, or section:1.3 Section Header).<br>Entries must match author provided titles when provided. For instances where a resource lacks numeric/ordinal/cardinal codes, but provides textual section/chapter headers, the researcher must introduce numbering themselves so that quotes maintain their order (eg "A New Subsection" becomes "section:1.3 A New Subsection") |
| page: | Preference is given to published page numbers (eg journal articles)<br>as opposed to those assigned by viewing software |

**Text Type**

| Key | Value |
|:---:|:---|
| statement: | - *argument*, a coherent point of view on a given topic presented by the author(s) which is supported by their reasoning and rationale<br>- *fact*, information that can be proven to be true<br>- *proof*, information that corroborates a *fact*<br>- *opinion*, a point of view held by the author(s) on a given topic without corroboration or proof |
| argument: | Two values ("for" or "against") can be used to describe whether the central thesis made by the author supports or challenges ideas, principles, or theses published by the project for which the quotations are being collected |
| definition: | The value after this key is the term being defined by the quoted text |
| requirement: | Three values can be used to identify the type of system requirement being cited:<br>   - functional, describes what a system should be able to do, including features it should offer<br>    - data, escribes the entities, and their named properties or attributes, about which the system should record information (this is a subset of functional requirements)<br>   - quality, places constraints or expectations on a functional requirement (eg performance, scalability, or usability criteria) |

**Context**

| Key | Value |
|:---:|:---|
| quote: | the text directly copied from the resource. This key:value pair is used for instances where the SciWheel highlighting feature does not work and the text must therefore be copied manually |
| level: | Utilized after a requirement:value pair in order to denote its requirement level. Two values can be used:<br>   - optional (ie the system should…)<br>    - mandatory (ie the system must…) |

9. Remove the TODO tag once quotations are captured and add the COMPLETED tag. 
10.  If the Resource has a DRM protected PDF, DO NOT highlight text. Instead use the .txt file to cut-and-paste the quotation into a Note using the following convention: 
  - `section:chapter 3 | page:25 | statement:fact | quote:Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Phasellus faucibus scelerisque eleifend donec pretium vulputate. Morbi tincidunt ornare massa eget egestas.`

## Export Sciwheel Reference records and Notes into Wikibase
See technical instructions in the [README](https://github.com/landano/sciwheel-export/blob/main/README.md) instructions for this repository.

## Enhance the Requirements and Definitions in Wikibase
1. Add editorial and/or housekeeping comments
1. Add tags - once common patterns emerge these can become candidates for structured markup in SciWheel (e.g. "problem statement" -> `statement:problem`, "solution" -> `statement:solution`)
1. Draft System requirement statements that paraphrase and link to one or more requirements quoted in a Resource.
1. Draft Definitions that paraphrase and link to one or more definitions and scope notes quoted in a Resource.
