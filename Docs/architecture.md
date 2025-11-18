# Project Architecture

## Overview

This is a Python-based data management application that uses SQLite for persistent storage. It implements a layered architecture with repository pattern for data access, service layer for business logic, and includes a command-line UI for storage management with user authentication. The application supports managing items in storage and user accounts, including CRUD operations and reporting.

## Components

### Database Layer

- **DatabaseConfig** (`database/config.py`): A configuration class that handles SQLite database connections. It provides methods for executing queries, fetching single rows, and fetching all rows. Supports both file-based databases (default: `storage.db`) and in-memory databases for testing.

### Data Access Layer (Repositories)

- **StorageRepository** (`storage/StorageRepository.py`): Implements CRUD operations for storage items. Uses the DatabaseConfig to interact with the `items` table.
- **UserRepository** (`user/Repository/UserRepository.py`): Implements CRUD operations for user accounts. Uses the DatabaseConfig to interact with the `users` table.

### Business Logic Layer (Services)

- **StorageService** (`storage/StorageService.py`): Provides business logic for storage operations, including validation and coordination of storage-related tasks. Depends on IStorageRepository.
- **UserService** (`user/Service/UserService.py`): Provides business logic for user management, including authentication and user account operations. Depends on IUserRepository.

### Data Transfer Objects (DTOs)

- **ItemDto** (`storage/dto.py`): A simple data class representing an item with attributes: name, quantity, and price.
- **UserDto** (`user/dto.py`): A simple data class representing a user with attributes: username, email, and password.

### Interfaces

- **IStorageRepository** (`storage/IStorageRepository.py`): Abstract base class defining the contract for storage data access operations.
- **IStorageService** (`storage/IStorageService.py`): Abstract base class defining the contract for storage business logic operations.
- **IUserRepository** (`user/Repository/IUserRepository.py`): Abstract base class defining the contract for user data access operations.
- **IUserService** (`user/Service/IUserService.py`): Abstract base class defining the contract for user business logic operations.

### User Interface

- **ScreensEnums** (`UI/ScreensEnums.py`): Defines enumerations for different UI screens, including main menu (sign-in/sign-up), storage operations (add, view, search, update, delete, reports), and logout.
- **Menu** (`UI/menu.py`): Provides mock command-line interface displaying various screens for storage management and user authentication operations, including adding items, viewing all items, searching for items, updating items, deleting items, and generating reports.

### Testing

- Unit tests are located in the `tests/` directory, including `storage_repository_test.py` and `user_repository_test.py`, using pytest for testing the repository classes.

## Database Schema

### Items Table
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
- `name` (TEXT UNIQUE)
- `quantity` (INTEGER)
- `price` (REAL)

### Users Table
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
- `username` (TEXT UNIQUE)
- `email` (TEXT UNIQUE)
- `password` (TEXT)

## Architecture Patterns

- **Repository Pattern**: Abstracts data access logic into repository classes.
- **Service Layer Pattern**: Encapsulates business logic in service classes, separating concerns from data access.
- **DTO Pattern**: Uses data transfer objects to encapsulate data structures.
- **Interface Segregation**: Uses abstract base classes to define contracts for repositories and services, promoting loose coupling.
- **Dependency Injection**: Services depend on repository interfaces, allowing for flexible and testable implementations.
- **Layered Architecture**: Separates concerns into database, data access, business logic, and UI layers.

## Dependencies

- `sqlite3` (built-in Python library for SQLite database operations)