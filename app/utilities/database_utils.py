"""Module to keep all database functionality in one place."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from app.utilities.weight import Weight

DATABASE_NAME = "app/weights.db"
engine = create_engine(f"sqlite:///{DATABASE_NAME}")
Session = sessionmaker(engine)


def initialise_database():
    if not database_exists(engine.url):
        create_database(engine.url)
        Weight.__table__.create(engine)


def add_measurement(weight_obj):
    """Adds weight measurement coming from the slack app to `Weight` table.

    Args:
        weight_obj (:py:class:`Weight`): custom class that contains data needed to add a new
            weight measurement.
    """
    with Session() as s:
        s.add(weight_obj)
        s.commit()
