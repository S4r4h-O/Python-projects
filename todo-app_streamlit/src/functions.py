import streamlit as st


def get_todos(filepath):
    with open(filepath, "r") as local_todos:
        local_todos = local_todos.readlines()
    return local_todos


def write_todos(filepath, content):
    with open(filepath, "w") as write_file:
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
        st.rerun()


def complete_todo(todo_to_complete):
    todo_to_complete = todo_to_complete
    todos = get_todos("todos.txt")
    # First, append the selected todo to the completed file
    completed_todos = get_todos("completed.txt")
    completed_todos.append(todo_to_complete)
    write_todos("completed.txt", completed_todos)
    # Then remove the todo from the todos file
    index = todos.index(todo_to_complete)
    todos.pop(index)
    write_todos("todos.txt", todos)
    st.rerun()


def delete_todo(todo_to_delete):
    todo_to_delete = todo_to_delete
    todos = get_todos(filepath="todos.txt")
    index = todos.index(todo_to_delete)
    todos.pop(index)
    write_todos("todos.txt", todos)
    st.rerun()
