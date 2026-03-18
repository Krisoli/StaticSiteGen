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

'''import os
import shutil
from pathlib import Path


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Gå gjennom alle elementer i content-mappen
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        # Hvis det er en fil, sjekk om det er markdown
        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                # Endre etternavn fra .md til .html
                dest_html_path = dest_path.replace(".md", ".html")
                print(f"Genererer side: {from_path} -> {dest_html_path}")
                generate_page(from_path, template_path, dest_html_path)
        
        # Hvis det er en mappe, opprett tilsvarende mappe i public og gå dypere
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path)

def main():
    # 1. Slett public-mappen for en ren start
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    
    # 2. Kopier statiske filer (antar du har en funksjon for dette)
    # copy_static("./static", "./public") 

    # 3. Generer alle sider rekursivt
    print("Starter rekursiv generering...")
    generate_pages_recursive("./content", "template.html", "./public")

if __name__ == "__main__":
    main()
'''
import os
import shutil
import sys
from copystatic import copy_files_recursive
from gencontent import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                from pathlib import Path
                dest_html_path = os.path.join(dest_dir_path, Path(filename).stem + ".html")
                print(f"Genererer side: {from_path} -> {dest_html_path}")
                # Send basepath videre til generate_page
                generate_page(from_path, template_path, dest_html_path, basepath)
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

def main():
    # Hent basepath fra argumenter, default til "/"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    dir_path_static = "./static"
    dir_path_docs = "./docs" # Endret fra public til docs

    print(f"Sletter {dir_path_docs}...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Kopierer statiske filer...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print(f"Genererer sider med basepath: {basepath}")
    generate_pages_recursive("./content", "template.html", dir_path_docs, basepath)

if __name__ == "__main__":
    main()

    
import os
import shutil
import sys
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs" # Endret fra public til docs for GitHub Pages

def main():
    # 1. Hent basepath fra CLI-argumenter, default til "/"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    # Slett docs-mappen for en ren start
    if os.path.exists(dir_path_docs):
        print(f"Sletter eksisterende {dir_path_docs}...")
        shutil.rmtree(dir_path_docs)

    # Kopier statiske filer til docs-mappen
    print(f"Kopierer statiske filer fra {dir_path_static} til {dir_path_docs}...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    # Generer alle sider rekursivt med den valgte basepathen
    print(f"Starter rekursiv generering med basepath: '{basepath}'...")
    generate_pages_recursive(
        "./content", 
        "template.html", 
        dir_path_docs, 
        basepath
    )

if __name__ == "__main__":
    main()
