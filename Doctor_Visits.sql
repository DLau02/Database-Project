create table Doctor_Visits (
	  Invoice_ID varchar(50) Not Null,
    Patient_SSN int(9) Not Null,
    Doc_SSN int(9) Not Null,
    Duration varchar(50) Not Null,
    Visit_Type varchar(50) Not Null,
    primary key (Invoice_ID),
    foreign key (Patient_SSN) references Patient(SSN),
    foreign key (Doc_SSN) references doctor(SSN)
);
