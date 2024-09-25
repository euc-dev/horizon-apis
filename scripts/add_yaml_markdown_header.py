import os
import re

def replace_markdown_header(file_path):
	"""
	Replaces the YAML front matter of a Markdown file with a new header and removes unwanted text.
	If no front matter exists, it adds the new header at the beginning of the file.
	
	Args:
	file_path: The path to the Markdown file.
	"""
	
	with open(file_path, 'r') as f:
		content = f.read()
	
	# Regular expression to match YAML front matter
	front_matter_pattern = r'^---\s*\n.*?\n---\s*\n'
	# Extract the title from the first heading
	title_match = re.search(r'^#\s*(.*)$', content, re.MULTILINE)
	title = title_match.group(1) if title_match else "untitled"
	
	new_header = f"""---
layout: page
title: {title}
hide:
- navigation
#- toc
---
"""
	
	# Replace existing front matter or add new header at the beginning
	if re.match(front_matter_pattern, content, re.DOTALL):
		content = re.sub(front_matter_pattern, new_header, content, count=1, flags=re.DOTALL)
	
	else:
		content = new_header + content
	
	with open(file_path, 'w') as f:
		f.write(content)

def search_and_replace_markdown_files(directory):
	"""
	Recursively searches a directory for Markdown files, replaces their headers, and removes unwanted text.
	
	Args:
	directory: The path to the directory to search.
	"""
	
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith('.md'):
				file_path = os.path.join(root, file)
				replace_markdown_header(file_path)

# Directory path
directory_path = "/Users/helmlingp/euc-oss/view/versions/7.6.0"
search_and_replace_markdown_files(directory_path)