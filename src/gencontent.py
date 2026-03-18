import os
from pathlib import Path
from blocks import markdown_to_html_node, extract_title
'''
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f:
        markdown_content = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()

    node = markdown_to_html_node(markdown_content)
    html_content = node.to_html()
    
    title = extract_title(markdown_content)
    
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    html_content = html_content.replace('href="/', f'href="{basepath}')
    html_content = html_content.replace('src="/', f'src="{basepath}')
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(template)
'''



import os
from pathlib import Path
from blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} with basepath {basepath}")
    
    with open(from_path, "r") as f:
        markdown_content = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()

    node = markdown_to_html_node(markdown_content)
    html_content = node.to_html()
    
    title = extract_title(markdown_content)
    
    # Sett inn innhold i template
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    
    # Erstatt stier med basepath
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # Denne funksjonen må være her for at main.py skal kunne importere den!
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                # Lag html-filnavn
                dest_html_path = os.path.join(dest_dir_path, Path(filename).stem + ".html")
                generate_page(from_path, template_path, dest_html_path, basepath)
        else:
            # Hvis det er en mappe, lag den og gå dypere
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
