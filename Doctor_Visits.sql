create table Doctor_Visits (
	Invoice_ID int Not Null,
    Patient_SSN int(9) Not Null,
    Doc_SSN int(9) Not Null,
    Duration varchar(50) Not Null,
    Visit_Type varchar(50) Not Null,
    primary key (patient_ssn,doc_ssn),
    foreign key (Patient_SSN) references Patient(SSN),
    foreign key (Doc_SSN) references doctor(SSN)
);
insert into doctor_visits values (1, 374837293, 123456789, "1 hour", "Physical Evaluation");
