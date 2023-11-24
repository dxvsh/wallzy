import os
from models import Image, Tag, Session, engine
from sqlmodel import select

session = Session(engine)
defined_tags = ['nature', 'ghibli', 'city', 'abstract', 'painting', 'digital_art', 'comfy', 'best']


# creates a text file with a listing of all the URL's of the images in the given directory
def create_file_list(directory_name, output_filename, url_prefix):
    with open(output_filename, 'w') as file:
        for filename in os.listdir(directory_name):
            file.write(f"{url_prefix}{filename}\n")

directory_name = "/home/athena/Walls"
output_filename = "image_list.txt"

# url prefix to add to our filenames, this is the url where the images are located online
url_prefix = 'https://storage.googleapis.com/wallzy-fcc69.appspot.com/' 

create_file_list(directory_name, output_filename, url_prefix)
# now the output file contains the URL of each image in the directory (one on each line)

f = open(output_filename, 'r')

# add the images to the DB along with their tags
for line in f.readlines():
    url = line.strip()
    print("Filename :", url.split("appspot.com/")[-1])
    tags = input("Enter the tags for image, separated by spaces: ").split()

    while not(set(tags).issubset(set(defined_tags))):
        print("One or more of the entered tags is not defined. Try again and enter one of the defined tags.")
        print("Defined tags: ", defined_tags)
        tags = input("Enter the tags for image, separated by spaces: ").split()

    taglist = []
    for tag in tags:
        taglist.append(session.exec(select(Tag).where(Tag.name==tag)).one())
    img = Image(url=url, tags=taglist)
    session.add(img)
    session.commit()
    print("Commit Successful! Tags added to the image.")