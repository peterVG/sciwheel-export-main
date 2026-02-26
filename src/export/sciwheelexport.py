"""Sciwheel-export script

How it works:

    1. Query the projects for which you are a member.
    2. Return the references for that project.
    3. For each reference, identify if there are any annotations.
    4. For each record with an annotation, download the annotation
       record.
    5. Create a new list field for all records with annotations and add
       the notes records.

    The result is a modified Sciwheel record containing references +
    annotations. This can then be mapped into other systems.

Output:

    An export file (JSON) is created with the naming convention:

       * sciwheel-project-{project}-{project-ID}-{timestamp}-export.json

"""

import datetime
import json
import os
import sys

import requests
from dotenv import load_dotenv


class SciwheelexportException(Exception):
    """Exception for errors connecting to Sciwheel."""


def get_bearer_token() -> str:
    """Access local ENV and return a configured bearer token for
    Sciwheel - the API "bearer" token.
    """
    load_dotenv()
    return os.getenv("SCIWHEEL_TOKEN")


def _make_request(
    url: str, bearer: str, params: dict = {}, debug: bool = False
) -> dict:
    """Make a request to a given URL and return the response"""
    headers = {
        "Authorization": f"Bearer {bearer}",
        "Accept": "application/json",
        "User-Agent": "landano-sciwheel-export/0.1",
    }
    resp = requests.get(url, headers=headers, params=params)
    if debug:
        print(url, headers, params, file=sys.stderr)
    try:
        return resp.json()
    except requests.exceptions.JSONDecodeError as err:
        msg = f"Resp: {resp}, err {err}"
        raise SciwheelexportException(msg)
    return {}


def get_projects(bearer: str) -> list:
    """Return a dictionary of projects from Sciwheel.

    Example cURL:

        curl -s "https://sciwheel.com/extapi/work/projects" \
            -H "Accept: application/json" \
            -H "Authorization: Bearer {bearer token}" \
            | jq
    """
    projects_url = "https://sciwheel.com/extapi/work/projects/"
    projects = _make_request(projects_url, bearer)
    try:
        projects = {
            idx: (project["name"], project["id"])
            for idx, project in enumerate(projects.get("results", []), 1)
        }
    except IndexError:
        return []
    return projects


def get_project(projects: dict) -> tuple:
    """Return a project value to export from Sciwheel from user input."""
    project_number = input(f"select a project number: {projects}\n")
    print(f"User entered: {project_number}", file=sys.stderr)
    try:
        project_number = int(project_number)
    except ValueError:
        project_number = 0
    return projects.get(project_number, 0)


def add_annotations(annotated: dict, bearer: str) -> dict:
    """Retrieve references for a given ID.

    Example cURL:

        curl -s "https://sciwheel.com/extapi/work/references/13332938/notes" \
            -H "Accept: application/json" \
            -H "Authorization: Bearer {bearer token}" \
            | jq
    """
    annotated_url = "https://sciwheel.com/extapi/work/references/{}/notes"
    notes_arr = {}
    for id_ in annotated:
        url = annotated_url.format(id_)
        resp = _make_request(url, bearer)
        notes_arr[id_] = resp
    return notes_arr


def get_project_refs(selection: tuple, bearer: str) -> list:
    """Get references included in a Sciwheel project

    Example cURL:

        curl -s "https://sciwheel.com/extapi/work/references/13332938" \
            -H "Accept: application/json" \
            -H "Authorization: Bearer {bearer token}" \
            | jq
    """
    print(
        f"Retrieving references for: {selection[0]} ({selection[1]})", file=sys.stderr
    )
    refs_url = "https://sciwheel.com/extapi/work/references"
    params = {"projectId": int(selection[1])}
    refs = _make_request(refs_url, bearer, params=params)
    notes_field = "f1000NotesCount"
    id_field = "id"
    results = refs.get("results", [])
    annotated = []
    for res in results:
        if not res.get(notes_field, ""):
            continue
        annotated.append(res.get(id_field))
    notes_arr = add_annotations(annotated, bearer)
    all_refs = []
    for res in results:
        if res.get(id_field, "") not in notes_arr:
            all_refs.append(res)
            continue
        res["notes"] = notes_arr[res.get(id_field)]
        all_refs.append(res)
    return all_refs


def export_sciwheel() -> None:
    """Export data from Sciwheel"""
    bearer = get_bearer_token()
    if not bearer:
        raise EnvironmentError("Set SCIWHEEL_TOKEN in your environment or .env file")
        return
    projects = get_projects(bearer)
    selection = get_project(projects)
    if not selection:
        sys.exit("Exiting: No project, or no valid-project selected")
    all_refs = get_project_refs(selection, bearer)
    timestamp = "{:%Y%m%d%H%M%S}".format(datetime.datetime.now())
    filename = f"sciwheel-project-{selection[0]}-{selection[1]}-{timestamp}-export.json"
    print(f"Export output to: {filename}", file=sys.stderr)
    with open(filename, "w") as res:
        res.write(json.dumps(all_refs, indent=2, sort_keys=True))


def main() -> None:
    """Primary entry point for this script."""
    export_sciwheel()


if __name__ == "__main__":
    main()
