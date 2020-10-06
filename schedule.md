---
layout: default
img: artsrouni
img_link: http://www.hutchinsweb.me.uk/IJT-2004.pdf
caption: "Georges Artsrouni's mechanical brain, a translation device patented in 1933 in France."
title: Syllabus
active_tab: syllabus
---

## Schedule

The schedule is preliminary and subject to change.

<style type="text/css">
    .bs-example{
        margin: 20px;
    }
</style>

<div class="bs-example">
    <div class="panel-group" id="accordion">
        <table>
        <thead><tr>
          <th>Date</th>
          <th>Topic</th>
          <th>Assignments</th>
          <th>Readings</th>
        </tr></thead>
        <tbody>  
        {% for week in site.data.schedule %}
          {% for date in week.dates %}
            <tr {% if date.noclass %}class="noclass"{% endif %}>
              <td>{{ date.date }}</td>
              <td>
                {% if date.noclass %}
                  {{ date.title }}
                {% elsif date.title %}
                 Lecture: {{ date.title }} <br/>
                  {% if date.leclinks %}
                    {% for link in date.leclinks %}
                      [<a href="{{link.url}}">{{link.name}}</a>]
                    {% endfor %}
                    <br/>
                  {% endif %} 
                  {% if date.tutorial != null %}
                    Tutorial: {{ site.tutorials[date.tutorial].title }}<br/>
                    {% if date.tutlinks %}
                      {% for link in date.tutlinks %}
                        [<a href="{{link.url}}">{{link.name}}</a>]
                      {% endfor %}
                      <br/>
                    {% endif %} 
                  {% endif %}
                {% endif %}
              </td>
              <td>
                {% if date.hwdue %}
                  Due: <a href="{{site.baseurl}}/hw{{date.hwdue}}.html">HW{{ date.hwdue }}</a><br/>
                {% endif %}
                {% if date.project %}
                  Due: {{ date.project }}<br/>
                {% endif %}
              </td>
              {% if date.skipread %} 
              {% else %}
                 {% if date.keepread %}
                   {% assign keepread = date.keepread %}
                {% else %} 
                   {% assign keepread = 1 %} 
                {% endif %}
              <td rowspan="{{ keepread }}">
                {% if date.lecture %}
                  {% assign lectures = site.data.syllabus | where: "tag", date.lecture  %}
                  {% if lectures[0] %}
                      <ul>
                      {% if date.readings %}
                         {% assign readings = lectures[0].readings | where: "tag", date.readings[0] %}
                      {% else %}
                         {% assign readings = lectures[0].readings %}
                      {% endif %}  
                      {% for link in readings %}
                        <li> 
                        {%if link.abbr %}
                          <a href="{{ link.url }}">{{ link.title }}</a>
                        {% else %}
                          <a href="{{ link.url }}">{{ link.title }}</a>.
                          {%if link.author %}
                              {{ link.author }}.
                          {% endif %}
                        {% endif %}
                        {%if link.citation %}
                            {{ link.citation }}.
                        {% endif %}
                        {%if link.video %}
                            <a href="{{ link.video }}"><span class="glyphicon glyphicon-film"></span></a>
                        {% endif %}
                        {% if link.download %} 
                            <a href="{{ link.download }}"><span class="glyphicon glyphicon-save"> </span></a> 
                        {% endif %}
                        </li>
                      {% endfor %}
                      </ul>
                  {% endif %}
                {% endif %}
              </td>
              {% endif %}
            </tr>
          {% endfor %}
        {% endfor %}
        </tbody>
        </table>
    </div>
</div>

