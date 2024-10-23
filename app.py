import streamlit as st
import pandas as pd

# Set up page title and layout
st.set_page_config(page_title="Student Daily Timetable", page_icon="📅", layout="centered")

st.title("📅 Student Daily Timetable")

# Initialize session state for storing the timetable
if "timetable" not in st.session_state:
    st.session_state["timetable"] = []

# Function to add a task to the timetable
def add_task(task, start_time, end_time):
    st.session_state["timetable"].append({"Task": task, "Start Time": start_time, "End Time": end_time})

# Input section for user to add tasks
st.subheader("Add Task to Timetable")
task = st.text_input("Enter Task Name")
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")

# Button to add the task to the timetable
if st.button("Add Task"):
    if task and start_time and end_time:
        add_task(task, start_time, end_time)
        st.success(f"Added: {task} ({start_time} - {end_time})")
    else:
        st.error("Please enter all fields.")

# Display the timetable if any tasks have been added
if st.session_state["timetable"]:
    st.subheader("Your Daily Timetable")
    df_timetable = pd.DataFrame(st.session_state["timetable"])
    st.table(df_timetable)
else:
    st.write("No tasks added to the timetable yet.")

# Option to clear the timetable
if st.button("Clear Timetable"):
    st.session_state["timetable"] = []
    st.success("Timetable cleared.")
    
# Footer
st.write("Note: This app helps create a simple timetable for the day.")
