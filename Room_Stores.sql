create table Room_Stores (
	  Room_Num Int(5) Not Null,
    Supply_Code varchar(50) Not Null Unique,
    Time_Held varchar(50) Not Null,
    Quantitiy int(5) Not Null,
    primary key (Room_Num),
    foreign key (Room_Num) references room(Room_Num),
    foreign key (Supply_Code) references Supplies(Supply_Code)
);
