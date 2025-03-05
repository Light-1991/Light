from helpers.database import Database
from helpers.employee_manager import EmployeeManager
from models.admin import Admin
from models.users import User

def main():
    while True:
        print("\n Employee Management System")
        print("1. Login")
        print("2. Migrate Database")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            # if(username == 'admin'):
            #     user = Admin(username, password)
            # else:
            #     user = User(username, password)

            user = Admin(username, password) if username == 'admin' else User(username, password)
            if not user.authenticate():
                print("Invalid Username and Password.")
                continue

            employee_manager = EmployeeManager()

            while True:
                print("\n --- Employee Management System ---")
                print("1. Add Employee")
                print("2. View Employee")
                print("3. Search Employee")
                print("4. Update Employee")
                print("5. Delete Employee")
                print("6. View Salary Statistics")
                print("7. Add User (Admin Only)")
                print("8. Export to CSV")
                print("9. Logout")

                option = input("\n Select Option: ")

                if option == "1":
                    name = input("Enter employee name: ")
                    age = int(input("Enter employee age: "))
                    department = input("Enter employee department: ")
                    salary = float(input("Enter employee salary: "))

                    employee_manager.add_employee(name, age, department, salary)

                elif option == "2":
                    employee_manager.view_employees()

                elif option == "3":
                    name = input("Enter employee name (or leave blank): ")
                    department = input("Enter employee department (or leave blank): ")
                    employee_manager.search_employee(name or None, department or None)


                elif option == "4":
                    emp_id = int(input("Enter employee ID to update: "))
                    name = input("Enter new name")
                    age = int(input("Enter new age"))
                    department = input("Enter new department")
                    salary = float(input("Enter new salary"))
                    employee_manager.update_employee(emp_id, name, age, department, salary)

                elif option == "5":
                    pass
                elif option == "6":
                    pass
                elif option == "7":
                    pass
                elif option == "8":
                    pass
                elif option == "9":
                    print("Logging Out...")
                    break
                else:
                    print("Invalid Option, Please try again.")

        elif choice == "2":
            database = Database()
            database.setup_database()

        elif choice == "3":
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
