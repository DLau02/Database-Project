Create Table room (
	Room_Num Int(5) Not Null,
    Room_type varchar(30) Not Null,
    Primary Key (Room_Num)
);

Create Table Room_Capacity (
	Room_Type varchar(30) Not Null,
    Room_Cap int(4) Not Null,
    Primary Key (Room_Type)
);

insert into room_capacity values ("Surgery Room", 1);
insert into room_capacity values ("Patient Room", 1);
insert into room_capacity values ("Storage Room", 60);
insert into room values (10000, "Patient Room");
insert into room values (10001, "Patient Room");
insert into room values (10002, "Surgery Room");
insert into room values (10003, "Storage Room");