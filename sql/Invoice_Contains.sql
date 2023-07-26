create table Invoice_Contains (
	PID varchar(50) Not Null ,
    Invoice_ID int Not Null,
    Primary Key (Invoice_ID, pid),
    foreign key (PID) references Procedure_Info(PID),
    foreign key (Invoice_ID) references Invoice(Invoice_ID)
);

insert into invoice_contains values ("123", 1);
insert into invoice_contains values ("456", 2);
