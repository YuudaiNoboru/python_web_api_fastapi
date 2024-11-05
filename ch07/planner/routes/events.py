from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, Request,status
from models.events import Event, EvenUpdate
from database.connection import Database

event_router = APIRouter(tags=["Events"])

event_database = Database(Event)

@event_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    events = await event_database.get_all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event with supplied ID does not exist.")
    return event

@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {
        "message": "Event created successfully."
    }

@event_router.delete("/delete/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event with supplied ID does not exist.")
    return {"message": "Event deleted successfully."}

@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EvenUpdate) -> Event:
    update_event = await event_database.update(id, body)
    if not update_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event with supplied ID does not exist.")
    return update_event