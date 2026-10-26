USE library_db;


INSERT INTO AUTHOR (author_id, name, country) VALUES 
(1, 'Agatha Christie', 'UK'),
(2, 'Ahmed Khaled Tawfik', 'Egypt'),
(3, 'Dan Brown', 'USA');

INSERT INTO BOOK (book_id, title, price, author_id) VALUES 
(101, 'And Then There Were None', 15.50, 1),
(102, 'Murder on the Orient Express', 18.00, 1),
(201, 'Utopia', 12.00, 2),
(202, 'Phantasia', 10.50, 2),
(301, 'The Da Vinci Code', 22.00, 3),
(302, 'Angels & Demons', 20.00, 3);