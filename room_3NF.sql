Create Table room (
	Room_Num Int(5) Not Null,
    Room_type varchar(30) Not Null Unique,
    Primary Key (Room_Num)
);

Create Table Room_Capacity (
	Room_Type varchar(30) Not Null,
    Room_Cap int(4) Not Null,
    Primary Key (Room_Type),
    foreign key (Room_Type) references room(room_type)
);
