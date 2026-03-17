'''from textnode import TextNode, TextType
import os
import shutil
from copystatic import copy_files_recursive
from gencontent import generate_page


dir_path_static = "./static"
dir_path_public = "./public"

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    #print(node)
    #print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

   # print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page(
        "content/index.md",
        "template.html",
        "public/index.html"
    )

if __name__ == "__main__":
    main()
'''

import os
import shutil
# Her importerer vi funksjonene fra de andre filene dine
from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Gå gjennom alt i content-mappen
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                # Bytt ut .md med .html for destinasjonen
                # Vi bruker Path for å håndtere filendelser tryggere
                from pathlib import Path
                dest_html_path = os.path.join(dest_dir_path, Path(filename).stem + ".html")
                
                print(f"Genererer side: {from_path} -> {dest_html_path}")
                generate_page(from_path, template_path, dest_html_path)
        else:
            # Hvis det er en mappe, lag den i public og gå dypere
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path)

def main():
    print("Sletter public-mappe...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Kopierer statiske filer...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Starter rekursiv generering av sider...")
    generate_pages_recursive("./content", "template.html", dir_path_public)

if __name__ == "__main__":
    main()
