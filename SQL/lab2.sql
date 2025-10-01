-- LAB -2                                                                                                                                                                   Task 1: Update the Student table with the following information:
-- Change the email to 'jane_Smith@example.com'
-- Where FirstName is 'Jane' and LastName is 'Smith';
-- Update the Instructor with the following information:
-- Change the email to 'rogerwhite@example.com'
-- Where FirstName of the instructor is 'Roger' and LastName is 'White';
-- Task 2:
-- Delete record from the Student table on following condition:
-- Delete student/students records from the Student table where last name is Smith

-- Update Student's email
UPDATE Student
SET Email = 'jane_Smith@example.com'
WHERE FirstName = 'Jane' AND LastName = 'Smith';

-- Update Instructor's email
UPDATE Instructor
SET Email = 'rogerwhite@example.com'
WHERE FirstName = 'Roger' AND LastName = 'White';

-- Delete students with LastName = 'Smith'
DELETE FROM Student
WHERE LastName = 'Smith';

SELECT * FROM Student;
SELECT * FROM Instructor;

