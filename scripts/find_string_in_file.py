import os
import re

def find_string(file_path):
	"""
	'* This property will be one of: ' string and writes a note in a file so that I can go back and check
	
	Args:
	
	file_path: The path to the Markdown file.
	"""
	
	with open(file_path, 'r') as f:
	  content = f.read()
    
    for m in re.finditer(pattern, content):
		  line_number = content.count("\n", 0, m.start()) + 1
		  text_to_append = f"""Match found at line: {line_number} in file: {file_path}\n"""
		  append_text_to_file(log_file_path, text_to_append)
		  print("Match found at line: ", line_number, " in file: ", file_path)

def append_text_to_file(file_path, text_to_append):
	with open(file_path, 'a') as file:
		file.write(text_to_append)

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
				find_string(file_path)

# Extract the title from the first heading
pattern = r" \* This property"

# Directory path
directory_path = "/Users/helmlingp/euc-oss/view/versions"
log_file_path = "/Users/helmlingp/euc-oss/view/find_string_log.txt"
search_and_replace_markdown_files(directory_path)