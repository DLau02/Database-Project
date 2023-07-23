Create Table Director (
    SSN int(9) Not Null primary key,
    foreign key (SSN) references person(SSN)
);
