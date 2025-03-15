import streamlit as st

# Title of the app
st.title("✅ To-Do List")

# Session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input field for new task
new_task = st.text_input("Add a new task", "")

# Button to add task
if st.button("➕ Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Added: {new_task}")
    else:
        st.warning("Task cannot be empty!")

# Show current tasks
st.subheader("📋 Your Tasks:")
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(f"- {task}")
    if col2.button("❌", key=i):
        st.session_state.tasks.pop(i)
        st.rerun()
