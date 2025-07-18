import streamlit as st
import functions

todos_file = "todos.txt"

st.set_page_config(layout="wide")
st.title("My TODOS App")

user_input = st.text_input(label="Write a todo")

with st.sidebar:
    st.write("My app")

col1, col2 = st.columns(2)

# Define the 'todo_to_edit' key as None 
if 'todo_to_edit' not in st.session_state:
    st.session_state.todo_to_edit = None

with col1:
    with st.container(border=True):
        st.write("Your TODOS")
        todos_tab, completed_tab = st.tabs(["TODOS", "Completed"])
            
        with todos_tab:
            todos = functions.get_todos(todos_file)
            for todo in todos:
                checkbox = st.checkbox(todo, key=todo)
                if checkbox:
                    popover = st.popover("Complete or edit")
                    complete = popover.button("Complete", key=f"complete_button_{todo}", use_container_width=True)
                    edit = popover.button("Edit", key=f"edit_button_{todo}", use_container_width=True)
                    if edit:
                        # Reassign the key 'todo_to_edit' to todo (selected_todo in the function edit_todo())
                        st.session_state.todo_to_edit = todo

# If session_state.todo_to_edit is assigned to the selected_todo (checkbox), the function edit() is called
if st.session_state.todo_to_edit:
    functions.edit_todo(st.session_state.todo_to_edit)

with col2:
    add_button = st.button("Add TODO", use_container_width=True)
    delete_button = st.button("Delete TODO", use_container_width=True)


if user_input:
    if add_button:
        todos = functions.get_todos(todos_file)
        todos.append(user_input + "\n")
        functions.write_todos(filepath=todos_file, content=todos)
        st.rerun()

        


st.session_state
