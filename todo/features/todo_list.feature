Feature: To-Do List Manager

  Scenario: Change status of task as completed
    Given a set of todo list
      | TASK                 | DATE       | STATUS      | PRIORITY |
      | Clean the car        | 31/07/2023 | In Progress | Medium   |
      | Buy the bottle water | 30/07/2023 | In Progress | Low      |
    When the user click on status of task
    And the user selects "Completed" Status
    Then the status of task "Clean the car" should change to "Completed" and be updated
      | TASK                 | DATE       | STATUS    | PRIORITY |
      | Clean the car        | 31/07/2023 | Completed | Medium   |
      | Buy the bottle water | 30/07/2023 | In Progress | Low    |

  Scenario: Clear the entire to do list
    Given a set of todo list
      | TASK                 | DATE       | STATUS      | PRIORITY |
      | Clean the car        | 31/07/2023 | In Progress | Medium   |
      | Buy the bottle water | 30/07/2023 | In Progress | Low      |
    When the user clicks on "Delete" icon
    Then the to-do list should be empty
  # Escenario adicional: Agregar una tarea y marcarla como incompleted
  Scenario: Add a task and mark it as incompleted
    Given the to-do list is empty
    When the user adds a task "Call doctor"
    And the user marks task "Call doctor" as incompleted
    Then the to-do list should show task "Call doctor" as incompleted

  # Escenario adicional: Marcar una tarea como incompleted
  Scenario: Mark a task as incompleted
    Given the to-do list contains tasks:
      | Task          | Status   |
      | Buy groceries | Completed |
    When the user marks task "Buy groceries" as incompleted
    Then the to-do list should show task "Buy groceries" as incompleted