#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from uuid import uuid4


# creation of a State
state = State(name="California", id=str(uuid4()))
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco", id=str(uuid4()))
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd", id=str(uuid4()))
user.save()

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1", id=str(uuid4()))
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2", id=str(uuid4()))
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi", id=str(uuid4()))
amenity_1.save()
amenity_2 = Amenity(name="Cable", id=str(uuid4()))
amenity_2.save()
amenity_3 = Amenity(name="Oven", id=str(uuid4()))
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")
