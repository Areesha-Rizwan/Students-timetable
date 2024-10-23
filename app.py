import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Student Daily Timetable", page_icon="📅", layout="centered")

# Add custom CSS for improved styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: #4A90E2;
        }
        .subtitle {
            font-size: 1.5em;
            color: #555;
            margin-bottom: 20px;
        }
        .timetable-table {
            border-radius: 10px;
            border: 1px solid #ddd;
            padding: 10px;
        }
        .add-button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        .clear-button {
            background-color: #FF6347;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<div class="title">📅 Student Daily Timetable</div>', unsafe_allow_html=True)

# Subheading
st.markdown('<div class="subtitle">Plan your tasks for the day by adding tasks and time slots</div>', unsafe_allow_html=True)

# Initialize session state for storing the timetable
if "timetable" not in st.session_state:
    st.session_state["timetable"] = []

# Function to add a task to the timetable
def add_task(task, start_time, end_time):
    st.session_state["timetable"].append({"Task": task, "Start Time": start_time, "End Time": end_time})

# Input section using columns
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    task = st.text_input("📝 Task Name")
with col2:
    start_time = st.time_input("⏰ Start Time")
with col3:
    end_time = st.time_input("⌛ End Time")

# Add button with feedback
if st.button("Add Task", key="add_task"):
    if task and start_time and end_time:
        add_task(task, start_time, end_time)
        st.success(f"✅ Task '{task}' added from {start_time} to {end_time}.")
    else:
        st.error("⚠️ Please fill in all fields before adding a task.")

# Display the timetable if tasks have been added
if st.session_state["timetable"]:
    st.subheader("Your Daily Timetable")
    df_timetable = pd.DataFrame(st.session_state["timetable"])
    st.markdown('<div class="timetable-table">', unsafe_allow_html=True)
    st.table(df_timetable)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("No tasks added to the timetable yet.")

# Clear timetable button
if st.button("Clear Timetable", key="clear_timetable"):
    st.session_state["timetable"] = []
    st.success("🗑️ Timetable cleared.")

# Footer
st.write("Note: This app is for helping you plan your tasks for the day.")
