CREATE TABLE employee (
  SSN INT(9) NOT NULL,
  Specialty VARCHAR(50) NOT NULL UNIQUE,
  Super_SSN INT(9) NOT NULL UNIQUE,
  PRIMARY KEY (SSN),
  FOREIGN KEY (SSN) REFERENCES person(SSN)
);

Create Table Specialty_Salary (
	Specialty VARCHAR(50) NOT NULL,
    Salary int(10) NOT NULL,
    PRIMARY KEY (Specialty),
    Foreign Key (Specialty) REFERENCES employee(Specialty)
);

Create Table Department_Supervisor (
	Super_SSN INT(9) NOT NULL,
    Department varchar(50) NOT NULL,
    PRIMARY KEY (Super_SSN),
    Foreign Key (Super_SSN) REFERENCES employee(Super_SSN)
);
