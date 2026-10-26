USE company;

INSERT INTO DEPARTMENT (Dnumber, Dname, mgr_ssn, mgr_start_date) VALUES 
(1, 'Research', NULL, '2022-01-01'),
(2, 'Administration', NULL, '2023-05-15'),
(3, 'Development', NULL, '2024-03-10');

INSERT INTO EMPLOYEE (ssn, fname, lname, bdate, address, gender, salary, Dno) VALUES 
(101, 'Ahmed', 'Ali', '1995-04-12', 'Alexandria', 'M', 8500.00, 1),
(102, 'Sara', 'Mahmoud', '1998-07-20', 'Cairo', 'F', 9200.00, 2),
(103, 'Omar', 'Khaled', '1990-11-05', 'Giza', 'M', 12000.00, 3);

UPDATE DEPARTMENT SET mgr_ssn = 103, mgr_start_date = '2024-03-10' WHERE Dnumber = 1;
UPDATE DEPARTMENT SET mgr_ssn = 102, mgr_start_date = '2023-05-15' WHERE Dnumber = 2;
UPDATE DEPARTMENT SET mgr_ssn = 101, mgr_start_date = '2022-01-01' WHERE Dnumber = 3;

INSERT INTO PROJECT (Pnumber, Pname, Plocation, Dno) VALUES 
(10, 'AI System', 'Alexandria', 1),
(20, 'HR Portal', 'Cairo', 2),
(30, 'Cloud Migration', 'Giza', 3);