USE cupcakes;


CREATE TABLE users(id INT NOT NULL AUTO_INCREMENT, username VARCHAR(255), password VARCHAR(255), PRIMARY KEY (id));

CREATE TABLE menu(flavor varchar(255) primary key NOT NULL, price int);

CREATE TABLE orders(orderID int NOT NULL AUTO_INCREMENT, orderPrice int, item varchar(255), userId int, PRIMARY KEY(orderId), 
FOREIGN KEY(userId) REFERENCES users(id), foreign key(item) references menu(flavor));

DROP TABLE orders;
DROP TABLE users;
DROP TABLE menu;

SELECT * FROM users;

insert into users (username, password) values ("Dane", "password1"), ("John", "password2"), ("Kerry", "password3");


INSERT INTO menu (flavor, price) VALUES ("Chocolate", 5), ("Vanilla", 4), ("Cookies & Cream", 7);


SELECT * FROM menu;