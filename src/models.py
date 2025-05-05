from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    subscription_date : Mapped[str] = mapped_column(nullable=False)

    favorites = relationship("Favorite", back_populates="users")

class People(db.Model):
    __tablename__ = 'peoples'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    height: Mapped[int]
    gender: Mapped[str] = mapped_column(nullable=False)
    birth_year: Mapped[str] = mapped_column(nullable=False)
    species: Mapped[str] = mapped_column(nullable=False)

    favorites = relationship("Favorite", back_populates="people")
    
class Planet(db.Model):
    __tablename__ = 'planets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[str] = mapped_column(nullable=False)

    favorites = relationship("Favorite", back_populates="planets")

class Favorite(db.Model):
    __tablename__ = 'favorites'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey('users.id'))
    people_id : Mapped[int] = mapped_column(ForeignKey('peoples.id'))
    planet_id : Mapped[int] = mapped_column(ForeignKey('planets.id'))

    users = relationship("User" , back_populates="favorites")
    people = relationship("People" , back_populates="favorites")
    planets = relationship("Planet" , back_populates="favorites")