from sqlmodel import JSON, SQLModel, Field, Column

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: list[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.\
                Ensure to come with your own copy to win gifts!",
                "tags": ["python", "book", "launch"],
                "location": "Google Meet"
            }
        }

class EvenUpdate(SQLModel):
    title: str | None = None
    image: str | None = None
    description: str | None = None
    tags: list[str] | None = None
    location: str | None = None

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.\
                Ensure to come with your own copy to win gifts!",
                "tags": ["python", "book", "launch"],
                "location": "Google Meet"
            }
        }