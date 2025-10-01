-- Lab1 Mysql                                                                                                                                                         Lab 1. Create a Database & Table Using MySQL Command-Line Client.
-- ● Create a database with the name StudentManagementSystem.
-- Create a table with named Student with attributes:
-- ● StudentID (Primary Key)
-- ● FirstName
-- ● LastName
-- ● DateOfBirth
-- ● Gender
-- ● Email
-- ● Phone
-- Create a table with name Course with attributes:
-- ● CourseID (Primary Key)
-- ● CourseTitle
-- ● Credits
-- Create a table with named Instructor with attributes:
-- ● InstructorID (Primary Key)
-- ● FirstName
-- ● LastName
-- ● Email

-- 1. Create Database
CREATE DATABASE StudentManagementSystem;

-- 2. Use the Database
USE StudentManagementSystem;

-- 3. Create Student Table
CREATE TABLE Student (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE,
    Gender ENUM('Male', 'Female', 'Other'),
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15)
);

-- 4. Create Course Table
CREATE TABLE Course (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseTitle VARCHAR(100) NOT NULL,
    Credits INT NOT NULL
);

-- 5. Create Instructor Table
CREATE TABLE Instructor (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE
);
