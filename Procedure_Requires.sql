create table Procedure_Requires (
	PID varchar(50) Not Null Unique,
    supply_code varchar(50) not null, 
    Time_Held varchar(50) Not Null,
    Quantitiy int(5) Not Null,
    Primary Key (pid,supply_code),
    foreign key (PID) references Procedure_Info(PID),
    foreign key (supply_code) references Supplies(supply_code)
);

insert into Procedure_requires values("123", 3, "1 hour", 1);
