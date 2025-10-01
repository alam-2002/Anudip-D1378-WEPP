-- LAB 4 
-- Lab 1: 
-- Use the Student management system Database and table from our previous lab and write a sql query to achieve the below scenario. 
-- Assume you are managing a university database that tracks student enrollments in various courses. 
-- You have two tables, "Student" and "Enrollment". 
-- The goal is to retrieve information about each student's ID, first name, last name, and their enrollment details, including the enrollment ID and the associated course ID. Hint:Use inner join to retrieve data. 
-- Submission: Create an SQL script file containing your solutions for all tasks (queries). 
-- Name the file "lab_assignment1.sql" Provide comments above each query to indicate the query's purpose


-- Use the StudentManagementSystem database
USE StudentManagementSystem;

-- Create Enrollment Table 
CREATE TABLE IF NOT EXISTS Enrollment (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

-- Insert Sample Data into Enrollment 
INSERT INTO Enrollment (StudentID, CourseID) VALUES (1, 101);
INSERT INTO Enrollment (StudentID, CourseID) VALUES (2, 102);
INSERT INTO Enrollment (StudentID, CourseID) VALUES (3, 103);

-- Retrieve Student Info with Enrollment Details
-- Retrieve StudentID, FirstName, LastName, EnrollmentID, CourseID
-- Using INNER JOIN between Student and Enrollment
SELECT 
    s.StudentID,
    s.FirstName,
    s.LastName,
    e.EnrollmentID,
    e.CourseID
FROM Student s
INNER JOIN Enrollment e ON s.StudentID = e.StudentID;
