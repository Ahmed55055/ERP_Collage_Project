## 🔍 UI Task — Search Item Screen

**S — Situation:**
Users need a simple way to find specific items in the storage by name instead of scrolling through the full list. This helps confirm whether an item exists and view its details quickly.

**T — Task:**
Create a CLI screen that allows the user to enter an item name and displays matching items by calling `StorageService.search_item(name)`.

**A — Action:**

1. Open or create the file `UI/storage_ui.py`.

2. Define a function `show_search_item_screen(storage_service)` that:

   * Displays this layout:

     ```
     ===============================
               SEARCH ITEM
     ===============================
     Enter item name to search:
     -------------------------------
     ```
   * Reads user input using `input()`.
   * Calls:

     ```python
     results = storage_service.search_item(name)
     ```
   * If the returned list is not empty:

     * Display a formatted table of matching items:

       ```
       Item Name        Quantity        Price
       --------------------------------------
       Pen              50              3.25
       ```
   * If no results are found, print:

     ```
     No items found with that name.
     ```
   * At the end, display:

     ```
     --------------------------------------
     (Press Enter to return to menu)
     ```

     and return to `show_storage_menu(storage_service)` after pressing Enter.

**R — Result:**
The user can type an item’s name and instantly view all matching entries. The screen provides quick access to specific item details, improving usability and navigation within the CLI-based ERP system.

