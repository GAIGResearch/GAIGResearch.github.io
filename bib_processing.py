import os


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


def find_all_files(path_to_search):
    """Recursively find all bib files in root path given"""
    list_of_files = os.listdir(path_to_search)
    all_files = []
    # Iterate over all the entries
    for e in list_of_files:
        # Create full path
        full_path = os.path.join(path_to_search, e)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + find_all_files(full_path)
        elif full_path.endswith(".bib"):
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
    return os.path.isfile("pdf/pub/" + year + "/" + entry_id + ".pdf")


def format_entry(entry):
    """
    Prints the given bibtex entry into yaml supported format
    :param entry
    """
    with open("output.yml", 'a+') as wf:
        wf.write("-   id: " + entry["id"] + "\n")
        for e in entry:
            if e != "id":
                if ":" in entry[e]:
                    entry[e] = '"' + entry[e] + '"'
                wf.write("    " + e + ": " + entry[e] + "\n")


def main():
    """
    Main function to process bibtex entries in a given path and output a file in yaml supported format.
    """
    path = "bibfiles"
    files = find_all_files(path)
    abs_path = os.path.abspath(os.path.dirname(__file__))

    entries = []
    for bibfile in files:
        entry = ""
        full_pth = os.path.join(abs_path, bibfile).replace("\\", "\\\\")
        try:
            with open(full_pth) as f:
                lines = f.readlines()
                line_number = 0
                for line in lines:
                    if "@" in line or line_number == len(lines)-1:  # Starting a new entry
                        if entry != "":
                            entries.append(entry)
                        entry = ""
                    if "@" in line:
                        line = line.replace("{", "=")
                    stripped_line = line.strip()
                    if stripped_line != "":  # Adding to current entry
                        if stripped_line.endswith(","):
                            stripped_line = stripped_line[:-1]
                        entry += stripped_line + "\n"
                    line_number += 1
        except:
            print("File " + full_pth + " not found.")

    for entry in entries:
        entry = entry.translate({ord(c): None for c in '\\"{}~\''})
        processed_entry = process_entry(entry)
        format_entry(processed_entry)


if __name__ == "__main__":
    main()
