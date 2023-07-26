Create Table Patient(
	SSN int(9) Not Null,
    Room_Num Int(5) Not Null,
    primary key (SSN),
    foreign key (SSN) references person(SSN),
    foreign key (Room_Num) references room(Room_Num)
);

insert into patient values (374837293, 10000);