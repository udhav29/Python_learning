import sqlite3
import hashlib
import getpass
import os


class UserManagementSystem:
    def __init__(self, db_name="users.db"):
        """Initialize the user management system with database setup."""
        self.db_name = db_name
        self.current_user = None
        self.init_database()

    def init_database(self):
        """Initialize the SQLite database and create users table if it doesn't exist."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    is_logged_in INTEGER DEFAULT 0
                )
            ''')

            conn.commit()
            conn.close()
            print("Database initialized successfully.")
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")

    def hash_password(self, password):
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self):
        """Register a new user with username and password."""
        print("\n--- User Registration ---")

        username = input("Enter username: ").strip()
        if not username:
            print("Error: Username cannot be empty.")
            return

        # Check if username already exists
        if self.username_exists(username):
            print("Error: Username already exists. Please choose a different username.")
            return

        password = getpass.getpass("Enter password: ")
        if not password:
            print("Error: Password cannot be empty.")
            return

        confirm_password = getpass.getpass("Confirm password: ")
        if password != confirm_password:
            print("Error: Passwords do not match.")
            return

        # Hash password and store user
        hashed_password = self.hash_password(password)

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO users (username, password, is_logged_in)
                VALUES (?, ?, 0)
            ''', (username, hashed_password))

            conn.commit()
            conn.close()
            print("Registration successful! You can now log in.")

        except sqlite3.Error as e:
            print(f"Registration error: {e}")

    def username_exists(self, username):
        """Check if username already exists in database."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
            result = cursor.fetchone()

            conn.close()
            return result is not None

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def login_user(self):
        """Log in a user with username and password."""
        print("\n--- User Login ---")

        if self.current_user:
            print(f"Error: User '{self.current_user}' is already logged in.")
            return

        username = input("Enter username: ").strip()
        if not username:
            print("Error: Username cannot be empty.")
            return

        password = getpass.getpass("Enter password: ")

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Check if user exists and verify password
            cursor.execute('SELECT username, password, is_logged_in FROM users WHERE username = ?', (username,))
            result = cursor.fetchone()

            if not result:
                print("Error: Username not found.")
                conn.close()
                return

            stored_username, stored_password, is_logged_in = result

            # Check if user is already logged in
            if is_logged_in == 1:
                print("Error: User is already logged in from another session.")
                conn.close()
                return

            # Verify password
            hashed_input_password = self.hash_password(password)
            if hashed_input_password != stored_password:
                print("Error: Incorrect password.")
                conn.close()
                return

            # Update login status
            cursor.execute('UPDATE users SET is_logged_in = 1 WHERE username = ?', (username,))
            conn.commit()
            conn.close()

            self.current_user = username
            print(f"Login successful! Welcome, {username}.")

        except sqlite3.Error as e:
            print(f"Login error: {e}")

    def logout_user(self):
        """Log out the current user."""
        print("\n--- User Logout ---")

        if not self.current_user:
            print("Error: No user is currently logged in.")
            return

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Update login status
            cursor.execute('UPDATE users SET is_logged_in = 0 WHERE username = ?', (self.current_user,))
            conn.commit()
            conn.close()

            print(f"User '{self.current_user}' logged out successfully.")
            self.current_user = None

        except sqlite3.Error as e:
            print(f"Logout error: {e}")

    def change_password(self):
        """Change password for the currently logged-in user."""
        print("\n--- Change Password ---")

        if not self.current_user:
            print("Error: You must be logged in to change your password.")
            return

        # Verify current password
        current_password = getpass.getpass("Enter current password: ")

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Get current password hash
            cursor.execute('SELECT password FROM users WHERE username = ?', (self.current_user,))
            result = cursor.fetchone()

            if not result:
                print("Error: User not found.")
                conn.close()
                return

            stored_password = result[0]
            hashed_current_password = self.hash_password(current_password)

            if hashed_current_password != stored_password:
                print("Error: Current password is incorrect.")
                conn.close()
                return

            # Get new password
            new_password = getpass.getpass("Enter new password: ")
            if not new_password:
                print("Error: New password cannot be empty.")
                conn.close()
                return

            confirm_new_password = getpass.getpass("Confirm new password: ")
            if new_password != confirm_new_password:
                print("Error: New passwords do not match.")
                conn.close()
                return

            # Update password
            hashed_new_password = self.hash_password(new_password)
            cursor.execute('UPDATE users SET password = ? WHERE username = ?',
                           (hashed_new_password, self.current_user))
            conn.commit()
            conn.close()

            print("Password changed successfully!")

        except sqlite3.Error as e:
            print(f"Password change error: {e}")

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "=" * 40)
        print("    USER MANAGEMENT SYSTEM")
        print("=" * 40)
        if self.current_user:
            print(f"Logged in as: {self.current_user}")
        else:
            print("Not logged in")
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change Password")
        print("5. Exit")
        print("-" * 40)

    def run(self):
        """Main program loop."""
        print("Welcome to the User Management System!")

        while True:
            self.display_menu()

            try:
                choice = input("Enter your choice (1-5): ").strip()

                if choice == '1':
                    self.register_user()
                elif choice == '2':
                    self.login_user()
                elif choice == '3':
                    self.logout_user()
                elif choice == '4':
                    self.change_password()
                elif choice == '5':
                    # Logout current user before exiting
                    if self.current_user:
                        self.logout_user()
                    print("Thank you for using the User Management System. Goodbye!")
                    break
                else:
                    print("Error: Invalid choice. Please enter a number between 1 and 5.")

            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Logging out...")
                if self.current_user:
                    self.logout_user()
                print("Goodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


def main():
    """Main function to start the user management system."""
    system = UserManagementSystem()
    system.run()


if __name__ == "__main__":
    main()