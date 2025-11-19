# Service Task - Storage - Add Item

## Task Description
In this task, you will implement the `create` method in the `StorageService` class. This method is responsible for adding a new item to the storage system.

## What the Code Will Do
The `create` method will take an `ItemDto` object and try to add it to the storage. Before adding, it should check if an item with the same name already exists. If it does, the method should not add the item and return `False`. If the item does not exist, it should add the item and return `True` if the addition was successful, or `False` if it failed.

## What is ItemDto
`ItemDto` is a data transfer object that represents an item in the storage. It contains three pieces of information:
- `name`: The name of the item (a string, like "Apple")
- `quantity`: The quantity of the item (a number, like 10)
- `price`: The price of the item (a number, like 1.50)

## Repository Methods You Will Use
The `StorageService` has a repository injected into it (called `repo`). You will use these methods from the repository:

- `repo.exists(name)` -> This method checks if an item with the given name already exists in the storage. It returns `True` if the item exists, `False` if it does not.
- `repo.create(dto)` -> This method tries to add the item to the storage. It returns `True` if the item was added successfully, `False` if there was an error (like if the item already exists or some other problem).

## Final Result and Behavior
The `create` method should:
1. Trim the name in the dto: `dto.name = dto.name.strip()`.
2. First, validate the input data by calling `self._validate_item(dto)`. If it returns `False`, return `False`.
3. Check if the item already exists by calling `repo.exists(dto.name)`.
4. If `repo.exists(dto.name)` returns `True`, then return `False` (do not add the item).
5. If `repo.exists(dto.name)` returns `False`, then call `repo.create(dto)` and return whatever `repo.create(dto)` returns (either `True` or `False`).

This ensures that invalid data is rejected, duplicate items are not added, and the method reports whether the operation was successful.

**Note:** Make sure to complete the "Service Task - Storage - Validate Item" task first, as this task depends on the `_validate_item` method being implemented.

## Implementation Steps
1. Open the file `src/storage/Service/StorageService.py`.
2. Find the `create` method (it currently has `pass` in it).
3. Implement the logic as described above.
4. Run the tests to make sure your implementation works correctly.

## How to Verify Your Code is Correct
To make sure your code works correctly, you can run the specific tests for adding items using the terminal. Open a terminal in your project directory and run this command:

```
pytest -v -m add_item
```

This command will run only the tests related to adding items in the storage service. If all tests pass, it means your implementation is correct. If any test fails, check your code and fix the issues.