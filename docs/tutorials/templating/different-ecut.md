```jinja2
encut ={% spaceless %}
{# ================================================================= #}
{#                                                                   #}
{#  The code below automatically sets the value of "encut" flag		 #}
{#  for materials that contain Oxygen to higher that for others:     #}
{#                                                                   #}
{#      encut = 60 ! or 45 if no Oxygen is present                   #}
{#                                                                   #}
{# ================================================================= #}
{% set high_cutoff_element = "Al" %}
{% set poscar_string = input.POSCAR|e("js") %}
{% set atoms = poscar_string.split('direct')[0] %}
{% set lines = atoms.split("\u000A") %}
{% set element_lines = lines[5] %}
{% if element_lines.includes(high_cutoff_element) %} 60{% else %} 45{% endif %}
{% endspaceless %}
```
