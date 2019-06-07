---
layout: page
title: Publications
permalink: /publications/
icon: archive
type: page
---

* content
{:toc}

<div style="clear:both">
	{% for paper in site.data.papers %}
		<div class="bibblock">
			<p>
				{{ paper.authors }},
				"{{ paper.title }}",
				in <em>{{ paper.journal }}</em>,
				{{ paper.year }},
				{% if paper.volume %} <strong>{{ paper.volume }}</strong>,{% endif %}
				{% if paper.pages %} pp. {{ paper.pages }}{% endif %}.
			</p>
			
			{% if paper.doi %}
				<a href="http://dx.doi.org/{{ paper.doi }}">[DOI]</a>
			{% endif %}
			
			{% if paper.pdf == true %}<a href="/pdf/{{ paper.year }}/{{ paper.id }}.pdf">[PDF]</a>{% endif %}

			{% if paper.abstract %}
				<a data-toggle="collapse" href="javascript:toggleDiv('{{paper.id}}-abstract')">[Abstract]</a>
			{% endif %}

			<a data-toggle="collapse" href="javascript:toggleDiv('{{paper.id}}-bibtex')">[BibTeX]</a>
			
			<div id="{{paper.id}}-abstract" style="display:none;padding-left:50px;" class="collapse"><h4>Abstract</h4>{{paper.abstract}}</div>
			<div id="{{paper.id}}-bibtex" style="display:none;padding-left:50px;" class="collapse"><h5>BibTex</h5>bibtex</div>
		</div>
	{% endfor %}
</div>


## Comments

{% include comments.html %}
