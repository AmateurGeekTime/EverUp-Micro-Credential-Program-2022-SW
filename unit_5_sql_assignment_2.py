# -*- coding: utf-8 -*-
"""Unit 5 SQL Assignment 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Akv9GtiBaq7gFr1F6A4IVNi3NX4FlOb
"""

#Unit 5 SQL Assignment 2
#Name: Qianbing Chen
#Lesson 9: Insert and Update
#1. Create a table with the following parameters:  
#CustomerID
#CustomerName  
#Address
#City
#PostalCode
#Country  Email
CREATE TABLE information (
    CustomerID serial PRIMARY KEY,
    CustomerName VARCHAR(255) NOT NULL,
    Address VARCHAR(255),
    City VARCHAR(255),
    PostalCode VARCHAR(255),
    Country VARCHAR(255),
    Email VARCHAR(255));
#2. Insert 3 rows of data into these columns using INSERT. The data you insert should make sense for the column.
INSERT INTO information(customername, address, city, postalcode,country,email)
VALUES VALUES ('John', ‘’, ‘’, ‘’, ‘’, 'john123@gmail.com'),
('Jen','123 1st Avenue','New York','11223','US','jen123@email.com')
(‘Jake’, ‘’, ‘New York’, ‘12345’, ‘United States’, ‘jake@gmail.com’)
#3. Use an UPDATE to modify any portion of the data
UPDATE information
SET city = 'Brooklyn'
WHERE customername = ‘Jake’
#4. Finally, write a statement to delete one row of data.
DELETE FROM information
WHERE CustomerID = 3