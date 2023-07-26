Create Table Supplies (
	Supp_Name varchar(50) Not Null,
    Supply_code varchar(50) Not Null Unique,
    Price decimal(13,2) Not Null,
    primary key (Supply_code)
);

insert into supplies values ("scalpel", "1", 7.00);
insert into supplies values ("masks", "2", 9.00);
insert into supplies values ("stethescope", "3", 100.00);
insert into supplies values ("ibuprofen 200mg", "4", 10.00); 