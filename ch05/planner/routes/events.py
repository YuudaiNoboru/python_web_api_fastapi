from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event

even_router = APIRouter(tags=["Events"])

events = []

@even_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    return events

@even_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="vent with supplied ID does not exist.")

@even_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message": "Event created successfully."
    }

@even_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "Event deleted successfully."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event with supplied ID does not exist.")

@even_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "Events deleted successfully."}