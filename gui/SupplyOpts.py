import customtkinter as ctk
from dbConfig import db, cursor

class SupplyOpts(ctk.CTkFrame):
    def __init__(self, parent, controller):

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # elements to be rendered
        label = ctk.CTkLabel(self, text="Select an option")
        add_medication = ctk.CTkButton(
            self, 
            text="Add medication",
            command=lambda: controller.show_frame("AddMedication")
        )
        search_medication = ctk.CTkButton(
            self,
            text="Search medication",
            command=lambda: controller.show_frame("SearchMedication")
        )
        add_equipment = ctk.CTkButton(
            self,  
            text="Add equipment",
            command=lambda: controller.show_frame("AddEquipment"),
        )
        search_equipment = ctk.CTkButton(
            self,
            text="Search equipment",
            command=lambda: controller.show_frame("SearchEquipment")
        )
        equipment_for_procedure = ctk.CTkButton(
            self,
            text="supplies for  procedure",
            command=lambda: controller.show_frame("SuppliesforProcedure")
        )
        back = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: controller.show_frame("StartPage"),
        )

        # render all elements 
        label.pack(side="top", fill="x", pady=10)
        add_medication.pack()
        search_medication.pack()
        add_equipment.pack()
        search_equipment.pack()
        equipment_for_procedure.pack()
        back.pack()

class AddMedication(ctk.CTkFrame):
    def __init__(self, parent, controller):

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # elements to be rendered
        label = ctk.CTkLabel(self, text="Enter medication information", width=200)
        name = ctk.CTkEntry(self, placeholder_text="name", width=200)
        code = ctk.CTkEntry(self, placeholder_text="code", width=200)
        expiration = ctk.CTkEntry(
            self, placeholder_text="Expiration: MM-DD-YYYY", width=200
        )
        dose = ctk.CTkEntry(self, placeholder_text="dose", width=200)
        form = ctk.CTkEntry(self, placeholder_text="form", width=200)
        price = ctk.CTkEntry(self, placeholder_text="price (price cannot be updated)", width=200)
        submit = ctk.CTkButton(
            self, text="Submit", command=lambda: addMedicationToDatabase(name.get(), code.get(), expiration.get(), dose.get(), form.get(), float(price.get())),
        )
        update = ctk.CTkButton(
            self, text="Update", command=lambda: updateMedicationInDatabase(name.get(), code.get(), expiration.get(), dose.get(), form.get()),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_supply_opts()
        )        

        # order the elements
        self.entries = [name, code, expiration, dose, form, price]
        self.elements = [label] + self.entries + [submit, update, back]

        # render all elements 
        for element in self.elements:
            element.pack()

    def goto_supply_opts(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)

        self.controller.show_frame("SupplyOpts")

class SearchMedication(ctk.CTkFrame):
    def __init__(self, parent, controller):

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # elements to be rendered
        label = ctk.CTkLabel(self, text="Enter medication information", width=200)
        self.results_box=ctk.CTkTextbox(self, width=500)
        name = ctk.CTkEntry(self, placeholder_text="name", width=200)
        code = ctk.CTkEntry(self, placeholder_text="code", width=200)
        submit = ctk.CTkButton(
            self, text="Search", command=lambda: self.searchDatabaseForMedication(name.get(), code.get()),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_supply_opts()
        )  

        self.entries = [name, code]
        self.elements = [label, self.results_box] + self.entries + [submit, back]

        # render all elements 
        for element in self.elements:
            element.pack()

    def searchDatabaseForMedication(self, name: str, code: str):
    
        querySql = "Select * From Medication Where Med_Name = %s OR Supply_Code = %s;"
        queryVal = (name, code)
        
        try:
            cursor.execute(querySql, queryVal)
            medications = cursor.fetchall()
            label_text = "There are {} medications matching name: {}, code: {}\n".format(len(medications), name, code)
            for medication in medications:
                label_text += "Name: {} \nCode: {}\nExpiration: {}\nDose: {}\nForm: {}\n\n".format(medication[0], medication[1], medication[2], medication[3], medication[4])
            self.results_box.configure(state=ctk.NORMAL)
            self.results_box.delete("0.0", "end")
            self.results_box.insert("0.0", label_text)
            self.results_box.configure(state=ctk.DISABLED)    
        except Exception as e:
            print(e)

    def goto_supply_opts(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)

        self.controller.show_frame("SupplyOpts")

    def __init__(self, parent, controller):

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # elements to be rendered
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
            self, text="Submit", command=lambda: addMedicationToDatabase(name.get(), code.get(), expiration.get(), dose.get(), form.get(), float(price.get())),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_supply_opts()
        )        

        # order the elements
        self.entries = [name, code, expiration, dose, form, price]
        self.elements = [label] + self.entries + [submit, back]

        # render all elements 
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

        # elements to be rendered
        label = ctk.CTkLabel(self, text="Enter equipment information", width=200)  
        name = ctk.CTkEntry(self, placeholder_text="name", width=200)
        code = ctk.CTkEntry(self, placeholder_text="code", width=200)  
        lifetime = ctk.CTkEntry(self, placeholder_text="lifetime", width=200)
        hours = ctk.CTkEntry(self, placeholder_text="hours", width=200)
        type = ctk.CTkEntry(self, placeholder_text="type", width=200)
        price = ctk.CTkEntry(self, placeholder_text="price", width=200)
        submit = ctk.CTkButton(
            self, text="Submit", command=lambda: addEquipmentToDatabase(name.get(), code.get(), lifetime.get(), hours.get(), type.get(), float(price.get())),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_supply_opts()
        )

        # order the elements
        self.entries = [name, code, lifetime, hours, type, price]
        self.elements = [label] + self.entries + [submit, back]
        
        # render all elements 
        for element in self.elements:
            element.pack()

    def goto_supply_opts(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)

        self.controller.show_frame("SupplyOpts")

class SearchEquipment(ctk.CTkFrame):
    def __init__(self, parent, controller):

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # elements to be rendered
        label = ctk.CTkLabel(self, text="Enter medication information", width=200)
        name = ctk.CTkEntry(self, placeholder_text="name", width=200)
        code = ctk.CTkEntry(self, placeholder_text="code", width=200)
        self.results_box=ctk.CTkTextbox(self, width=500)
        
        submit = ctk.CTkButton(
            self, text="Search", command=lambda: self.searchDatabaseForEquipment(name.get(), code.get()),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_supply_opts()
        )

        self.entries = [name, code]
        self.elements = [label, self.results_box] + self.entries + [submit, back]

        # render all elements 
        for element in self.elements:
            element.pack()

    def goto_supply_opts(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)

        self.controller.show_frame("SupplyOpts")

    def searchDatabaseForEquipment(self, name: str, code: str):
    
        querySql = "Select * From Equipment Where Eqmt_Name = %s OR Supply_Code = %s;" 
        queryVal = (name, code)

        try:
            cursor.execute(querySql, queryVal)
            equipment = cursor.fetchall()
            label_text = "There are {} equipment pieces matching name: {}, code: {}\n".format(len(medications), name, code)
            for piece in equipment:
                label_text += "Name: {}\nCode: {}\nLifetime: {}\nHours: {}\nType: {}".format(equipment[0], equipment[1], equipment[2], equipment[3], equipment[4])
            self.results_box.configure(state=ctk.NORMAL)
            self.results_box.delete("0.0", "end")
            self.results_box.insert("0.0", label_text)
            self.results_box.configure(state=ctk.DISABLED)    
        except Exception as e:
            print(e)

    def goto_supply_opts(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)

        self.controller.show_frame("SupplyOpts")

class SuppliesforProcedure(ctk.CTkFrame):
    def __init__(self, parent, controller):

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # elements to be rendered
        label = ctk.CTkLabel(self, text="Enter procedure ID", width=200)
        med = ctk.CTkLabel(self, text="Medications required", width=200)
        equip = ctk.CTkLabel(self, text="prescriptions required", width=200)
        self.medication_results_box=ctk.CTkTextbox(self, width=500)
        self.equipment_results_box=ctk.CTkTextbox(self, width=500)
        code = ctk.CTkEntry(self, placeholder_text="procedure ID", width=200)
        submit = ctk.CTkButton(
            self, text="Search", command=lambda: self.getSuppliesForProcedure(code.get()),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_supply_opts()
        )

        self.entries = [code]
        self.elements = [label] + self.entries + [submit, med, self.medication_results_box, equip, self.equipment_results_box, back]

        # render all elements 
        for element in self.elements:
            element.pack()

    def getSuppliesForProcedure(self, pid):
        
        medicationQuerySql = "Select * From procedure_requires JOIN medication ON PID = {};".format(pid)

        equipmentQuerySql = "Select * From procedure_requires JOIN equipmennt ON PID = {};".format(pid)
        
        medication_text = ""
        equipment_text = ""

        try:
            cursor.execute(medicationQuerySql)
            medications = cursor.fetchall()
            for medication in medications:
                medication_text += "Name: {} \nCode: {}\nExpiration: {}\nDose: {}\nForm: {}\n\n".format(medication[0], medication[1], medication[2], medication[3], medication[4])
            self.medication_results_box.configure(state=ctk.NORMAL)
            self.medication_results_box.delete("0.0", "end")
            self.medication_results_box.insert("0.0", medication_text)
            self.medication_results_box.configure(state=ctk.DISABLED)  

            cursor.execute(equipmentQuerySql)
            equipment = cursor.fetchall()
            for piece in equipment:
                equipment_text += "Name: {}\nCode: {}\nLifetime: {}\nHours: {}\nType: {}".format(equipment[0], equipment[1], equipment[2], equipment[3], equipment[4])
            self.equipment_results_box.configure(state=ctk.NORMAL)
            self.equipment_results_box.delete("0.0", "end")
            self.equipment_results_box.insert("0.0", equipment_text)
            self.equipment_results_box.configure(state=ctk.DISABLED)  

        except Exception as e:
            print(e)

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

def updateMedicationInDatabase(name: str, code: str, expiration: str, dose: str, form: str):

    medicationSql = "UPDATE medication, supplies SET Med_Name='{}', Expiration=STR_TO_DATE('{}','%m-%d-%Y'), Dose='{}', Form='{}' WHERE medication.Supply_code='{}' AND supplies.Supply_code='{}'"
    medicationVal = (name, expiration, dose, form, code, code)

    try:
        cursor.execute(medicationSql.format(*medicationVal))
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
