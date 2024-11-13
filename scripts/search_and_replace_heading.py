import os
import re

def remove_specific_headings(file_path):
	# Read the file content
	with open(file_path, 'r', encoding='utf-8') as file:
		lines = file.readlines()
	
	# Process the lines
	cleaned_lines = []
	for line in lines:
		# Check if the line starts with '# ' but not '#- '
		if not re.match(r'^# (?!-)', line):
			cleaned_lines.append(line)
		
		# Write the cleaned content back to the file
		with open(file_path, 'w', encoding='utf-8') as file:
			file.writelines(cleaned_lines)

		print(f"Specific headings removed from {file_path}")

def search_and_replace_markdown_files(directory):
	"""
	Recursively searches a directory for Markdown files and replaces their headers.
	
	Args:
	directory: The path to the directory to search.
	"""
	
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith('.md'):
				file_path = os.path.join(root, file)
				remove_specific_headings(file_path)

# Directory path
directory_path = "/Users/helmlingp/euc-oss/view/versions"
search_and_replace_markdown_files(directory_path)