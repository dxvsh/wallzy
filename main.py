from typing import Union, List
from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from models import Image, Tag, ImageTagLink, Session, engine
from sqlmodel import select
from api_documentation import api_docs
import random

app = FastAPI()

defined_tags = ['nature', 'ghibli', 'city', 'abstract', 'painting', 'digital_art', 'comfy', 'best']

@app.get("/")
async def read_root():
    return api_docs

@app.get("/random")
async def get_random_image():
    with Session(engine) as session:
        images = session.exec(select(Image)).all()
        randimg_idx = random.randint(0, len(images)-1)
        randimg_url = images[randimg_idx].url
        return RedirectResponse(url=randimg_url)


@app.get("/{tag}")
async def get_tagged_image(tag: str):
    if tag in defined_tags:
        with Session(engine) as session:
            tag_object = session.exec(select(Tag).where(Tag.name == tag)).one()
            randimg_idx = random.randint(0, len(tag_object.images)-1)
            randimg_url = tag_object.images[randimg_idx].url
            return RedirectResponse(url=randimg_url)
    else:
        return {"error": f"Tag '{tag}' doesn't exist in the database. Try from one of the defined tags.",
                "defined_tags": defined_tags}


@app.get("/intersection/")
async def get_images_by_tags(tags: List[str] = Query(...)):

    # input sanitation: check if supplied tags actually exist in the db
    if not(set(tags).issubset(set(defined_tags))):
        return {"error": "One or more of the supplied tags don't exist in the db. Try again with the defined tags.",
                "defined_tags": defined_tags}
    
    # Query for tags based on the provided names
    with Session(engine) as session:
        tag_models = session.exec(select(Tag).where(Tag.name.in_(tags))).all()
        # print(tag_models)

        # Get images that have all the specified tags
        # this set will hold all our matching images
        image_ids = set()

        # add all images that match the first tag in the list
        image_ids_tag1 = session.exec(
            select(ImageTagLink.image_id).where(ImageTagLink.tag_id == tag_models[0].id)
        ).all()

        # now the set contains will all images with the first tag
        image_ids.update(image_ids_tag1)

        # here we'll continually update our set by making intersections with other sets
        for tag in tag_models[1:]:
            image_ids_for_tag = session.exec(
                select(ImageTagLink.image_id).where(ImageTagLink.tag_id == tag.id)
            ).all()
            image_ids.intersection_update(image_ids_for_tag)

        # print(image_ids)

        if not image_ids:
            return {"error": "No images found with this intersection!"}

        # Fetch image details using the collected image ids
        matching_images = session.exec(select(Image).where(Image.id.in_(image_ids))).all()
        randimg_idx = random.randint(0, len(matching_images)-1)
        randimg_url = matching_images[randimg_idx].url
        return RedirectResponse(url=randimg_url)        
        # return {"matching_images": [image.dict() for image in matching_images]}

