
CREATE TABLE person(
	SSN int(9) NOT NULL,
    Address varchar(256) NOT NULL,
    Last_name varchar(256) NOT NULL,
    First_name varchar(256) NOT NULL,
    Birthdate date NOT NULL,
    PRIMARY KEY(SSN)
);

INSERT INTO person VALUES (123456789, '1234 Place Lane, Schenectady, NY, 12345', 'Son', 'Per', STR_TO_DATE('07-25-2012','%m-%d-%Y'));
INSERT INTO person VALUES (987654321, '566 Street Drive, Schenectady, NY, 12345, 20748', 'Smith', 'John', STR_TO_DATE('06-30-200','%m-%d-%Y'));
INSERT INTO person VALUES (192837465, '134 Place Lane, Schenectady, NY, 12345, 32714', 'Doe', 'Jane', STR_TO_DATE('11-02-1994','%m-%d-%Y'));
INSERT INTO person VALUES (918273645, "223 Location Street, Schenectady, NY, 12345", "Bill", "Thomas", STR_TO_DATE('11-02-1994','%m-%d-%Y'));
insert into person values (348293849, "223 Location Street, Schenectady, NY, 12345", "San", "Sue", STR_TO_DATE('11-22-1994','%m-%d-%Y'));
insert into person values (374837293, "3822 Location Way, Schenectady, NY, 12345", "Tient", "Pai", STR_TO_DATE('01-22-1905','%m-%d-%Y'));

CREATE TABLE employee (
  SSN INT(9) NOT NULL unique,
  Specialty VARCHAR(50) NOT NULL,
  Department varchar(50) not null,
  PRIMARY KEY (SSN),
  FOREIGN KEY (SSN) REFERENCES person(SSN)
);

Create Table Specialty_Salary (
	Specialty VARCHAR(50) NOT NULL,
    Salary decimal(13, 2) NOT NULL,
    PRIMARY KEY (Specialty)
);

Create Table Department_Supervisor (
	Super_SSN int(9) NOT NULL,
    Department varchar(50) NOT NULL,
    PRIMARY KEY (Department)
);

insert into specialty_salary values ("Cardiology", 458626.00);
insert into specialty_salary values ("Radiology", 63401.00);
insert into specialty_salary values ("Urology", 410680.00);
insert into specialty_salary values ("General Surgery", 424100.00);
insert into department_supervisor values (1234556789, "Cardiology");
insert into department_supervisor values (987654321, "Radiology");
insert into department_supervisor values (192837465, "Urology");
insert into department_supervisor values (918273645, "General Surgery");
insert into employee values (123456789, "Cardiology", "Cardiology");
insert into employee values (987654321, "Radiology", "Radiology");
insert into employee values (192837465, "Urology", "Urology");
insert into employee values (918273645, "General Surgery", "General Surgery");
insert into employee values (348293849, "General Surgery", "General Surgery");


CREATE TABLE doctor(
	SSN int(9) NOT NULL,
    PRIMARY KEY(SSN),
    FOREIGN KEY(SSN) REFERENCES employee(SSN)
);

INSERT INTO doctor VALUES (123456789);
INSERT INTO doctor VALUES (987654321);
INSERT INTO doctor VALUES (192837465);


CREATE TABLE Invoice (
    invoice_ID int AUTO_INCREMENT PRIMARY KEY
);

insert into invoice values(0);
insert into invoice values(null);
insert into invoice values(null);


Create Table room (
	Room_Num Int(5) Not Null,
    Room_type varchar(30) Not Null,
    Primary Key (Room_Num)
);

Create Table Room_Capacity (
	Room_Type varchar(30) Not Null,
    Room_Cap int(4) Not Null,
    Primary Key (Room_Type)
);

insert into room_capacity values ("Surgery Room", 1);
insert into room_capacity values ("Patient Room", 1);
insert into room_capacity values ("Storage Room", 60);
insert into room values (10000, "Patient Room");
insert into room values (10001, "Patient Room");
insert into room values (10002, "Surgery Room");
insert into room values (10003, "Storage Room");

Create Table Procedure_Info (
	PID varchar(50) Not Null,
    Specialty varchar(50) Not Null,
    Room_Type varchar(50) Not Null,
    primary key (PID)
);

insert into procedure_info values ("123", "Cardiology", "Surgery Room");
insert into procedure_info values ("456", "Urology", "Patient Room");

create table Invoice_Contains (
	PID varchar(50) Not Null ,
    Invoice_ID int Not Null,
    Primary Key (Invoice_ID, pid),
    foreign key (PID) references Procedure_Info(PID),
    foreign key (Invoice_ID) references Invoice(Invoice_ID)
);

insert into invoice_contains values ("123", 1);
insert into invoice_contains values ("456", 2);

Create Table Patient(
	SSN int(9) Not Null,
    Room_Num Int(5) Not Null,
    primary key (SSN),
    foreign key (SSN) references person(SSN),
    foreign key (Room_Num) references room(Room_Num)
);

insert into patient values (374837293, 10000);
create table Doctor_Visits (
	Invoice_ID int Not Null,
    Patient_SSN int(9) Not Null,
    Doc_SSN int(9) Not Null,
    Duration varchar(50) Not Null,
    Visit_Type varchar(50) Not Null,
    primary key (Invoice_ID),
    foreign key (Patient_SSN) references Patient(SSN),
    foreign key (Doc_SSN) references doctor(SSN)
);

insert into doctor_visits values (1, 374837293, 123456789, "1 hour", "Physical Evaluation");
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
Create Table Equipment (
	Eqmt_Name varchar(50) Not Null,
    Supply_code varchar(50) Not Null Unique,
    Lifetime varchar(50) Not Null,
    Hours varchar(50) Not Null,
    Eqmt_Type varchar(50) Not Null,
    primary key (Supply_code),
    foreign key (Supply_Code) references Supplies(Supply_Code)
);

insert into equipment values ("scalpel", "1", "1 use", "5", "surgical");
insert into equipment values ("masks", "2", "1 use", "5", "general use");
insert into equipment values ("stethescope", "3", "2 years", "1", "acoustic medical device");
CREATE TABLE Insurance (
    Provider VARCHAR(20) PRIMARY KEY,
    Deductible DECIMAL(13, 2),
    Co_pay DECIMAL(13, 2)
);

insert into insurance values ("Aetna", 2000.00, 50.00);
insert into insurance values ("UnitedHealthcare", 1500.00, 30);
insert into insurance values ("Trinton Benefits", 1500.00, 40);

create table Procedure_Contains (
	PID varchar(50) Not Null,
    Invoice_ID int Not Null,
    Primary Key (Invoice_ID, PID),
    foreign key (PID) references Procedure_Info(PID),
    foreign key (Invoice_ID) references Invoice(Invoice_ID)
);

insert into procedure_contains values ("123", 1);

create table Procedure_Requires (
	PID varchar(50) Not Null Unique,
    supply_code varchar(50) not null, 
    Time_Held varchar(50) Not Null,
    Quantitiy int(5) Not Null,
    Primary Key (pid,supply_code),
    foreign key (PID) references Procedure_Info(PID),
    foreign key (supply_code) references Supplies(supply_code)
);

insert into Procedure_requires values("123", 3, "1 hour", 1);

create table Room_Stores (
	Room_Num Int(5) Not Null,
    Supply_Code varchar(50) Not Null Unique,
    Time_Held varchar(50) Not Null,
    Quantitiy int(5) Not Null,
    primary key (Room_Num,supply_code),
    foreign key (Room_Num) references room(Room_Num),
    foreign key (Supply_Code) references Supplies(Supply_Code)
);

insert into room_stores values (10003, "4", "5 months", 1000);
insert into room_stores values (10003, "3", "2 years", 50);
insert into room_stores values (10003, "2", "5 months", 1000);
insert into room_stores values (10003, "1", "2 months", 1000);


CREATE TABLE Insurance_Pay_For (
    invoice_ID int,
    Provider VARCHAR(20),
    primary key (invoice_id, provider),
    FOREIGN KEY (invoice_ID) REFERENCES Invoice(invoice_ID),
    FOREIGN KEY (Provider) REFERENCES Insurance(Provider)
);

Create Table Medication (
	Med_Name varchar(50) Not Null,
    Supply_code varchar(50) Not Null Unique,
    Expiration date Not Null,
    Dose varchar(50) Not Null,
    Form varchar(50) Not Null,
    primary key (Supply_code),
    foreign key (Supply_Code) references Supplies(Supply_Code)
);

insert into medication values ("ibuprofen", "4",  STR_TO_DATE('11-22-2024','%m-%d-%Y'), "200 mg", "pill");
