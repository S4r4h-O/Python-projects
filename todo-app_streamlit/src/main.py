import streamlit as st
import functions
from pathlib import Path

todos_file = Path("todos.txt")
if not todos_file.exists():
    functions.write_todos("todos.txt", "")

completed_file = Path("completed.txt")
if not completed_file.exists():
    functions.write_todos("completed.txt", "")

# st.set_page_config(layout="wide")
st.title("My TODOS App")

with st.sidebar:
    st.write("""
             This is an improved version of the Streamlit app
             taught by Ardit Sulce.
             """)
    st.image("assets/python_logo.png")


user_input = st.text_input(label="Write a todo")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.write("Your TODOS")
        todos_tab, completed_tab = st.tabs(["TODOS", "Completed"])

        # Todo tab to show only the unfinished tasks    
        with todos_tab:
            todos = functions.get_todos(todos_file)
            for todo in todos:
                # Creates checkboxes for all the todos
                checkbox = st.checkbox(todo, key=todo)
                if checkbox:
                    # If some some checkbox is checked, a popover is open only to the
                    # selected todo
                    popover = st.popover("Item actions")
                    complete = popover.button("Complete", key=f"cb_{todo}", 
                                              use_container_width=True)
                    edit = popover.button("Edit", key=f"eb_{todo}", 
                                          use_container_width=True)
                    delete = popover.button("Delete TODO", key=f"db_{todo}", 
                                            use_container_width=True)
                    
                    if edit:
                        functions.edit_todo(selected_todo=todo)

                    elif complete:
                        functions.complete_todo(todo)

                    elif delete:
                        functions.delete_todo(todo)
        
        # Tab to show only the finished tasks
        with completed_tab:
            completed_todos = functions.get_todos(completed_file)
            for completed in completed_todos:
                st.write(completed)

with col2:
    add_button = st.button("Add TODO", use_container_width=True)

if user_input:
    if add_button:
        todos = functions.get_todos(todos_file)
        todos.append(user_input + "\n")
        functions.write_todos(filepath=todos_file, content=todos)
        st.rerun()
