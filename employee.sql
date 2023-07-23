CREATE TABLE employee(
	SSN char(9) NOT NULL,
    Department varchar(256) NOT NULL,
    Salary decimal(13, 2) NOT NULL,
    super_SSN char(9),
    Specialty varchar(256),
	PRIMARY KEY(SSN),
    FOREIGN KEY(super_SSN) REFERENCES person(SSN)
);

INSERT INTO employee VALUES ("123456789", "Cardiology", 453779.00, NULL, "Cardiology");
INSERT INTO employee VALUES ("987654321", "Cardiology", 306379.00, "123456789", "Cardiology");
INSERT INTO employee VALUES ("192837465", "Neurology", 276346.00, NULL, "Neurology");
INSERT INTO employee VALUES ("918273645", "Clerical", 43693.00, NULL, NULL);