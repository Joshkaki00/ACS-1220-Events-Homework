# Events Site

## Purpose
This project allows you to practice creating SQLAlchemy models and using them to construct a small web application. It's designed to help you understand database relationships and web application development using Flask and SQLAlchemy.

## Setup Instructions

1. Clone this repository to your computer
2. Navigate to the project folder in your terminal
3. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
5. Run the server:
   ```bash
   python3 app.py
   ```

## Project Structure

The application consists of the following main components:

### Models
- `Event` and `Guest` models with appropriate relationships
- Located in `events_app/models.py`

### Routes & Templates
- `index` (`templates/index.html`): Shows a list of all events
- `create` (`templates/create.html`): Form to create new events
- `event_detail` (`templates/event_detail.html`): Details of a single event and RSVP form
- `rsvp`: Handles RSVP submissions
- `guest_detail` (`templates/guest_detail.html`): Shows guest details and their RSVPs

## Features
- Create and manage events
- RSVP system for guests
- View event details and guest lists
- View guest profiles and their event history

## Resources
- [SQLAlchemy Relationship Patterns](https://docs.sqlalchemy.org/en/13/orm/relationship_persistence.html)
- [Declaring Models](https://docs.sqlalchemy.org/en/13/orm/mapping_styles.html)
- [Filter Operations](https://docs.sqlalchemy.org/en/13/orm/query.html)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)

## Grading Criteria

| Score | Rating | Correctness | Code Quality |
|-------|--------|-------------|--------------|
| **1** | Needs Improvement | Required sections missing or not functional | Messy code, missing docstrings |
| **2** | Basic | Most routes functional, some hard-coded | Some messy code, missing some docstrings |
| **3** | Proficient | All routes functional | Clear code, complete docstrings |
| **4** | Advanced | Stretch challenges complete | Extensible code with helper functions |
