from typing import List, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine

class ImageTagLink(SQLModel, table=True):
    image_id: Optional[int] = Field(
        default=None, foreign_key="image.id", primary_key=True
    )
    tag_id: Optional[int] = Field(
        default=None, foreign_key="tag.id", primary_key=True
    )

class Image(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str
    tags: List["Tag"] = Relationship(back_populates="images", link_model=ImageTagLink)

class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    images: List["Image"] = Relationship(back_populates="tags", link_model=ImageTagLink)


sqlite_file_name = "image_database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def add_tags_and_images():
    nature = Tag(name="nature")
    ghibli = Tag(name="ghibli")
    city = Tag(name="city")
    abstract = Tag(name="abstract")
    painting = Tag(name="painting")
    digital_art = Tag(name="digital_art")
    comfy = Tag(name="comfy")
    best = Tag(name="best")

    with Session(engine) as session:
        session.add_all([nature, ghibli, city, abstract, painting, digital_art, comfy, best])
        
        # image_1 = Image(url="xyz.com/img1.png", tags=[nature, ghibli]) 
        # image_2 = Image(url="xyz.com/img2.png", tags=[city])
        # session.add_all([image_1, image_2])

        session.commit()  


if __name__ == "__main__":
    create_db_and_tables()
    add_tags_and_images()