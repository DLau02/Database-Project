CREATE TABLE Insurance (
    Provider VARCHAR(20) PRIMARY KEY,
    Deductible DECIMAL(13, 2),
    Co_pay DECIMAL(13, 2)
);

insert into insurance values ("Aetna", 2000.00, 50.00);
insert into insurance values ("UnitedHealthcare", 1500.00, 30);
insert into insurance values ("Trinton Benefits", 1500.00, 40);
