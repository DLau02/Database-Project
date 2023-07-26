create table Room_Stores (
	Room_Num Int(5) Not Null,
    Supply_Code varchar(50) Not Null Unique,
    Time_Held varchar(50) Not Null,
    Quantitiy int(5) Not Null,
    primary key (Room_Num,supply_code),
    foreign key (Room_Num) references room(Room_Num),
    foreign key (Supply_Code) references Supplies(Supply_Code)
);

insert into room_stores values (10003, "4", "5 months", 1000);
insert into room_stores values (10003, "3", "2 years", 50);
insert into room_stores values (10003, "2", "5 months", 1000);
insert into room_stores values (10003, "1", "2 months", 1000);

