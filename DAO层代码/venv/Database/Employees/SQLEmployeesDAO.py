from Employees import Employees
from EmployeesDAO import EmployeesDAO


class SQLEmployeesDAO(EmployeesDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_employees(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        employees = []
        for row in rows:
            employee = Employees(row[0], row[1], row[2], row[3], row[4])
            employees.append(employee)
        return employees

    def create_employees(self, employee):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (employee.employee_id, employee.employee_name, employee.contact_info, employee.roleplay, employee.other_info))
        self.conn.commit()
