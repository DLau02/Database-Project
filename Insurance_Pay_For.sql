CREATE TABLE Insurance_Pay_For (
    invoice_ID VARCHAR(8),
    Provider VARCHAR(20),
    FOREIGN KEY (invoice_ID) REFERENCES Invoice(invoice_ID),
    FOREIGN KEY (Provider) REFERENCES Insurance(Provider)
);
