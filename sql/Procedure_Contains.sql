create table Procedure_Contains (
	PID varchar(50) Not Null,
    Invoice_ID int Not Null,
    Primary Key (Invoice_ID, PID),
    foreign key (PID) references Procedure_Info(PID),
    foreign key (Invoice_ID) references Invoice(Invoice_ID)
);

insert into procedure_contains values ("123", 1);