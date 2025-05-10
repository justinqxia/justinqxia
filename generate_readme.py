#!/usr/bin/env python3

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def generate_readme():
    # Read the ASCII art and details
    ascii_lines = read_file('asciiart.txt')
    detail_lines = read_file('details.txt')
    
    # Combine the lines
    combined_lines = []
    for ascii_line, detail_line in zip(ascii_lines, detail_lines):
        # Remove trailing whitespace from ASCII art and add detail
        ascii_line = ascii_line.rstrip()
        detail_line = detail_line.rstrip()
        # Increased spacing from 40 to 48 to match test.md
        combined_line = f"{ascii_line:<56}{detail_line}"
        combined_lines.append(combined_line)
    
    # Create the final content
    content = "```text\njustinqxia@GitHub:~$ fastfetch\n"
    content += "\n".join(combined_lines)
    content += "\n```"
    
    # Write to README.md
    with open('README.md', 'w') as f:
        f.write(content)

if __name__ == "__main__":
    generate_readme() 