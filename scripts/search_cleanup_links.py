import os
import re

def replace_html_with_md(file_path):
	# Read the content of the file
	with open(file_path, 'r', encoding='utf-8') as file:
		content = file.read()

	# Perform the replacement
	new_content = content.replace('.html', '.md')
	
	# Write the modified content back to the file
	with open(file_path, 'w', encoding='utf-8') as file:
		file.write(new_content)
	
	print(f"Replacements made in {file_path}")

def process_directory(directory):
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith('.md'): # Process only Markdown files
				file_path = os.path.join(root, file)
				replace_html_with_md(file_path)

# Usage for a single file
directory_path = "/Users/helmlingp/euc-oss/view/versions"
process_directory(directory_path)
 
# Usage for a directory (uncomment to use)
# directory_path = 'path/to/your/directory'
# process_directory(directory_path)