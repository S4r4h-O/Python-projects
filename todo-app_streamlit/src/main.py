import enum
import streamlit as st
import functions

todos_file = "todos.txt"

st.title("My TODOS App")

user_input = st.text_input(label="Write a todo")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.write("Your TODOS")
        todos_tab, completed_tab = st.tabs(["TODOS", "Completed"])
            
        with todos_tab:
            todos = functions.get_todos(todos_file)
            for todo in todos:
                checkbox = st.checkbox(todo, key=todo)


with col2:
    add_button = st.button("Add TODO", use_container_width=True)
    edit_button = st.button("Edit TODO", use_container_width=True)
    complete_button  = st.button("Complete TODO", use_container_width=True)
    delete_button = st.button("Delete TODO", use_container_width=True)


if user_input:
    if add_button:
        todos = functions.get_todos(todos_file)
        todos.append(user_input + "\n")
        functions.write_todos(filepath=todos_file, content=todos)

        


st.session_state
