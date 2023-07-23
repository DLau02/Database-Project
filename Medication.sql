Create Table Medication (
	  Med_Name varchar(50) Not Null,
    Supply_code varchar(50) Not Null Unique,
    Expiration date Not Null,
    Dose varchar(50) Not Null,
    Form varchar(50) Not Null,
    primary key (Supply_code),
    foreign key (Supply_Code) references Supplies(Supply_Code)
);
