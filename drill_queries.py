import sqlite3

def top_departments(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.name, SUM(e.salary) as total_salary
            FROM departments d
            JOIN employees e ON d.dept_id = e.dept_id
            GROUP BY d.name
            ORDER BY total_salary DESC
            LIMIT 3;
        """)
        return cursor.fetchall()

def employees_with_projects(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.name, p.name
            FROM employees e
            JOIN project_assignments pa ON e.emp_id = pa.emp_id
            JOIN projects p ON pa.project_id = p.project_id;
        """)
        return cursor.fetchall()

def salary_rank_by_department(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.name, d.name, e.salary,
                   RANK() OVER(PARTITION BY d.dept_id ORDER BY e.salary DESC) as rank
            FROM employees e
            JOIN departments d ON e.dept_id = d.dept_id
            ORDER BY d.name ASC, rank ASC;
        """)
        return cursor.fetchall()