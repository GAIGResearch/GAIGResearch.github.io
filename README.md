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
img: path to title image
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

Publications are displayed in the `/publications` tab on the website. The list is generated from files in the `_posts/papers` folder, where each paper has its own file with paper meta-data.

To add a new publication, **create** a new file in the `_posts/papers` folder.

### Features
- Publications require only front matter base information to be added in a new file.
- Publications have an associated post page automatically created, which can be left empty, or can be accompanied by a blog post.
- Tagged publications are sorted by tags the `/tag` page on the website. We recommend including the conference abbreviation as a tag.
- Publications are listed on the main publications page, sorted by year, and tagged by venue.
- Publications are also automatically added to GAIG member's profile if an author.
- Authors on a publications who are GAIG members have their profile automatically linked from the author list.

### File name

The name of the file follows typical post guidelines, requiring the format `YYYY-MM-DD-paperID.md`. The date is used to sort papers - generally, only the year is relevant.

The **paperID** is recommended to be the Bibtex paper ID, usually the last name of the first author, the year of publication and the first word in the paper title, e.g. gaina2020rolling. The paperID format is not checked at any point and can be different, this is just guideline.

### File contents

**The file MUST include a front matter at the top of the file.** Required fields are the following (you can simply copy this base template into a new file to ensure you're respecting the correct format):

```aidl
---
layout: post
categories: Publications
paper: true
hidden: true

pubid: {your paperID}
type: {your publication type, the tag after @ in Bibtex citations, e.g. article, inproceedings, book etc.}
title: {your paper title}
author: {your paper authors, names separated by keyword 'and' with spaces on each side}
year: {year of publication}
---

* content
{:toc}
```

**IMPORTANT:** authors should be separated by keyword ' and ', with the spaces on either side. This is the typical format given by Bibtex citations. If not respected, the authors which are members of GAIG will not have their profiles automatically linked in the author list. If the name deviates much from that used on the website, this linking will also fail.

After this base information, anything else can be added in the file in markdown format, which will be displayed on the publication's post page (e.g. blog post, custom links, images, videos, tables, results etc.).

**Bibtex fields supported:** All fields included in Bibtex citations are supported. You can simply copy-paste a Bibtex citation into the front matter, then replace '={' with ': ' (the space after is important), and remove '},' at the end of each field, as well as other braces included. **IMPORTANT:** If your text in a field includes a colon symbol (':'), then everything should be surrounded by double quotes. If your text in the double quotes includes any other double quotes, replace those inside with single quotes to avoid compilation errors.
- **url**: use field name **puburl** instead, as url is already a keyword in Jekyll and it causes errors. If included, link is added on the publication's post page.
- **keywords**: we recommend duplicating the list of keywords in the tags field (with dashes, '-', replacing spaces between words)
- **journal**, **booktitle**, **volume**, **number**, **series**, **edition**, **chapter**
- **month**, **timestamp**
- **pages**
- **editor**, **publisher**, **address**, **howpublished**
- **organization**, **school**, **institution**
- **eprint**, **archivePrefix**
- **bibsource**, **biburl**, **doi**, **issn**, **isbn**, **note**, **abstract**



**Other fields supported:**
- **venue**: if specified, this adds a tag before the paper year and title in the display. Currently supported venue options (not case sensitive): 
    - IEEE COG 
    - EVOSTAR
    - IEEE TOG
	- IEEE TEVC
    - IEEE CEC
    - FDG
    - AAMAS
    - DIGRA
    - CEEC
    - ICCC
    - AIIDE
    - IWAI
    - GECCO
	- SSCI
    - EXAG
    - STRATEGY AIIDE
    - AAAI
    - CIML
    - GAMES AAAI
    - PHD
    - BOOK
- **img**: if specified, adds a banner-type crop of the image linked at the top (path relative to root folder required)
- **smallimg**: if specified, adds a small portrait-size crop of the image linked in the top-right (path relative to /img/posts/ required)
- **tags**: if specified, the paper will be tagged and matched to other papers with the same tags (found in `/tag` page on the website, or by clicking any tags)
- **arxiv**: if specified, link is added in the paper's post page.
- **pdf**: if specified and set to true, PDF existing on the website is linked automatically on paper's post page. PDF must be in folder `/pdf/` and have the same name as the paperID.
- **repo**: if specified, links on paper's post page to the Github repository containing code associated with the publication.
- **note**: if specified, note is displayed on paper's post page.PDF existing on the website is linked automatically on paper's post page. PDF must be in folder `/pdf/` and have the same name as the paperID.
- **issn, isbn, doi**: if specified, details added on paper's post page.
- **talkpdf**: if specified and set to true, PDF of presentation associated with publication, which exists on the website, is linked automatically on paper's post page. PDF must be in folder `/pdf/` and have the name format `paperID-talk.pdf`.
- **talkppt**: if specified and set to true, PPTX of presentation associated with publication, which exists on the website, is linked automatically on paper's post page. PPTX must be in folder `/ppt/` and have the name format `paperID.pptx`.
- **youtube**: if specified, link is added in the paper's post page.

## Adding new pages:

To add a new page, create a new markdown (.md) or HTML (.html) file in the `GAIGResearch.github.io/page` directory. The name of the file will become its path, relative from root website (unless 'permalink' field is specified in the front matter).

**The file MUST include a front matter at the top of the file. Recquried fields are: 'layout', 'title', 'permalink'.** If the field 'type: page' is specified, the page will be displayed in the header menu (top-right of website), otherwise it will only be accessible by link. Full list of supported fields:

```
---
layout: page
title: name of page
permalink: relative link to page (i.e. /archive/)
icon: fontawesome icon name (e.g. calendar)
type: page (if this field is not defined, the page will not be included in the header, but can be linked from other pages).
---
```

A range of icons are supported and used throughout the site and more are available here: https://fontawesome.com. To use such an icon in a markdown or html file, include the following code:

```
<i class="fas fa-icon"></i>
```

Replace "icon" in the above with the name of the icon, as given on https://fontawesome.com. If it is a brand icon you're using (i.e. github), the code should instead be:

```
<i class="fab fa-icon"></i>
```

With the "icon" text replaced with the name of the icon, as before.

