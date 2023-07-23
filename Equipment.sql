Create Table Equipment (
	  Eqmt_Name varchar(50) Not Null,
    Supply_code varchar(50) Not Null Unique,
    Lifetime varchar(50) Not Null,
    Hours varchar(50) Not Null,
    Eqmt_Type varchar(50) Not Null,
    primary key (Supply_code),
    foreign key (Supply_Code) references Supplies(Supply_Code)
);
