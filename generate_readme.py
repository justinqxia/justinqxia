#!/usr/bin/env python3

def read_file(filename):
    # Strip newline characters from the end of each line
    with open(filename, 'r') as f:
        return [line.rstrip('\n') for line in f.readlines()]

def generate_readme():
    # Read the txt files
    ascii_lines = read_file('asciiart.txt')
    detail_lines = read_file('details.txt')
    
    # Combine the lines
    combined_lines = []
    for ascii_line, detail_line in zip(ascii_lines, detail_lines):
        # Add 11 spaces after ASCII art and combine with detail
        combined_line = f"{ascii_line}           {detail_line}"
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