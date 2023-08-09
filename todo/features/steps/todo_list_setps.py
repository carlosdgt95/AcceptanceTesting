from behave import given, when, then
from todo_list import ToDoListManager

# Inicializamos el objeto ToDoListManager en el contexto
@given('the to-do list is empty')
def step_impl(context):
    context.todo_manager = ToDoListManager()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo_manager.add_task({'description': task, 'completed': False})

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    found_task = any(t['description'] == task for t in context.todo_manager.tasks)
    assert found_task, f'Task "{task}" not found in the to-do list'

@when('the user lists all tasks')
def step_impl(context):
    context.output = ""
    for task in context.todo_manager.tasks:
        context.output += task['description'] + "\n"

@then('the output should contain:')
def step_impl(context):
    assert context.text.strip() == context.output.strip()

@given('the to-do list contains tasks:')
def step_impl(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        context.todo_manager.add_task({'description': row['Task'], 'completed': row['Status'] == 'Completed'})

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.todo_manager.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in context.todo_manager.tasks:
        if t['description'] == task:
            assert t['completed'], f'Task "{task}" not marked as completed'

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_manager.tasks) == 0, 'To-do list is not empty'
