"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
from enum import Enum

class EventType(Enum):
    PARTY = "Party"
    STUDY = "Study"
    NETWORKING = "Networking"
    OTHER = "Other"


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    events_attending = db.relationship('Event', secondary='guest_event_table', backref=backref('guests', lazy='dynamic'))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    event_type = db.Column(db.Enum(EventType), nullable=False, default=EventType.OTHER)

guest_event_table = db.Table('guest_event_table',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'), primary_key=True)
)