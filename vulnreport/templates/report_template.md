# Vulnerability Report

## Title: {{ title }}
**Severity:** {{ severity }}  
**Target:** {{ target }}

---

## Description
{{ description }}

## Steps to Reproduce
{% for step in steps_to_reproduce %}
- {{ step }}
{% endfor %}

## Impact
{{ impact }}

## Recommendation
{{ recommendation }}

## Screenshots
{% for img in screenshots %}
![Proof of Concept]({{ img }})
{% endfor %}
