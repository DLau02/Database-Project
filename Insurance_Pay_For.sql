CREATE TABLE Insurance_Pay_For (
    invoice_ID VARCHAR(50),
    Provider VARCHAR(20),
    primary key (invoice_id, provider),
    FOREIGN KEY (invoice_ID) REFERENCES Invoice(invoice_ID),
    FOREIGN KEY (Provider) REFERENCES Insurance(Provider)
);
