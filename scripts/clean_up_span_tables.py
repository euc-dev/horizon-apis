import os
import re
from pathlib import Path

def remove_unwanted_text(file_path):
	"""
	Removes the specified unwanted text blocks from the content.
	
	Args:
	content: The content of the file as a string.
	
	Returns:
	The content with the unwanted text removed.
	"""
	text_block1 = r"""
	## Data Object Properties

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
	"""
	text_block1_repl = r"""
	## Data Object Properties

::spantable::

 Name | Type | Description
:---|:---:|:---
	"""
	text_block2 = r"""
None @span
	
	"""
	text_block2_repl = r"""
None @span
::end-spantable::

	"""

	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			content = file.read()
			
			# Check if both blocks exist in the file
			#if text_block1 in content and text_block2 in content:
			normalized_content = re.sub(r'^\s+|\s+$', '', content, flags=re.MULTILINE)
			normalized_content = normalized_content.replace('\r\n', '\n')
			
			# Check if the normalized text block is in the normalized content
			if text_block1 in normalized_content:
				#matching_files.append(file_path)
				print(file_path)

	except Exception as e:
			print(f"Error reading {file_path}: {e}")
	# Read the file content
	# with open(file_path, 'r', encoding='utf-8') as file:
	# 	content = file.read()
	# for m in re.finditer(text_block1, content):
	# 	line_number = content.count("\n", 0, m.start()) + 1
	# 	text_to_append = f"""Match found at line: {line_number} in file: {file_path}\n"""

		# Remove the text block
  	#content_cleaned = re.sub(re.escape(text_block1), text_block1_repl, content, flags=re.DOTALL)
		
	# Write the cleaned content back to the file
	# with open(file_path, 'w', encoding='utf-8') as file:
	# 		file.write(content_cleaned)
	
		# append_text_to_file(log_file_path, text_to_append)
		# print(text_to_append)
	
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
				current_path = os.curdir
				file_name = Path(file).name
				file_path = os.path.join(root, file)
				#print(f"{file_name} in dir: {current_path}")
				remove_unwanted_text(file_path)

# Directory path
directory_path = "./docs/view/versions/2406"
log_file_path = "/Users/helmlingp/euc-dev/horizon-apis/docs/view/clean_up_span_tables1_log.txt"
search_and_replace_markdown_files(directory_path)