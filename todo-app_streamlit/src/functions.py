def get_todos(filepath):
    with open(filepath, 'r') as local_todos:
        local_todos = local_todos.readlines()
    return local_todos


def write_todos(filepath, content):
    with open(filepath, 'w') as write_file:
        write_file.writelines(content)


