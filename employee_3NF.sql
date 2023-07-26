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
