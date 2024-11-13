import os
import sys
from bs4 import BeautifulSoup
import html2text
import argparse

def convert_html_to_markdown(html_content):
    # Convert HTML to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Disable line wrapping
    return h.handle(html_content)

def process_file(file_path, output_dir):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse HTML and extract content from the body
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body.decode_contents() if soup.body else html_content

    # Convert to Markdown
    markdown_content = convert_html_to_markdown(body_content)

    # Create output file path
    relative_path = os.path.relpath(file_path, start=args.input_dir)
    output_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.md')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write Markdown content to file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

    print(f"Converted {file_path} to {output_path}")

def main(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                process_file(file_path, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HTML files to Markdown")
    parser.add_argument("input_dir", help="Input directory containing HTML files")
    parser.add_argument("output_dir", help="Output directory for Markdown files")
    args = parser.parse_args()

    main(args.input_dir, args.output_dir)
