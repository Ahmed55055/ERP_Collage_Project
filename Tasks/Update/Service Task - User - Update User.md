# Service Task - User - Update User

## Task Description
In this task, you will implement the `update` method in the `UserService` class. This method is responsible for updating an existing user in the system.

## What the Code Will Do
The `update` method will take a `UserDto` object and try to update the user with the same username in the system. Before updating, it should check if a user with that username already exists. If it does not exist, the method should not update anything and return `False`. If the user exists, it should update it and return `True` if the update was successful, or `False` if it failed.

## What is UserDto
`UserDto` is a data transfer object that represents a user. It contains three pieces of information:
- `username`: The username of the user (a string, like "john_doe")
- `email`: The email address of the user (a string, like "john@example.com")
- `password`: The password of the user (a string)

## Repository Methods You Will Use
The `UserService` has a repository injected into it (called `repo`). You will use these methods from the repository:

- `repo.exists(username)` -> This method checks if a user with the given username already exists. It returns `True` if the user exists, `False` if it does not.
- `repo.update(dto)` -> This method tries to update the user in the system. It returns `True` if the user was updated successfully, `False` if there was an error.

## Final Result and Behavior
The `update` method should:
1. Trim the username in the dto: `dto.username = dto.username.strip()`.
2. Check if the user already exists by calling `repo.exists(dto.username)`.
3. If `repo.exists(dto.username)` returns `False`, then return `False` (do not update the user).
4. If `repo.exists(dto.username)` returns `True`, then call `repo.update(dto)` and return whatever `repo.update(dto)` returns (either `True` or `False`).

This ensures that only existing users are updated, and the method reports whether the operation was successful.

## Implementation Steps
1. Open the file `src/user/Service/UserService.py`.
2. Find the `update` method (it currently has `pass` in it).
3. Implement the logic as described above.
4. Run the tests to make sure your implementation works correctly.

## How to Verify Your Code is Correct
To make sure your code works correctly, you can run the user service tests using the terminal. Open a terminal in your project directory and run this command:

```
pytest tests/user_service_test.py
```

This will run all tests for the user service. If all tests pass, it means your implementation is correct. If any test fails, check your code and fix the issues.