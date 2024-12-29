import streamlit as st
from multiapp import MultiApp  
import meal_planner
import energy_tracker
import outfit_planner 
import family_budget 
import mood_tracker

app = MultiApp()

app.add_app("Meal Planner",meal_planner.meal)
app.add_app("Energy Tracker", energy_tracker.run_energy_tracker)
app.add_app("Outfit Planner", outfit_planner.app)
app.add_app("Family Budgeting", family_budget.run_family_budget)
app.add_app("Mood Tracker", mood_tracker.run_mood_tracker)

app.run()
