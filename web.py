import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app is ti increase your productivity')
st.write('Hello world')


for index, todo in enumerate(todos):
    # Use the index (i) as the key to make each checkbox unique
    checkbox =st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='new_todo', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')

print('Hello')
print(checkbox)

st.session_state