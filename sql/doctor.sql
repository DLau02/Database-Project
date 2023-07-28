CREATE TABLE doctor(
	SSN int(9) NOT NULL,
    PRIMARY KEY(SSN),
    FOREIGN KEY(SSN) REFERENCES employee(SSN)
);

INSERT INTO doctor VALUES (123456789);
INSERT INTO doctor VALUES (987654321);
INSERT INTO doctor VALUES (192837465);

/*drop table doctor