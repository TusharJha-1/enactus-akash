import os

base_path = r"c:\Users\akash\OneDrive\Desktop\enactus\enactus2\enactus"
about_path = os.path.join(base_path, "templates", "about.html")
new_script_path = os.path.join(base_path, "new_map_script.txt")

with open(about_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(new_script_path, "r", encoding="utf-8") as f:
    new_script_content = f.read()

start_marker = "<!-- Dotted Map Script -->"
end_marker = "{% endblock %}"

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if start_marker in line:
        start_idx = i
    if end_marker in line and start_idx != -1 and i > start_idx:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    print(f"Found block from line {start_idx} to {end_idx}")
    # Replace content. Note: lines has newlines. new_script_content is a string.
    # We want to replace lines[start_idx:end_idx] with new_script_content
    # But new_script_content needs to be split if we keep list structure, or just join.
    
    # Simpler:
    new_lines = lines[:start_idx] + [new_script_content + "\n"] + lines[end_idx:]
    
    with open(about_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("Successfully updated about.html")
else:
    print("Could not find markers")
    print(f"Start: {start_idx}, End: {end_idx}")
