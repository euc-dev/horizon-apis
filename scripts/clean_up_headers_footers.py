import os
import re

def remove_unwanted_text(file_path):
	"""
	Removes the specified unwanted text blocks from the content.
	
	Args:
	content: The content of the file as a string.
	
	Returns:
	The content with the unwanted text removed.
	"""
	text_block = r"""
	| | Local Properties|
	---|---|---|---
	[Service Types](index-mo_types.html)| [Data Object Types](index-do_types.html)| [All Properties](index-properties.html)| [All Methods](index-methods.html)
	"""

	# Read the file content
	with open(file_path, 'r', encoding='utf-8') as file:
		content = file.read()

  # Remove the text block
  content_cleaned = re.sub(re.escape(text_block), '', content, flags=re.DOTALL)
		
		# Write the cleaned content back to the file
		with open(file_path, 'w', encoding='utf-8') as file:
		file.write(content_cleaned)
		
		print(f"Text block removed from {file_path}")

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
				remove_unwanted_text(file_path)

# Directory path
directory_path = "/Users/helmlingp/euc-oss/view/versions/2406"
search_and_replace_markdown_files(directory_path)