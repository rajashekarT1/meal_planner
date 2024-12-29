import streamlit as st
from datetime import date

class MoodTracker:
    def __init__(self):
        self.entries = []

    def add_entry(self, date, mood, journal_entry):
        self.entries.append({"date": date, "mood": mood, "journal_entry": journal_entry})

    def show_entries(self):
        return self.entries


def run_mood_tracker():
    mood_tracker = MoodTracker()

    st.title("Mood Tracker")

    with st.form(key='mood_form'):

        date_input = st.date_input("Date", min_value=date(2020, 1, 1))
        mood = st.selectbox("Mood", ["Happy", "Sad", "Angry", "Neutral"])
        journal_entry = st.text_area("Journal Entry")

        add_mood_button = st.form_submit_button(label='Add Mood Entry')

        if add_mood_button:
            if date_input and mood and journal_entry:
                mood_tracker.add_entry(str(date_input), mood, journal_entry)
                st.success("Mood entry added successfully!")
            else:
                st.error("Please fill in all the fields.")

    st.subheader("Mood Entries")
    entries = mood_tracker.show_entries()
    if entries:
        for entry in entries:
            st.write(f"**Date:** {entry['date']}")
            st.write(f"**Mood:** {entry['mood']}")
            st.write(f"**Journal Entry:** {entry['journal_entry']}")
            st.write("---")
    else:
        st.write("No mood entries yet.")

if __name__ == "__main__":
    run_mood_tracker()
