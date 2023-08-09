
from behave import given, when, then
from todo_list import ToDoListManager

# Inicializamos el objeto ToDoListManager en el contexto
@given('a set of todo list')
def step_impl(context):
    context.todo_manager = ToDoListManager()

@when('the user click on status of task')
def step_impl(context):
    # Implementa aquí la lógica para cuando el usuario hace clic en el estado de una tarea
    pass

@when('the user selects "Completed" Status')
def step_impl(context):
    # Implementa aquí la lógica para cuando el usuario selecciona el estado "Completado"
    pass

@then('the status of task "{task}" should change to "Completed" and be updated')
def step_impl(context, task):
    # Implementa aquí la lógica para verificar si el estado de la tarea ha cambiado a "Completado" y se ha actualizado
    pass

@when('the user clicks on "Delete" icon')
def step_impl(context):
    # Implementa aquí la lógica para cuando el usuario hace clic en el ícono "Eliminar"
    pass

@when('the user marks task "{task}" as incompleted')
def step_impl(context, task):
    context.todo_manager.mark_task_completed(task)

@then('the to-do list should show task "{task}" as incompleted')
def step_impl(context, task):
    found_task = any(t['description'] == task and not t['completed'] for t in context.todo_manager.tasks)
    assert found_task, f'Task "{task}" should not be marked as completed'

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        context.todo_manager.add_task({'description': row['Task'], 'completed': row['Status'] == 'Completed'})

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.todo_manager.mark_task_completed(task)

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_manager.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_manager.tasks) == 0, 'To-do list is not empty'

@given('the to-do list is empty')
def step_impl(context):
    context.todo_manager = ToDoListManager()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo_manager.add_task(task)
