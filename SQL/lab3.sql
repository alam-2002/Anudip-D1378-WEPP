-- Lab-3                                                                                                                                                                Lab 1: Database Schema:
-- Consider a simple database with one tables: BankAccount
-- BankAccount Table:
-- ● Columns: account_id (Primary Key), account_holder_name,
-- account_balance
-- Task 1: Insert Data
-- Write an SQL INSERT statement to insert data into the BankAccount table.
-- Task 2: Retrieving Data
-- Write an SQL SELECT statement to retrieve the account_holder_name and
-- account_balance of all account holders from the BankAccount table.
-- Task 3: Filtering Data
-- Write an SQL SELECT statement to retrieve the account_holder_name and
-- account_balance where the account_balance is more than 30,000.
-- Task 4: Updating Data
-- Write an SQL UPDATE statement to change the account_balance of the account
-- holder whose ID is 101.

-- Table Creation
CREATE TABLE BankAccount (
    account_id INT PRIMARY KEY,
    account_holder_name VARCHAR(100) NOT NULL,
    account_balance DECIMAL(15,2) NOT NULL
);

-- Insert Data
INSERT INTO BankAccount (account_id, account_holder_name, account_balance)
VALUES (101, 'John Doe', 25000.00);

INSERT INTO BankAccount (account_id, account_holder_name, account_balance)
VALUES (102, 'Jane Smith', 45000.00);

INSERT INTO BankAccount (account_id, account_holder_name, account_balance)
VALUES (103, 'Michael Brown', 32000.00);

-- Retrieve all account holders and balances
SELECT account_holder_name, account_balance
FROM BankAccount;

-- Filter where balance > 30,000
SELECT account_holder_name, account_balance
FROM BankAccount
WHERE account_balance > 30000;

-- Update balance of account with ID = 101
UPDATE BankAccount
SET account_balance = 35000.00
WHERE account_id = 101;

-- Check the updated table
SELECT * FROM BankAccount;
