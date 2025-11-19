## 🗃️ UI Task — Storage Main Menu

**S — Situation:**
After the user successfully signs in, the system should display the storage management menu. This menu acts as the central hub for all item-related operations such as adding, viewing, searching, and deleting items.

**T — Task:**
Create a menu interface that lists all available storage operations and routes the user to the corresponding window or service when selected.

**A — Action:**

1. Create a new file `UI/storage_menu.py`.
2. Define a function `show_storage_menu()` that displays the following layout:

   ```
   ===============================
           STORAGE MANAGEMENT
   ===============================
   1. Add Item
   2. View All Items
   3. Search Item
   4. Update Item
   5. Delete Item
   6. Reports
   7. Logout
   -------------------------------
   Choose an option:
   ```
3. Handle user input using `input()`.

   * Option `1`: Call `show_add_item_screen()` from `UI/storage_ui.py`.
   * Option `2`: Call `show_view_all_items_screen()` from `UI/storage_ui.py`.
   * Option `3`: Call `show_search_item_screen()` from `UI/storage_ui.py`.
   * Option `4`: Call `show_update_item_screen()` from `UI/storage_ui.py`.
   * Option `5`: Call `show_delete_item_screen()` from `UI/storage_ui.py`.
   * Option `6`: Call `show_reports_menu()` (later implemented for low-stock, sorting, CSV export, etc.).
   * Option `7`: Return to the main menu (`UI/main_menu.show_main_menu()`).
4. Add simple input validation — if the input is invalid, display “Invalid option, please try again.” and show the menu again.

**R — Result:**
After logging in, users are directed to a clean, text-based menu where they can perform all item management operations. This menu serves as the central navigation point for the storage module and keeps the user workflow organized.
