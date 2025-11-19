## ✏️ UI Task — Update Item Screen

**S — Situation:**
Sometimes an item’s name, quantity or price changes after it has been added to the system. The user should be able to update these values easily without deleting and re-adding the item.

**T — Task:**
Create a CLI screen that allows the user to update an existing item’s quantity or price using `StorageService.update_item(name, new_quantity, new_price)`.

**A — Action:**

1. Open or create the file `UI/storage_ui.py`.

2. Define a function `show_update_item_screen(storage_service)` that:

   * Displays this layout:

     ```
     ===============================
               UPDATE ITEM
     ===============================
     Enter item name to update:
     Enter new quantity:
     Enter new price:
     -------------------------------
     ```
   * Reads user input using `input()`.
   * Calls:

     ```python
     result = storage_service.update_item(name, new_quantity, new_price)
     ```
   * Prints the returned message (for example, “Item updated successfully!” or “Error: Item not found.”).
   * Displays:

     ```
     --------------------------------------
     (Press Enter to return to menu)
     ```

     and waits for user confirmation before returning to `show_storage_menu(storage_service)`.

**R — Result:**
The user can modify an existing item’s quantity and price directly from the command line. The update operation interacts with the storage service, ensuring that database records are kept current and consistent without duplicate entries.
