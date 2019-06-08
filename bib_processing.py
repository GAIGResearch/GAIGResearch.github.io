import os
from pathlib import Path
from difflib import SequenceMatcher


supported_bibtex_types = {"article", "book", "booklet", "inbook", "incollection", "inproceedings", "manual",
                          "mastersthesis", "misc", "phdthesis", "proceedings", "techreport", "unpublished"}

supported_fields = ["author", "title", "year", "month", "pages", "note",
                    "journal", "booktitle",
                    "volume", "number", "series", "edition",
                    "editor", "publisher", "address",
                    "howpublished", "type",
                    "chapter",
                    "organization", "school", "institution"]

extra_fields = ["doi", "issn", "isbn", "keywords", "abstract", "url", "archivePrefix", "eprint", "timestamp", "biburl",
                "bibsource"]

data_path = Path("_data/papers.yml")
bib_path = Path("bibfiles")
year_from = 2017
similarity_threshold = 0.8


def find_all_files(path_to_search):
    """Recursively find all bib files in root path given"""
    list_of_files = os.listdir(path_to_search)
    all_files = []
    # Iterate over all the entries
    for e in list_of_files:
        # Create full path
        full_path = path_to_search / e
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + find_all_files(full_path)
        elif full_path.with_suffix(".bib"):
            all_files.append(full_path)

    return all_files


def process_entry(entry_to_process):
    """
    Turns a string of an entry into a dictionary mapping from fields to field values
    :param entry_to_process
    :return: dictionary.
    """
    dict_entry = {}
    entry_lines = entry_to_process.split("\n")
    first_line = entry_lines[0].split("=")

    entry_type = first_line[0].replace("@", "")
    entry_id = first_line[1]

    # Type validation
    if entry_type.lower() not in supported_bibtex_types:
        print("Type " + entry_type + " not supported for bibtex entry " + entry_id)
        return dict_entry

    dict_entry["id"] = entry_id
    dict_entry["type"] = entry_type

    # Process the rest of the fields
    field_value = ""  # Keep this up here to be able to access previous values in case of multi-line field
    field = ""
    for l in entry_lines:
        split_line = l.split("=")
        if len(split_line) == 1 and field != "":  # No = found on this line, it's a multi-line field
            field_value += " " + split_line[0].strip()
            dict_entry[field] = field_value.strip()
        else:
            field = split_line[0].strip()
            field_value = split_line[1].strip()
            if field.lower() in supported_fields or field.lower() in extra_fields:
                if field.lower() == "pages" and "--" not in field_value:
                    field_value = field_value.replace("-", "--")
                dict_entry[field] = field_value

    # Try to find pdf of this paper
    pdf = find_pdf(entry_id, dict_entry["year"])
    dict_entry["pdf"] = str(pdf).lower()

    return dict_entry


def find_pdf(entry_id, year):
    """
    Returns true if a pdf for this paper exists in the pdf/pub/year directory (must have name as paper ID)
    """
    return os.path.isfile("pdf/pub/" + year + "/" + entry_id + ".pdf")


def output_entries(entries):
    """
    Prints the given bibtex entries into yaml supported format
    """
    with open(data_path.absolute(), 'w+', encoding='utf-8') as wf:
        for entry in entries:
            if int(entry["year"]) < year_from:
                continue
            wf.write("-   id: " + entry["id"] + "\n")
            for e in entry:
                if e != "id":
                    if ":" in entry[e]:
                        entry[e] = '"' + entry[e] + '"'
                    wf.write("    " + e + ": " + entry[e] + "\n")


def check_equality(entry1, entry2):
    """
    Checks if 2 entries are the same
    """
    sim_fields = 0
    common_fields = 0
    for field1 in entry1:
        for field2 in entry2:
            if field1 == field2:
                common_fields += 1
                if similar(entry1[field1], entry2[field2]) >= similarity_threshold:
                    sim_fields += 1
    if common_fields == 0:
        return False
    if sim_fields / common_fields >= similarity_threshold:
        return True
    return False


def similar(a, b):
    """
    Checks if 2 strings are similar, returns a similarity measure.
    """
    return SequenceMatcher(None, a, b).ratio()


def process_yml_entries(lines):
    """
    Processes entries in yml format
    :param lines: list of lines from yml file to process
    :return: list of entries as dictionaries
    """
    entry_list = []
    entry = {}
    ln = 0
    for line in lines:
        if "-   id:" in line or ln == len(lines) - 1:  # Starting a new entry
            if len(entry) > 0:
                entry_list.append(entry)
            entry = {}
        line = line.replace("\"", "")
        if "-   id:" in line:
            line = line[1:]  # Ignore first dash
        stripped_line = line.strip()
        if stripped_line != "":  # Adding to current entry
            split_line = stripped_line.split(':')
            entry[split_line[0].strip()] = ':'.join(split_line[1:]).strip()
        ln += 1
    return entry_list


def main():
    """
    Main function to process bibtex entries in a given path and output a file in yaml supported format.
    """
    # Read in current entries
    lines = data_path.read_text(encoding='utf-8').split('\n')
    entries = process_yml_entries(lines)

    # Find new entries
    files = find_all_files(bib_path)

    for bibfile in files:
        entry = ""
        full_pth = Path(bibfile)
        lines = full_pth.read_text(encoding='utf-8').split('\n')
        line_number = 0
        for line in lines:
            if "@" in line or line_number == len(lines)-1:  # Starting a new entry
                if entry != "":
                    entry = entry.translate({ord(c): None for c in '\\"{}~\'"'})
                    processed_entry = process_entry(entry)
                    entries.append(processed_entry)
                entry = ""
            if "@" in line:
                line = line.replace("{", "=")
            stripped_line = line.strip()
            if stripped_line != "":  # Adding to current entry
                if stripped_line.endswith(","):
                    stripped_line = stripped_line[:-1]
                entry += stripped_line + "\n"
            line_number += 1

    # Check for duplication
    duplicate_entries = []
    for i in range(len(entries)-1):
        for j in range(i+1, len(entries)):
            if check_equality(entries[i], entries[j]):
                print("Duplicate found: " + entries[i]["id"] + " = " + entries[j]["id"])
                duplicate_entries.append(j)
    duplicate_entries.sort()
    for i in range(len(duplicate_entries)):
        e = duplicate_entries[i] - i
        del entries[e]

    # Finally, save entries
    output_entries(entries)


if __name__ == "__main__":
    main()
