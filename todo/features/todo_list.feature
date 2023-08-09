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

  Scenario: Clear the entire to do list
    Given a set of todo list
      | TASK                 | DATE       | STATUS      | PRIORITY |
      | Clean the car        | 31/07/2023 | In Progress | Medium   |
      | Buy the bottle water | 30/07/2023 | In Progress | Low      |
    When the user clicks on "Delete" icon
    Then the to-do list should be empty

 