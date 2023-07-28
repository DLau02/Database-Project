import customtkinter as ctk
from dbConfig import db, cursor

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
            command=lambda: controller.show_frame("AddEquipment"),
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
        label.pack()
        name = ctk.CTkEntry(self, placeholder_text="name", width=200)
        code = ctk.CTkEntry(self, placeholder_text="code", width=200)
        expiration = ctk.CTkEntry(
            self, placeholder_text="Expiration: MM-DD-YYYY", width=200
        )
        dose = ctk.CTkEntry(self, placeholder_text="dose", width=200)
        form = ctk.CTkEntry(self, placeholder_text="form", width=200)
        price = ctk.CTkEntry(self, placeholder_text="price", width=200)
        submit = ctk.CTkButton(
            self, text="Submit", command=lambda: addMedicationToDatabase(name.get(), code.get(), expiration.get(), dose.get(), form.get(), float(price.get())),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_supply_opts()
        )        

        self.entries = [name, code, expiration, dose, form, price]
        self.elements = [label] + self.entries + [submit, back]

        for element in self.elements:
            element.pack()

    def goto_supply_opts(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)

        self.controller.show_frame("SupplyOpts")

class AddEquipment(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Enter equipment information", width=200)  
        label.pack()   
        name = ctk.CTkEntry(self, placeholder_text="name", width=200)
        code = ctk.CTkEntry(self, placeholder_text="code", width=200)  
        lifetime = ctk.CTkEntry(self, placeholder_text="lifetime", width=200)
        hours = ctk.CTkEntry(self, placeholder_text="hours", width=200)
        type = ctk.CTkEntry(self, placeholder_text="type", width=200)
        price = ctk.CTkEntry(self, placeholder_text="price", width=200)
        submit = ctk.CTkButton(
            self, text="Submit", command=lambda: addMedicationToDatabase(name.get(), code.get(), lifetime.get(), hours.get(), type.get(), float(price.get())),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_supply_opts()
        )

        self.entries = [name, code, lifetime, hours, type, price]
        self.elements = [label] + self.entries + [submit, back]

        for element in self.elements:
            element.pack()

    def goto_supply_opts(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)

        self.controller.show_frame("SupplyOpts")

def addSupplyToDatabase(name: str, code: str, price: float):
    
    supplySql = "INSERT INTO supplies VALUES (%s, %s, %s)"
    supplyVal = (name, code, price)
    try:
        cursor.execute(supplySql, supplyVal)
        db.commit()
    except Exception as e:
        print(e)

def addMedicationToDatabase(name: str, code: str, expiration: str, dose: str, form: str, price: float):

    addSupplyToDatabase(name, code, price)

    medicationSql = "INSERT INTO medication VALUES (%s, %s, STR_TO_DATE('01-22-1905','%m-%d-%Y'), %s, %s)"
    medicationVal = (name, code, dose, form)
    try:
        cursor.execute(medicationSql, medicationVal)
        db.commit()
    except Exception as e:
        print(e)

def addEquipmentToDatabase(name: str, code: str, lifetime: str, hours: str, type: str, price: float):
    
    addSupplyToDatabase(name, code, price)

    equipmentSql = "INSERT INTO equipment VALUES (%s, %s, %s, %s, %s)"
    equipmentVal = (name, code, lifetime, hours, type)
    try:
        cursor.execute(equipmentSql, equipmentVal)
        db.commit()
    except Exception as e:
        print(e)
