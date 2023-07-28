import customtkinter as ctk
from dbConfig import db

class SupplyOpts(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Select an option")
        add_medication = ctk.CTkButton(
            self, 
            text="Add medication",
            command=lambda: controller.show_frame("AddMedication")
        )
        add_equipment = ctk.CTkButton(
            self,  
            text="Add equipment",
            command=lambda: controller.show_frame("Add equipment"),
        )
        back = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: controller.show_frame("StartPage"),
        )

        label.pack(side="top", fill="x", pady=10)
        add_medication.pack()
        add_equipment.pack()
        back.pack()

class AddMedication(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Enter medication information", width=200)
        name = ctk.CTkEntry(self, placeholder_text="name", width=200)
        code = ctk.CTkEntry(self, placeholder_text="code", width=200)
        expiration = ctk.CTkEntry(
            self, placeholder_text="Expiration: MM-DD-YYYY", width=200
        )
        dose = ctk.CTkEntry(self, placeholder_text="dose", width=200)
        form = ctk.CTkEntry(self, placeholder_text="form", width=200)
        price = ctk.CTkEntry(self, placeholder_text="price", width=200)
        submit = ctk.CTkButton(
            self, text="Submit", command=lambda: self.add(name.get(), code.get(), expiration.get(), dose.get(), form.get(), float(price.get())),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_patient_opts()
        )

        elements = [
            label,
            name,
            code,
            expiration,
            dose,
            form,
            price,
            submit,
            back,
        ]

        for element in elements:
            element.pack()

    def add(self, name: str, code: str, expiration: str, dose: str, form: str, price: float):
        mycursor = db.cursor()
        
        supplySql = "INSERT INTO supplies VALUES (%s, %s, %s)"
        supplyVal = (name, code, price)
        try:
            mycursor.execute(supplySql, supplyVal)
        except Exception as e:
            print(e)
        
        medicationSql = "INSERT INTO medication VALUES (%s, %s, STR_TO_DATE('01-22-1905','%m-%d-%Y'), %s, %s)"
        medicationVal = (name, code, dose, form)
        try:
            mycursor.execute(medicationSql, medicationVal)
        except Exception as e:
            print(e)

        db.commit()

