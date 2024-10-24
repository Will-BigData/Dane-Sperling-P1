USE cupcakes;

CREATE TABLE users(id INT NOT NULL AUTO_INCREMENT, username VARCHAR(255), password VARCHAR(255), admin bool, PRIMARY KEY (id));

CREATE TABLE menu(flavor varchar(255) primary key NOT NULL, price int);

CREATE TABLE orders(orderID int NOT NULL AUTO_INCREMENT, orderPrice int, item varchar(255), userId int, PRIMARY KEY(orderId), 
FOREIGN KEY(userId) REFERENCES users(id), foreign key(item) references menu(flavor));

DROP TABLE orders;
DROP TABLE users;
DROP TABLE menu;

SELECT * FROM users;

DELETE FROM users where id = 4;

insert into users (username, password, admin) values ("Dane", "password1", true), ("John", "password2", false), ("Kerry", "password3", false);
INSERT INTO menu (flavor, price) VALUES ("Chocolate", 5), ("Vanilla", 4), ("Cookies & Cream", 7);
Insert into orders (orderPrice, item, userId) VALUES (5, "Chocolate", 1), (4, "Vanilla", 1), (7, "Cookies & Cream", 1);
insert into orders (orderPrice, item, userId) Values (5, "Chocolate", 2);

SELECT * FROM menu;

SELECT * FROM orders;


UPDATE menu set price = 5 where flavor = "Chocolate";
update menu set flavor = "Vanilla" where flavor = "Strawberry";

SELECT * from users where username = "dane";






