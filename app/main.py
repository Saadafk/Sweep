from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import Base, engine, get_db
from app.models import Ticket, TicketCreate, TicketOut, TicketUpdate
Base.metadata.create_all(engine)

app = FastAPI(title="Sweep")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tickets", response_model=TicketOut)
def create_ticket(data: TicketCreate, db: Session = Depends(get_db)):
    ticket = Ticket(title=data.title, description=data.description, requester=data.requester)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


@app.get("/tickets", response_model=list[TicketOut])
def list_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).order_by(Ticket.id.desc()).all()

@app.get("/tickets/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.get(Ticket, ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@app.patch("/tickets/{ticket_id}", response_model=TicketOut)
def update_ticket(ticket_id: int, data: TicketUpdate, db: Session = Depends(get_db)):
    ticket = db.get(Ticket, ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    if data.category is not None:
        ticket.category = data.category
    if data.priority is not None:
        ticket.priority = data.priority
    if data.status is not None:
        ticket.status = data.status

    db.commit()
    db.refresh(ticket)
    return ticket