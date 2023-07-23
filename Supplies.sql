Create Table Supplies (
	Supp_Name varchar(50) Not Null,
    Supply_code varchar(50) Not Null Unique,
    Price int(10) Not Null,
    primary key (Supply_code)
);
