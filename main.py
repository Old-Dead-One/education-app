from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///education.db", echo=True)

conn = engine.connect()

conn.close()

create_students_table = """
    CREATE TABLE students(
    student_id integer PRIMARY KEY AUTOINCREMENT,
    f_name varchar(32),
    l_name varchar(64),
    email text,
    enrollment_year integer
);
"""

insert_student = """
    INSERT INTO students (f_name, l_name, email, enrollment_year)
    VALUES ('Alan', 'McGraw','olddeadone@protonmail.com', 2024)
"""

with engine.connect() as conn:
    conn.execute(text(create_students_table))
    conn.execute(text(insert_student))
    conn.commit()
    result = conn.execute(text("SELECT * FROM students"))
    print (result.all())

