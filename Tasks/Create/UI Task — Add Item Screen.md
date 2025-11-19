## ➕ UI Task — Add Item Screen

**S — Situation:**
The user should be able to add new items to the storage by entering an item name, quantity, and price. The UI must communicate with the `StorageService` class, which contains the logic for validation and repository interaction.

**T — Task:**
Create a user interface screen that gathers item information from the user, then uses `StorageService.add_item(name, quantity, price)` to save the data after validation.

**A — Action:**

1. Open or create the file `UI/storage_ui.py`.

2. Define a function `show_add_item_screen(storage_service)` that:

   * Displays this layout:

     ```
     ===============================
               ADD ITEM
     ===============================
     Enter item name:
     Enter quantity:
     Enter price:
     -------------------------------
     ```
   * Takes user input for name, quantity, and price using `input()`.
   * Calls:

     ```python
     result = storage_service.add_item(name, quantity, price)
     ```
   * Prints the result message (success or error).
   * Waits for the user to press Enter, then return.

**R — Result:**
The user can easily add new items through a text-based screen. Input is validated through `StorageService`, ensuring clean database entries and separation between UI and business logic layers.
