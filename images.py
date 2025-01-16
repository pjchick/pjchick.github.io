import os
import re
import shutil
import pathlib
import subprocess
from datetime import datetime

def list_files_in_all_directories(root_directory):
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for file in filenames:
            all_files.append(os.path.join(dirpath, file))
    return all_files

obsidian_source_dir = r"D:\Obsidian Vault\pjchick.github.io"
obsidian_attachments_dir = r"D:\Obsidian Vault\_attachments"

hugo_content_dir = r"D:\repos\pjchick.github.io\content"
hugo_static_images_dir = r"D:\repos\pjchick.github.io\static\images"

# Step 1: Copy content files. 
if os.path.exists(hugo_content_dir):
    shutil.rmtree(hugo_content_dir)
    shutil.copytree(obsidian_source_dir, hugo_content_dir, dirs_exist_ok=True)

# Step 2: Process image files
if os.path.exists(hugo_static_images_dir):
    shutil.rmtree(hugo_static_images_dir)
    os.makedirs(hugo_static_images_dir)

for fullfilename in list_files_in_all_directories(hugo_content_dir):

    print(fullfilename)
    filepath, filename = os.path.split(fullfilename)

    if filename.endswith(".md"):
        
        with open(fullfilename, "r", encoding="utf-8") as file:
            content = file.read()
        
        #Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
        #Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            #Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(obsidian_attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, hugo_static_images_dir)

        #Write the updated content back to the markdown file
        with open(fullfilename, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")

# Step 3: Rebuild hugo
subprocess_result = subprocess.run('hugo',check = True, capture_output=True, text=True)
print(f"Exit code: {subprocess_result.returncode}")
print(f"Standard output: {subprocess_result.stdout}")
print(f"Standard error: {subprocess_result.stderr}")


# Step 4: 

subprocess_result = subprocess.run(['git', 'add', '.'],check = True, capture_output=True, text=True)
print(f"Exit code: {subprocess_result.returncode}")
print(f"Standard output: {subprocess_result.stdout}")
print(f"Standard error: {subprocess_result.stderr}")


now = datetime.now()
date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")
commit_message = "Blog update: " + date_time_string


subprocess_result = subprocess.run(['git', 'commit', '-m', commit_message],check = True, capture_output=True, text=True)
print(f"Exit code: {subprocess_result.returncode}")
print(f"Standard output: {subprocess_result.stdout}")
print(f"Standard error: {subprocess_result.stderr}")

#subprocess.run(['git', 'commit', '-m', commit_message], check=True)