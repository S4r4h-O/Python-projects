import streamlit as st


def get_todos(filepath):
    with open(filepath, 'r') as local_todos:
        local_todos = local_todos.readlines()
    return local_todos


def write_todos(filepath, content):
    with open(filepath, 'w') as write_file:
        write_file.writelines(content)


# This function uses the @st.dialog decorator
@st.dialog("Edit your todo")
def edit_todo(selected_todo):
    new_todo = st.text_input("Enter your new todo") + "\n"
    if st.button("Edit"):
        todos = get_todos("todos.txt")
        index = todos.index(selected_todo)
        todos[index] = new_todo
        write_todos(content=todos, filepath="todos.txt")
        # Define the key 'todo_to_edit' as None every time we call the function, so we can reassign it as the variable todo later
        st.session_state.todo_to_edit = None
        st.rerun()
