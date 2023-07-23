create table Invoice_Contains (
	  PID varchar(50) Not Null Unique,
    Invoice_ID varchar(50) Not Null,
    Primary Key (Invoice_ID),
    foreign key (PID) references Procedure_Info(PID),
    foreign key (Invoice_ID) references Invoice(Invoice_ID)
);
