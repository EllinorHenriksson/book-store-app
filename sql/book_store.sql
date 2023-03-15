CREATE SCHEMA book_store;

USE book_store;

CREATE TABLE books (
isbn char(10) not null,
author varchar(100) not null,
title varchar(128) not null,
price float not null,
`subject` varchar(30) not null,
PRIMARY KEY(isbn)
);

CREATE TABLE members (
userid int not null auto_increment,
fname varchar(20) not null,
lname varchar(20) not null,
address varchar(50) not null,
city varchar(30) not null,
state varchar(20) not null,
zip int not null,
phone varchar(12) null,
email varchar(40) not null unique,
`password` varchar(65) not null,
creditcardtype varchar(10) null,
creditcardnumber char(16) null,
PRIMARY KEY(userid)
);

CREATE TABLE orders (
ono int not null auto_increment,
userid int not null,
received date not null,
shipped date null,
shipAddress varchar(50) null,
shipCity varchar(30) null,
shipState varchar(20) null,
shipZip int null,
PRIMARY KEY(ono),
FOREIGN KEY(userid) REFERENCES members(userid) on update cascade on delete cascade
);

CREATE TABLE odetails (
ono int not null,
isbn char(10) not null,
qty int not null,
price float not null,
primary key(ono, isbn),
foreign key (ono) references orders (ono) on update cascade on delete cascade,
foreign key (isbn) references books (isbn) on update cascade on delete cascade
);

CREATE TABLE cart (
userid int not null,
isbn char(10) not null,
qty int not null,
primary key(userid, isbn),
foreign key (userid) references members (userid) on update cascade on delete cascade,
foreign key (isbn) references books (isbn) on update cascade on delete cascade
);


