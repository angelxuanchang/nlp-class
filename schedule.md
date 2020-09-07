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
                {% else %}
                  Lecture: {{ date.title }} <br/>
                  {% if date.tutorial != null %}
                    Tutorial: {{ site.tutorials[date.tutorial].title }}  <br/>
                  {% endif %}
                {% endif %}
              </td>
              <td>
                {% if date.hwdue %}
                  Due: HW{{ date.hwdue }}
                {% endif %}
              </td>
              <td>
              </td>
            </tr>
          {% endfor %}
        {% endfor %}
        </tbody>
        </table>
    </div>
</div>

