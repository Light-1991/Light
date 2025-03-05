from helpers.database import Database


class EmployeeManager:
    def __init__(self):
        self.db = Database()

    def add_employee(self, name, age, department, salary):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO employees (name, age, department, salary) VALUES
                (%s,%s,%s,%s)
            """
            cursor.execute(query,(name, age, department, salary))
            conn.commit()
            print(f"Employee : {name} added successfully.")

        except Exception as e:
            print(f"Error Adding Employee: {e}")

        finally:
            self.db.close()

    def view_employees(self):
        conn = self.db.connect_database()

        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """
                SELECT * FROM employees
            """
            cursor.execute(query)
            employees = cursor.fetchall()

            print("\n---- Employees List ---------")

            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}, Salary: {emp[4]}")


        except Exception as e:
            print(f"Error Fetching Employees Record: {e}")

        finally:
            self.db.close()


    def search_employee(self, name=None, department=None):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """
                        SELECT * FROM employees WHERE name=%s OR department=%s
                    """
            cursor.execute(query, (name, department))
            employees = cursor.fetchall()

            if employees:
                print("\n---- Search Result ---------")

                for emp in employees:
                    print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}, Salary: {emp[4]}")
            else:
                print("\n------- No Record Found -----------")

        except Exception as e:
            print(f"Error Fetching Employee Record: {e}")

        finally:
            self.db.close()

    def update_employee(self):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """UPDATE employees SET name=%s, age=%s, department=%s, salary=%s WHERE id=%s"""
            cursor.execute(query,)
            conn.commit()

            print(f"successfully updated employee details")
        except Exception as e:
            print(f"Error updating Employee: {e}")

        finally:
            self.db.close()




