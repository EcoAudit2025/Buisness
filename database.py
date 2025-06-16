# database.py

from collections import namedtuple
from datetime import datetime, timedelta
import random

# Mock data structure for utility record
UtilityRecord = namedtuple("UtilityRecord", [
    "timestamp", "water_gallons", "electricity_kwh", "gas_cubic_m",
    "water_status", "electricity_status", "gas_status",
    "efficiency_score", "carbon_footprint"
])

# Mock data structure for user
User = namedtuple("User", [
    "id", "username", "email", "location_type", "climate_zone", "adults",
    "children", "seniors", "household_type", "housing_type",
    "energy_features", "is_public", "language",
    "environmental_class", "ai_analysis", "created_at", "household_size"
])

# Generate mock utility history
def get_utility_history(limit=100):
    now = datetime.now()
    history = []
    for i in range(limit):
        history.append(UtilityRecord(
            timestamp=now - timedelta(days=i*30),
            water_gallons=random.randint(3000, 12000),
            electricity_kwh=random.randint(300, 800),
            gas_cubic_m=random.randint(50, 150),
            water_status="Normal",
            electricity_status="Normal",
            gas_status="Normal",
            efficiency_score=random.randint(50, 90),
            carbon_footprint=random.uniform(20.0, 50.0)
        ))
    return history

# Example current user for testing
def get_user(username):
    return User(
        id=1,
        username=username,
        email="user@example.com",
        location_type="Urban",
        climate_zone="Tropical",
        adults=2,
        children=1,
        seniors=0,
        household_type="Family",
        housing_type="Apartment",
        energy_features='["LED Lighting"]',
        is_public="public",
        language="English",
        environmental_class=None,
        ai_analysis=None,
        created_at=datetime(2023, 6, 1),
        household_size=3
    )

def create_user(**kwargs):
    return get_user(kwargs.get("username", "default_user"))

def save_utility_usage(**kwargs):
    print("Usage saved:", kwargs)

def get_user_usage_last_year(user_id):
    return get_utility_history(12)

def get_all_users():
    return [get_user("user1"), get_user("user2")]

def get_public_users():
    return [get_user("user1")]

def get_popular_materials(n):
    Material = namedtuple("Material", ["name", "search_count"])
    return [Material(name="plastic bottle", search_count=25)]

def find_material(name):
    MaterialData = namedtuple("MaterialData", ["reuse_tip", "recycle_tip"])
    return MaterialData(reuse_tip="Reuse it as a plant pot.", recycle_tip="Recycle it at your nearest center.")

def calculate_environmental_class(user_usage):
    return "A"

def generate_user_ai_analysis(user, usage):
    return "Your usage pattern is efficient."

def update_user_environmental_class(user_id, env_class, analysis):
    pass
