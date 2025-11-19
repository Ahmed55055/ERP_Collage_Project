## 📋 UI Task — View All Items Screen

**S — Situation:**
The user should be able to see all items currently stored in the system. This allows them to verify the data and confirm that items have been successfully added to the database.

**T — Task:**
Create a simple CLI screen that retrieves and displays all stored items using `StorageService.get_all_items()`.

**A — Action:**

1. Open or create the file `UI/storage_ui.py`.

2. Define a function `show_view_all_items_screen(storage_service)` that:

   * Displays this layout:

     ```
     ======================================
                 VIEW ALL ITEMS
     ======================================
     Item Name        Quantity        Price
     --------------------------------------
     ```
   * Calls:

     ```python
     items = storage_service.get_all_items()
     ```
   * Loops through the returned list of items (each being an object or dictionary) and prints their details in aligned columns.
     Example:

     ```
     Pen               50              3.25
     Notebook          20              15.00
     ```
   * If no items exist, print:

     ```
     No items found in storage.
     ```
   * After displaying the list, print:

     ```
     --------------------------------------
     (Press Enter to return to menu)
     ```
   * Wait for the user to press Enter, then return to `show_storage_menu(storage_service)`.

**R — Result:**
The user can view a clear, formatted list of all items stored in the system. The screen shows each item’s name, quantity, and price, giving a quick overview of inventory without requiring any manual database checks.
