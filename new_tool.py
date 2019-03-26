#! /usr/bin/env python
# [Gedit Tool]
# Input=document
# Applicability=all
# Output=replace-document
# Name=Format
# Shortcut=<Primary><Shift>f
# Save-files=nothing


import json
import sys
import lxml.etree as etree
import traceback
import copy 

def is_json(inp):
	try:
		json_object = json.loads(inp)
	except ValueError, e:
		return None
	return json_object

def format():
	result = ''
	for line in sys.stdin:
  		result += line
	j = is_json(result)
	if j:
		result = json.dumps(j, sort_keys=True, indent=2)
	else:
		try:
		  x = etree.fromstring(result)
		  result = etree.tostring(x, pretty_print=True, xml_declaration=True, encoding="UTF-8")
		except:
		  etype, evalue, etraceback = sys.exc_info()
		  traceback.print_exception(etype, evalue, etraceback, file=sys.stderr)
	return result

print format()
	
