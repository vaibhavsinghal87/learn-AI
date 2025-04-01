import os
import shutil

active_db_file = 'app.db'
backup_db_file = 'backup.db'

def backup_database():
    try:
        if not os.path.exists(active_db_file):
            raise FileNotFoundError(f"{active_db_file} does not exist.")
        shutil.copyfile(active_db_file, backup_db_file)
        print(f"Backup of {active_db_file} created as {backup_db_file}.")
    except FileNotFoundError as fnf_error:
        print(f"File not found error: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Permission error: {perm_error}")
    except Exception as e:
        print(f"Error creating backup: {e}")

def restore_database():
    try:
        shutil.copyfile(backup_db_file, active_db_file)
        print(f"Restored {active_db_file} from {backup_db_file}.")
    except Exception as e:
        print(f"Error restoring backup: {e}")

def main():
    print("1. Backup Database")
    print("2. Restore Database")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        backup_database()
    elif choice == '2':
        restore_database()
    elif choice == '3':
        print("Exiting...")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    # Example usage
    main()
    