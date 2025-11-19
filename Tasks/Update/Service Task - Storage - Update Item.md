# Service Task - Storage - Update Item

## Task Description
In this task, you will implement the `update` method in the `StorageService` class. This method is responsible for updating an existing item in the storage system.

## What the Code Will Do
The `update` method will take an `ItemDto` object and try to update the item with the same name in the storage. Before updating, it should check if an item with that name already exists. If it does not exist, the method should not update anything and return `False`. If the item exists, it should update it and return `True` if the update was successful, or `False` if it failed.

## What is ItemDto
`ItemDto` is a data transfer object that represents an item in the storage. It contains three pieces of information:
- `name`: The name of the item (a string, like "Apple")
- `quantity`: The quantity of the item (a number, like 10)
- `price`: The price of the item (a number, like 1.50)

## Repository Methods You Will Use
The `StorageService` has a repository injected into it (called `repo`). You will use these methods from the repository:

- `repo.exists(name)` -> This method checks if an item with the given name already exists in the storage. It returns `True` if the item exists, `False` if it does not.
- `repo.update(dto)` -> This method tries to update the item in the storage. It returns `True` if the item was updated successfully, `False` if there was an error.

## Final Result and Behavior
The `update` method should:
1. Trim the name in the dto: `dto.name = dto.name.strip()`.
2. First, validate the input data by calling `self._validate_item(dto)`. If it returns `False`, return `False`.
3. Check if the item already exists by calling `repo.exists(dto.name)`.
4. If `repo.exists(dto.name)` returns `False`, then return `False` (do not update the item).
5. If `repo.exists(dto.name)` returns `True`, then call `repo.update(dto)` and return whatever `repo.update(dto)` returns (either `True` or `False`).

This ensures that invalid data is rejected, only existing items are updated, and the method reports whether the operation was successful.

**Note:** Make sure to complete the "Service Task - Storage - Validate Item" task first, as this task depends on the `_validate_item` method being implemented.

## Implementation Steps
1. Open the file `src/storage/Service/StorageService.py`.
2. Find the `update` method (it currently has `pass` in it).
3. Implement the logic as described above.
4. Run the tests to make sure your implementation works correctly.

## How to Verify Your Code is Correct
To make sure your code works correctly, you can run the specific tests for updating items using the terminal. Open a terminal in your project directory and run this command:

```
pytest -m update_item
```

This command will run only the tests related to updating items in the storage service. If all tests pass, it means your implementation is correct. If any test fails, check your code and fix the issues.