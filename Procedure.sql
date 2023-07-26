Create Table Procedure_Info (
	PID varchar(50) Not Null,
    Specialty varchar(50) Not Null,
    Room_Type varchar(50) Not Null,
    primary key (PID)
);

insert into procedure_info values ("123", "Cardiology", "Surgery Room");
insert into procedure_info values ("456", "Urology", "Patient Room");
