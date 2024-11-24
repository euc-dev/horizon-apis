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
	text_block1 = r"""
Properties inherited from [EntityId](vdi.EntityId.md) @span
[id](vdi.EntityId.md#id) @span

"""
	text_block1_repl = r"""
Properties inherited from [EntityId](vdi.EntityId.md) @span
[id](vdi.EntityId.md#id) @span

::end-spantable::
"""

	# Read the file content
	with open(file_path, 'r', encoding='utf-8') as file:
		content = file.read()

  	
	for m in re.finditer(text_block1, content):
		line_number = content.count("\n", 0, m.start()) + 1
		text_to_append = f"""Match found at line: {line_number} in file: {file_path}\n"""

		# Remove the text block
  	#content_cleaned = re.sub(re.escape(text_block1), text_block1_repl, content, flags=re.DOTALL)
		
	# Write the cleaned content back to the file
	# with open(file_path, 'w', encoding='utf-8') as file:
	# 		file.write(content_cleaned)
	
	append_text_to_file(log_file_path, text_to_append)
	print(f"Text block changed from {file_path}")
	
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
				remove_unwanted_text(file_path)

# Directory path
directory_path = "/Users/helmlingp/euc-dev/horizon-apis/docs/view/versions/2406"
log_file_path = "/Users/helmlingp/euc-dev/horizon-apis/docs/view/clean_up_span_tables1_log.txt"
search_and_replace_markdown_files(directory_path)