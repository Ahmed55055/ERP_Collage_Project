## 🪟 UI Task — Main Menu (Sign In / Sign Up)

**S — Situation:**
The system needs an entry point where users can either create a new account or log in before accessing storage operations. This is the first screen the user sees when running the program.

**T — Task:**
Create a main menu that displays two options — **Sign In** and **Sign Up** — and routes the user to the correct screen based on their choice.

**A — Action:**

1. Create a new file: `UI/main_menu.py`.
2. Define a function `show_main_menu()` that:

   * Displays the following layout:

     ```
     ===============================
           STORAGE MANAGEMENT
     ===============================
     1. Sign In
     2. Sign Up
     3. Exit
     -------------------------------
     Choose an option:
     ```
   * Takes user input using `input()`.
   * Handle invalid input by re-displaying the menu.
   * return the value user choose
3. Make sure this function runs first when the program starts (e.g., from `main.py`).

**R — Result:**
When the program starts, users see a simple menu allowing them to sign in, sign up, or exit. This provides a clear and friendly entry point to the system and links user authentication to the rest of the ERP.
