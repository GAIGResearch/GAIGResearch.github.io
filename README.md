# GAIGResearch.github.io usage information

To update website, clone repository. Any changes made which are pushed to the master branch will show up on the website. Pushing changes to master will cause the entire website to be rebuilt (errors in compiling would be sent to the email registered with this account).

To test locally, install [Jekyll](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll), navigate to the repository's root folder and run command 'jekyll s'. This should start a server and you can navigate to `http://localhost:4000` to see your local version. Any changes made to files in the repository will be automatically updated (and the site rebuilt) locally while the server is running, unless the _config.yml file is modified (the server should be restarted then).

## Creating new posts:

To add a new post, simply create a new markdown (.md) file in `GAIGResearch.github.io/_posts` directory. 

**The file's name MUST follow the format `YYYY-MM-DD-fname.md`.** The `fname` part in the file name is not used (but should make it different to others). The first part is used to determine the date of the post (most recent posts are displayed first in the home page).

**The file MUST contain a front matter at the top of the file. Required fields are 'layout' and 'title'.** Full field options:

```
---
layout: post
title: Title of post
categories: [category1, category2]
tags: [tag1, tag2]
excerpt: "Shorter paragraph to be displayed rather than the entire post (the rest is displayed when users click 'Read More')."
mathjax: false
---
```

mathjax can be used to insert nicely formatted math into markdown (set to true if using math). To display a table of contents on the right side, created automatically from the headings included, add the following to your file:

```
* content
{:toc}
```

Anything else following will be considered content and displayed in markdown. The post will be automatically added on the website. Any posts removed from the folder will also be removed from the website. Any posts can also be modified by modifying their corresponding files.

## Adding new members:

To add a new member, create a new markdown (.md) file in the `GAIGResearch.github.io/_members` directory (no naming convention for files).

**The file MUST include a front matter at the top of the file. Recquried fields are: 'layout', 'permalink', 'title', 'img', 'job', 'job-type' and 'year' (for students only).** Please use only supported job-types (student, staff, external). Full list of supported fields:

```
---
layout: member
permalink: relative link through which the profile should be accessed (e.g. /members/Raluca-Gaina)
title: display name for member
img: relative path to image of member (e.g. /img/ralucagaina.png)
job: job title (e.g. PhD student / Lecturer)
year: phd student current year
job-type: options are student, staff or external
email: email address
web: link to website, including http://
twitter: twitter handle (e.g. b_gum22)
linkedin: name as included in profile link (e.g. raluca-gaina-347518114)
gscholar: user id as included in profile link (e.g. tC5klQYAAAAJ)
researchgate: name as included in profile link (e.g. Raluca_Gaina)
orcid: orcid ID
github: username (e.g. rdgain)
---
```

The rest of the file can contain any information the member wishes displayed on their profile (e.g. biography, research, other links). Any files can be modified to change information about members. Files can be deleted to remove member from the website.

## Adding new publications:

Publications are displayed in the `/publications` tab on the website and automatically compiled from the `GAIGResearch.github.io/_data/papers.yml` file to generate the list grouped by year.

There are 2 ways to add new publications. 

### Directly (not recommended)

* Modify the file `GAIGResearch.github.io/_data/papers.yml` directly to add a new publication following the format in file. 
* All fields supported by bibtex are also supported in this file. 
* If a field value contains ':', the whole field value must be included in double quotes ("...").
* Be careful to avoid duplications and any publications older than the group's start year (2017).

### Via Python3 script (recommended)

This option requires Python3 to be installed (base packages requried only). It is an automated process with validity checks included.

1. Place any bibtex (.bib) files you wish to include in the publications in the `GAIGResearch.github.io/bibfiles` directory (one file may contain multiple bibtex entries, no requirements as to naming conventions).
2. Run `bib_processing.py` script (found in root directory). This will process all bibtex entries in the files found in the previously specified directory, format them correctly and add them to the `GAIGResearch.github.io/_data/papers.yml` file. Duplicates are checked for and ignored. Publications older than the group's start year (2017) are also ignored.
3. Rebuild website (or push the new `papers.yml` file into the repository).
