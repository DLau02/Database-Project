CREATE TABLE person(
	SSN char(9) NOT NULL,
    Address varchar(256) NOT NULL,
    Last_name varchar(256) NOT NULL,
    First_name varchar(256) NOT NULL,
    Birthdate date NOT NULL,
    PRIMARY KEY(SSN)
);

INSERT INTO person VALUES ('123456789', '1234 Place Lane, Schenectady, NY, 12345', 'Son', 'Per', STR_TO_DATE('07-25-2012','%m-%d-%Y'));
INSERT INTO person VALUES ('987654321', '566 Street Drive, Schenectady, NY, 12345, 20748', 'Smith', 'John', STR_TO_DATE('06-30-200','%m-%d-%Y'));
INSERT INTO person VALUES ('192837465', '134 Place Lane, Schenectady, NY, 12345, 32714', 'Doe', 'Jane', STR_TO_DATE('11-02-1994','%m-%d-%Y'));
INSERT INTO person VALUES ("918273645", "223 Location Street, Schenectady, NY, 12345", "Bill", "Thomas", STR_TO_DATE('11-02-1994','%m-%d-%Y'));