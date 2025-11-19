## 🗑️ UI Task — Delete Item Screen

**S — Situation:**
When an item is no longer available or was added by mistake, the user should be able to remove it from the storage database. This maintains data accuracy and prevents clutter.

**T — Task:**
Create a CLI screen that allows the user to delete an existing item by name using `StorageService.delete_item(name)`.

**A — Action:**

1. Open or create the file `UI/storage_ui.py`.

2. Define a function `show_delete_item_screen(storage_service)` that:

   * Displays this layout:

     ```
     ===============================
               DELETE ITEM
     ===============================
     Enter item name to delete:
     -------------------------------
     ```
   * Reads the item name using `input()`.
   * Calls:

     ```python
     result = storage_service.delete_item(name)
     ```
   * Prints the result message, for example:

     * `"Item deleted successfully!"`
     * `"Error: Item not found."`
   * Then displays:

     ```
     --------------------------------------
     (Press Enter to return to menu)
     ```

     and returns to `show_storage_menu(storage_service)` after the user presses Enter.

**R — Result:**
The user can remove unwanted items by name through a simple command-line interface. The screen connects cleanly with the storage service, ensuring deleted items are removed from the database and the inventory remains accurate.
