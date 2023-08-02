import customtkinter as ctk
from dbConfig import db

class Invoice(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Select an option")

        View_Invoice = ctk.CTkButton(
            self,
            text = "View Invoice",
            command = lambda: controller.show_frame("ViewInvoice"),
        )

        Add_Invoice = ctk.CTkButton(
            self,
            text = "Add Invoice",
            command = lambda: controller.show_frame("AddInvoice"),
        )

        Update_Invoice = ctk.CTkButton(
            self,
            text = "Update Invoice",
            command = lambda: controller.show_frame("UpdateInvoice"),
        )

        back = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: controller.show_frame("StartPage"),
        )
    
        label.pack(side = "top", fill = "x", pady=10)
        View_Invoice.pack()
        Add_Invoice.pack()
        Update_Invoice.pack()
        back.pack()

class ViewInvoice(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text = "View Invoice", width = 200)
        self.results_box=ctk.CTkTextbox(self, width=400)
        Invoice_ID = ctk.CTkEntry(self, placeholder_text = "Invoice ID", width = 200)
        PID = ctk.CTkEntry(self, placeholder_text = "PID", width = 200)
        Provider = ctk.CTkEntry(self, placeholder_text = "Provider", width = 200)
        
        search = ctk.CTkButton(
            self,
            text = "View",
            command = lambda: self.search(Invoice_ID.get(), PID.get(), Provider.get())
        )
        
        back = ctk.CTkButton(
            self, text = "Back", command = lambda: self.goto_Invoice()
        )
        
        self.entries = [Invoice_ID, PID, Provider]

        elements = [
            label,
            Invoice_ID,
            PID,
            Provider,
            search,
            self.results_box,
            back,
        ]
        for element in elements:
            element.pack()

    def goto_Invoice(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)
        
        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.configure(state=ctk.DISABLED)
        self.controller.show_frame("Invoice")
        
    def search(self, Invoice_ID, PID, Provider):
        query = "select PID, Invoice_ID, Provider, Deductible, Co_pay from Invoice_Contains, Insurance where Invoice_ID = %s and PID = %s and Provider = %s"
        medicationQuerySql = "Select * From procedure_requires JOIN medication ON PID = %s;"

        equipmentQuerySql = "Select * From procedure_requires JOIN equipment ON PID = %s;"
        
        medication_text = ""
        equipment_text = ""
        mycursor = db.cursor()

        queryVal = (Invoice_ID, PID, Provider)
        queryVal1 = (PID, )
         # Fetch the results
        mycursor.execute(query, queryVal)
        result = mycursor.fetchall()
        mycursor.execute(medicationQuerySql, queryVal1)
        medication = mycursor.fetchall()
        mycursor.execute(equipmentQuerySql, queryVal1)
        equipment = mycursor.fetchall()

        if result:
            label_text = "PID: {}\nInvoice ID: {}\nProvider: {}\nDeductible: {}\nCo pay: {}\n\n".format(
                result[0][0], result[0][1], result[0][2], result[0][3], result[0][4]
            )
            medication_text += "MEDICTION:\n\nName: {}\t| Code: {}\t| Expiration: {}\t| Dose: {}\t| Form: {}\n\n".format(
                medication[0][0], medication[0][1], medication[0][2], medication[0][3], medication[0][4]
            )
            equipment_text += "EQUIPMENT:\n\nName: {}\t| Code: {}\t| Lifetime: {}\t| Hours: {}\t| Type: {}".format(
                equipment[0][0], equipment[0][1], equipment[0][2], equipment[0][3], equipment[0][4]
            )
            if medication_text == "MEDICTION:\n\n":
                label_text = label_text + equipment_text
            elif equipment_text == "EQUIPMENT:\n\n":
                label_text = label_text + medication_text
            else:
                label_text = label_text + medication_text + equipment_text
        else:
            label_text = "Invoice Does Not Exist."

        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.insert("0.0", label_text)
        self.results_box.configure(state=ctk.DISABLED)

class AddInvoice(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text = "Add Invoice", width = 200)
        self.results_box = ctk.CTkTextbox(self, width=400)
        PID = ctk.CTkEntry(self, placeholder_text = "PID", width = 200)
        Specialty = ctk.CTkEntry(self, placeholder_text = "Specialty", width = 200)
        Room_Type = ctk.CTkEntry(self, placeholder_text = "Room Type", width = 200)

        self.entries = [PID, Specialty, Room_Type]

        add = ctk.CTkButton(
            self,
            text="Add",
            command = lambda: self.add(PID.get(), Specialty.get(), Room_Type.get()),
        )
        back = ctk.CTkButton(
            self,
            text="Go back", 
            command = lambda: self.goto_Invoice(),
        )

        elements = [
            label,
            PID,
            Specialty,
            Room_Type,
            add,
            self.results_box,
            back,
        ]
        for element in elements:
            element.pack()

    def goto_Invoice(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)
        
        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.configure(state=ctk.DISABLED)
        self.controller.show_frame("Invoice")

    def add(self, PID, Specialty, Room_Type):
        query1 = " INSERT INTO invoice (Invoice_ID) VALUES (null)"
        query2 = "INSERT INTO Procedure_Info (PID, Specialty, Room_Type) VALUES (%s, %s, %s)"
        query3 = "Insert Into invoice_contains (PID, Invoice_ID) Values (%s, (SELECT Invoice_ID FROM invoice ORDER BY Invoice_ID DESC LIMIT 1));"
        queryVal2 = (PID, Specialty, Room_Type)
        queryVal3 = (PID,)
        mycursor = db.cursor()

        try:
            mycursor.execute(query1)
            mycursor.execute(query2, queryVal2)
            mycursor.execute(query3, queryVal3)
            db.commit()  # Commit the transaction to save the changes in the database
            self.results_box.configure(state=ctk.NORMAL)
            self.results_box.delete("0.0", "end")
            label_text = "Information added successfully!"
            self.results_box.insert("0.0", label_text)
            self.results_box.configure(state=ctk.DISABLED)
        except Exception as e:
            db.rollback()  # Rollback the transaction in case of an error
            self.results_box.configure(state=ctk.NORMAL)
            self.results_box.delete("0.0", "end")
            label_text = "Error occurred: {}".format(str(e))
            self.results_box.insert("0.0", label_text)
            self.results_box.configure(state=ctk.DISABLED)

class UpdateInvoice(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text = "Update Invoice", width = 200)
        self.results_box = ctk.CTkTextbox(self, width=400)
        Invoice_ID = ctk.CTkEntry(self, placeholder_text = "Invoice ID", width = 200)
        PID = ctk.CTkEntry(self, placeholder_text = "New PID", width = 200)

        update = ctk.CTkButton(
                self,
                text="Update",
                command = lambda: self.update(PID.get(), Invoice_ID.get()),
            )
        
        back = ctk.CTkButton(
            self,
            text="Go back", 
            command = lambda: self.goto_Invoice(),
        )
        
        self.entries = [PID, Invoice_ID]

        elements = [
            label,
            Invoice_ID,
            PID,
            update,
            self.results_box,
            back,
        ]
        for element in elements:
            element.pack()
    
    def goto_Invoice(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)
        
        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.configure(state=ctk.DISABLED)
        self.controller.show_frame("Invoice")
        
    def update(self, PID, Invoice_ID):
        query = "UPDATE invoice_contains SET PID = %s WHERE Invoice_ID = %s;"
        queryVal = (PID, Invoice_ID)
        mycursor = db.cursor()

        try:
            mycursor.execute(query, queryVal)
            db.commit()  # Commit the transaction to save the changes in the database
            self.results_box.configure(state=ctk.NORMAL)
            self.results_box.delete("0.0", "end")
            label_text = "Information added successfully!"
            self.results_box.insert("0.0", label_text)
            self.results_box.configure(state=ctk.DISABLED)
        except Exception as e:
            db.rollback()  # Rollback the transaction in case of an error
            self.results_box.configure(state=ctk.NORMAL)
            self.results_box.delete("0.0", "end")
            label_text = "Error occurred: {}".format(str(e))
            self.results_box.insert("0.0", label_text)
            self.results_box.configure(state=ctk.DISABLED)
