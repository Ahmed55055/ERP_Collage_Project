# Service Task - Storage - Validate Item

## Task Description
In this task, you will implement the `_validate_item` method in the `StorageService` class. This is a private helper method that checks if an `ItemDto` object has valid data.

## What the Code Will Do
The `_validate_item` method will take an `ItemDto` object and check if its data is valid according to the rules. It should return `True` if the data is valid, `False` if any validation fails.

## Validation Rules
The method should check:
- The name should not be empty or only spaces (after stripping whitespace).
- The quantity should not be less than 0.
- The price should not be less than 0.

## Final Result and Behavior
The `_validate_item` method should:
1. Check if `dto.name.strip()` is empty. If yes, return `False`.
2. Check if `dto.quantity < 0`. If yes, return `False`.
3. Check if `dto.price < 0`. If yes, return `False`.
4. If all checks pass, return `True`.

## Implementation Steps
1. Open the file `src/storage/Service/StorageService.py`.
2. Find the `_validate_item` method (it currently has `pass` in it).
3. Implement the logic as described above.
4. Run the tests to make sure your implementation works correctly (there might be tests for validation in the future).

## How to Verify Your Code is Correct
To make sure your code works correctly, you can run all storage service tests using the terminal. Open a terminal in your project directory and run this command:

```
pytest tests/storage_service_test.py
```

This will run all tests for the storage service. If all tests pass, it means your implementation is correct. If any test fails, check your code and fix the issues.