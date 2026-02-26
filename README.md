# sciwheel-export
This script will connect to Sciwheel and export References and Notes to a JSON file that you can
then use to map the data into another resource.

## See also: Researcher instructions
Instructions for Researchers using this `sciwheel-export` script to prepare citations and notes for import into Wikibase are provided on the [Researcher Instructions](https://github.com/landano/sciwheel-export/blob/main/researcher-instructions.md) page.

# Getting started

## Running this code...

sciwheel-export is a Python script. Clone this repository as follows:

* `git@github.com:landano/sciwheel-export.git`

Install the requirements:

* `python -m pip install -r requirements/requirements.txt`

From the root of the repository you can run:

* `python sciwheelexport.py`

You will be presented with an `OSError`. Follow the next steps to get up and
running with your exports.

## Next steps

* Create an environment variable or .env file containing `SCIWHEEL_TOKEN=`
which is your bearer token for the Sciwheel API.
> **Note:** If you are logged into Sciwheel it should be located at:
[User->Account->External API][API-1].
* Run `sciwheel.py` again.
* You will be shown a list of projects for which you are a member.
> E.g. `select a project number: {1: ('Arkly', '680802'), 2:
('Orcfax', '685232'), 3: ('Your publications', '685485')}`
* Select the number that you want to export references + annotations for.
* An export file (JSON) is created with the naming convention:
`sciwheel-project-{project}-{project-ID}-{timestamp}-export.json`
> E.g. `sciwheel-project-Arkly-680802-20220719212026-export.json`


# How it works

The code will:

1. Query the projects for which you are a member.
2. Return the references for that project.
3. For each reference, identify if there are any annotations.
4. For each record with an annotation, download the annotation record.
5. Create a new list field for all records with annotations and add the notes
records.

# Sciwheel API documentation

* [Sciwheel API][API-2]

# Examples in cURL

## get project example:

```curl
curl -s "https://sciwheel.com/extapi/work/references?projectId="680802"" \
    -H "Accept: application/json" \
    -H "Authorization: Bearer {bearer token}" \
    | jq
```

**Output sample**

```json
{
  "total": 6,
  "results": [
    {
      "id": "12380355",
      "type": "BOOK",
      "pubMedId": null,
      "doi": null,
      "pmcId": null,
      "title": "Archives: principles and practises",
      "abstractText": null,
      "publicationDate": "2017",
      "publishedYear": 2017,
      "volume": null,
      "issue": null,
      "pagination": null,
      "journalName": null,
      "journalAbbreviation": null,
      "authorsText": "Millar L",
      "fullTextLink": null,
      "pdfUrl": null,
      "pdfSize": null,
      "f1000Recommended": false,
      "f1000Bookmarked": false,
      "f1000Incomplete": false,
      "f1000NotesCount": 0,
      "f1000AddedBy": "Peter Van Garderen",
      "f1000AddedDate": 1658164797130,
      "f1000RecommendationsCount": 0,
      "f1000Tags": [],
      "pubmedCitationsCount": null
    },
```

## get reference example:

```curl
curl -s "https://sciwheel.com/extapi/work/references/13332938" \
    -H "Accept: application/json" \
    -H "Authorization: Bearer {bearer token}" \
    | jq
```

**Output sample**

```json
{
  "id": "13332938",
  "type": "MANUAL_ITEM_PDF",
  "pubMedId": null,
  "doi": null,
  "pmcId": null,
  "title": "ISO 10789: 2011 - Space Systems — Programme Management — Information and Documentation Management",
  "abstractText": null,
  "publicationDate": null,
  "publishedYear": null,
  "volume": null,
  "issue": null,
  "pagination": null,
  "journalName": "",
  "journalAbbreviation": null,
  "authorsText": "",
  "fullTextLink": null,
  "pdfUrl": "https://d2aexfmej97h8w.cloudfront.net/r1333/13332938/10789-pdf-5f663a4f-2fc3-4177-8af6-8efb3109e2a8.pdf?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDJhZXhmbWVqOTdoOHcuY2xvdWRmcm9udC5uZXQvcjEzMzMvMTMzMzI5MzgvMTA3ODktcGRmLTVmNjYzYTRmLTJmYzMtNDE3Ny04YWY2LThlZmIzMTA5ZTJhOC5wZGYiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NTgyNDQwNjB9LCJEYXRlR3JlYXRlclRoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1NzYzODk2MH19fV19&Signature=jlEx~uhv1IAot7~432aA5rTQUPT1wbiznW0J8LUIhmf4GXvNxoGsQ2oqBC-yv8~pwP8CbOKTakCh2hBxUPSk396qH~9XkXXUNcc9gF~HAeYt37dy~hV4IcWTn4N0adsstBZ0diwhvShkNhh2DkGsHvqpYbdZovPETE49znhVSZiPfEWfbJMlJfFU9qEXRGKAeVXOY8OCvM6Q7BqVv~~ETabs86xIYctj4ZjDQmVRymV7NyS-M6QfEX-F~CLgQ2721vM1kbtSminSyfNI45Nu6-j~NsAiiX8cqj2iidUraM5nlx6nTtJbaUg8tbVlhkPq3Vx2z8cjqkCQASB~TxvycQ__&Key-Pair-Id=KCSK5VUJBIQEU",
  "pdfSize": "1379403",
  "f1000Recommended": false,
  "f1000Bookmarked": false,
  "f1000Incomplete": false,
  "f1000NotesCount": 29,
  "f1000AddedBy": "Özhan Saglik",
  "f1000AddedDate": 1658164797108,
  "f1000RecommendationsCount": 0,
  "f1000Tags": [],
  "pubmedCitationsCount": null
}
```

## get notes example:

```curl
curl -s "https://sciwheel.com/extapi/work/references/13332938/notes" \
    -H "Accept: application/json" \
    -H "Authorization: Bearer {bearer token}" \
    | jq
```

**Output sample**

```json
  {
    "id": "8100993",
    "user": "Christian Koch",
    "comment": "Pg. 12",
    "highlightText": "Information/documentation shall be protected against environmental and accidental risks and against   unauthorized access.",
    "replies": [],
    "created": 253972,
    "updated": null,
    "url": "https://sciwheel.com/work/item/13332938/resources/14808836/pdf"
  },
  {
    "id": "8100991",
    "user": "Christian Koch",
    "comment": "guarantee of authenticity, guarantee of non-repudiation, guarantee of confidentiality (limited), guarantee of data integrity. Pg. 12",
    "highlightText": "delivery mechanism shall ensure",
    "replies": [],
    "created": 254005,
    "updated": null,
    "url": "https://sciwheel.com/work/item/13332938/resources/14808836/pdf"
  },
```

[API-1]: https://sciwheel.com/work/#/profile/externalAPI/
[API-2]: https://sciwheel.com/resources/Sciwheel_API_documentation.pdf
