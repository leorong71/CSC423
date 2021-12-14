import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor
query = """
    CREATE TABLE Department ( Department_name varchar(255) NOT NULL CHECK ( Department_name LIKE '%Department%') PRIMARY KEY, 
    Chair_name varchar(255), 
    Num_faculty int);
    """

# Execute query, the result is stored in cursor
cursor.execute(query)
query = """
    CREATE TABLE Major ( Code varchar(3) NOT NULL CHECK( length(Code)=3 ) PRIMARY KEY, 
    Major_name varchar(255), 
    Department_name varchar(255),
    Foreign Key (Department_name) references Department ( Department_name ) );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)
query = """
    CREATE TABLE Student  ( Student_id int NOT NULL PRIMARY KEY, 
    Student_name varchar(255), 
    Ini_name_student varchar(255) CHECK (length(Ini_name_student)>1) );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)
query = """
    CREATE TABLE Event  ( Event_id int PRIMARY KEY, 
    Event_name varchar(255), 
    Start_date date CHECK (Start_Date > date '2021-12-9'),
    End_date date CHECK (End_Date > date '2021-12-9'),
    CHECK (End_date >Start_date) );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)
query = """
    CREATE TABLE Event_Student ( Event_id int NOT NULL, 
    Student_id int NOT NULL,
    PRIMARY KEY(Event_id, Student_id),
    Foreign Key (Event_id) references Event ( Event_id ) ON DELETE CASCADE,
    Foreign Key (Student_id) references Student ( Student_id ) ON DELETE CASCADE );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)
query = """
    CREATE TABLE Event_Detail ( Event_id int,  
    Department_name varchar(255),
    PRIMARY KEY(Event_id, Department_name),
    Foreign Key (Event_id) references Event ( Event_id )  ON DELETE SET NULL,
    Foreign Key (Department_name) references Department ( Department_name ) ON DELETE CASCADE );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)
query = """
    CREATE TABLE Student_Detail  ( Student_id int, 
    Code varchar(255),
    PRIMARY KEY(Student_id, Code),
    Foreign Key (Student_id) references Student ( Student_id ) ON DELETE CASCADE,
    Foreign Key (Code) references Major ( Code ) ON DELETE CASCADE );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Department
    VALUES ('ADepartment', 'A', 1);
    """
cursor.execute(query)
query = """
    INSERT INTO Department
    VALUES ('BDepartment', 'B', 2);
    """
cursor.execute(query)
query = """
    INSERT INTO Department
    VALUES ('CDepartment', 'C', 3);
    """
cursor.execute(query)
query = """
    INSERT INTO Department
    VALUES ('DDepartment', 'D', 4);
    """
cursor.execute(query)
query = """
    INSERT INTO Department
    VALUES ('EDepartment', 'E', 5);
    """
cursor.execute(query)

query = """
    INSERT INTO Major
    VALUES ('AAA', 'A',  'ADepartment');
    """
cursor.execute(query)
query = """
    INSERT INTO Major
    VALUES ('BBB', 'B',  'BDepartment');
    """
cursor.execute(query)
query = """
    INSERT INTO Major
    VALUES ('CCC', 'C',  'CDepartment');
    """
cursor.execute(query)
query = """
    INSERT INTO Major
    VALUES ('DDD', 'D',  'DDepartment');
    """
cursor.execute(query)
query = """
    INSERT INTO Major
    VALUES ('EEE', 'E',  'EDepartment');
    """
cursor.execute(query)

query = """
    INSERT INTO Student
    VALUES (1, 'AA', 'AA');
    """
cursor.execute(query)
query = """
    INSERT INTO Student
    VALUES (2, 'BB', 'BB');
    """
cursor.execute(query)
query = """
    INSERT INTO Student
    VALUES (3, 'CC', 'CC');
    """
cursor.execute(query)
query = """
    INSERT INTO Student
    VALUES (4, 'DD', 'DD');
    """
cursor.execute(query)
query = """
    INSERT INTO Student
    VALUES (5, 'EE', 'EE');
    """
cursor.execute(query)

query = """
    INSERT INTO Event
    VALUES (1, 'A', DATE'2021-12-10', DATE'2021-12-11');
    """
cursor.execute(query)
query = """
    INSERT INTO Event
    VALUES (2, 'B', DATE'2021-12-10', DATE'2021-12-11');
    """
cursor.execute(query)
query = """
    INSERT INTO Event
    VALUES (3, 'C', DATE'2021-12-10', DATE'2021-12-11');
    """
cursor.execute(query)
query = """
    INSERT INTO Event
    VALUES (4, 'D', DATE'2021-12-10', DATE'2021-12-11');
    """
cursor.execute(query)
query = """
    INSERT INTO Event
    VALUES (5, 'E', DATE'2021-12-10', DATE'2021-12-11');
    """
cursor.execute(query)

query = """
    INSERT INTO Event_Student
    VALUES (1,1);
    """
cursor.execute(query)
query = """
    INSERT INTO Event_Student
    VALUES (2,2);
    """
cursor.execute(query)
query = """
    INSERT INTO Event_Student
    VALUES (3,3);
    """
cursor.execute(query)
query = """
    INSERT INTO Event_Student
    VALUES (4,4);
    """
cursor.execute(query)
query = """
    INSERT INTO Event_Student
    VALUES (5,5);
    """
cursor.execute(query)

query = """
    INSERT INTO Event_Detail
    VALUES (1,'ADepartment');
    """
cursor.execute(query)
query = """
    INSERT INTO Event_Detail
    VALUES (2,'BDepartment');
    """
cursor.execute(query)
query = """
    INSERT INTO Event_Detail
    VALUES (3,'CDepartment');
    """
cursor.execute(query)
query = """
    INSERT INTO Event_Detail
    VALUES (4,'DDepartment');
    """
cursor.execute(query)
query = """
    INSERT INTO Event_Detail
    VALUES (5,'EDepartment');
    """
cursor.execute(query)

query = """
    INSERT INTO Student_Detail
    VALUES (1,'AAA');
    """
cursor.execute(query)
query = """
    INSERT INTO Student_Detail
    VALUES (2,'BBB');
    """
cursor.execute(query)
query = """
    INSERT INTO Student_Detail
    VALUES (3,'CCC');
    """
cursor.execute(query)
query = """
    INSERT INTO Student_Detail
    VALUES (4,'DDD');
    """
cursor.execute(query)
query = """
    INSERT INTO Student_Detail
    VALUES (5,'EEE');
    """
cursor.execute(query)



# Select data
#Question1 1.	List the event_id of the event hosted by the Adepartment.
query = """
    SELECT Event_id
    FROM Event_Detail
    WHERE Department_name = 'ADepartment'
    """
cursor.execute(query)
#Question2 2.	List all the detail of the event hosted by Bdepartment or Cdepartment.
query = """
    SELECT e.*
    FROM Event_Detail d, Event e
    WHERE e.Event_id = d.Event_id and (d.Department_name = 'BDepartment' or d.Department_name = 'CDepartment')
    """
cursor.execute(query)
#Question3 3.	List all the detail of the students attended the event hosted by Ddepartment.
query = """
    SELECT s.*
    FROM Event_Detail d, Event_Student e, Student
    WHERE e.Event_id = d.Event_id and s.Student_id = e.Student_id and d.Department_name = 'DDepartment'
    """
cursor.execute(query)
#Question4 4.	List all the majors in the EDepartment.
query = """
    SELECT *
    FROM Major
    WHERE Department_name = 'EDepartment'
    """
cursor.execute(query)
#Question5 5.	List the end date of events which the students whose major are in Adepartment attended.
query = """
    SELECT e.Event_id, e.End_date
    FROM Event_Student s, Major m, Student_Detail d, Event e
    WHERE m.Department_name = 'ADepartment' and m.Code = d.Code and d.Student_id = s.Student_id and s.Event_id = e.event_id
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
