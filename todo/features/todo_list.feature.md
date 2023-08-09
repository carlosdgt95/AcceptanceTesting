Feature: Mark a task as completed.

    @taskCompleted
    Scenario: Change status of task as completed.
        Given a set of todo list
        | TASK                 | DATE       | STATUS      | PRIORITY|
        | Clean the car        | 31/07/2023 | In Progress | Medium  |
        | Buy the bottle water | 30/07/2023 | In Progress | Low     |
        Given the user click on status of task
        When the user select "Completed" Status
        Then the status of task change to "Completed" and updated it.
        | TASK                 | DATE       | STATUS       | PRIORITY |
        | Clean the car        | 31/07/2023 | Completed    | Medium   |
        | Buy the bottle water | 30/07/2023 | In Progress  | Low      |

Feature: Clear the entire to do list.
    @clearTodo
        Scenario: Delete all tasks of to do list.
            Given a set of todo list
            | TASK                 | DATE       | STATUS      | PRIORITY|
            | Clean the car        | 31/07/2023 | In Progress | Medium  |
            | Buy the bottle water | 30/07/2023 | In Progress | Low     |
            When the user click on "Delete" icon
            Then the todo list should be empty.
            | TASK                 | DATE       | STATUS       | PRIORITY |


Feature: Change status of the task.
    @changeStatus
        Scenario: Change status of task.
            Given a set of todo list
            | TASK                 | DATE       | STATUS      | PRIORITY|
            | Clean the car        | 31/07/2023 | In Progress | Medium  |
            | Buy the bottle water | 30/07/2023 | In Progress | Low     |
            Given the user click on status of task
            When the user select "No Completed" Status
            Then the status of task change to "Completed" and updated it.
            | TASK                 | DATE       | STATUS          | PRIORITY |
            | Clean the car        | 31/07/2023 | No Completed    | Medium   |
            | Buy the bottle water | 30/07/2023 | In Progress     | Low      |


Feature: Delete task from to do list.
    @deleteTask
        Scenario: Remove task of to do list.
            Given a set of todo list
            | TASK                 | DATE       | STATUS      | PRIORITY|
            | Clean the car        | 31/07/2023 | In Progress | Medium  |
            | Buy the bottle water | 30/07/2023 | In Progress | Low     |
            When the user click on "Delete" icon on "Clean the car" task
            Then the task "Clean the car" should not be appear on todo list.
            | TASK                 | DATE       | STATUS       | PRIORITY |
            | Buy the bottle water | 30/07/2023 | In Progress  | Low      |