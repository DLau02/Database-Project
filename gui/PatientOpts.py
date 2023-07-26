import customtkinter as ctk
from dbConfig import db


class PatientOpts(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Select an option")
        patient_by_name = ctk.CTkButton(
            self,
            text="Search patient by name",
            command=lambda: controller.show_frame("PatientByName"),
        )
        add_patient = ctk.CTkButton(
            self,
            text="Add patient",
            command=lambda: controller.show_frame("AddPatient"),
        )
        back = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: controller.show_frame("StartPage"),
        )

        label.pack(side="top", fill="x", pady=10)
        patient_by_name.pack()
        add_patient.pack()
        back.pack()


class PatientByName(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.results_box=ctk.CTkTextbox(self, width=500)
        label = ctk.CTkLabel(self, text="Search Patient By Name")
        label.pack(side="top", fill="x", pady=10)
        first = ctk.CTkEntry(self, placeholder_text="first name")
        last = ctk.CTkEntry(self, placeholder_text="last name")
        # results_box = ctk.CTkTextbox(self, width=500)
        search = ctk.CTkButton(
            self,
            text="Search",
            command=lambda: self.search(first.get(), last.get()),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_patient_opts()
        )
        self.entries = [first, last]
        first.pack()
        last.pack()
        search.pack()
        back.pack()
        self.results_box.pack()

    def clear_entries(self):
        pass

    def goto_patient_opts(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)
        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.configure(state=ctk.DISABLED)

        self.controller.show_frame("PatientOpts")

    def search(self, first_name: str, last_name: str):
        query = " select first_name,last_name,pa.ssn,address,birthdate,room_num from patient as pa join person as pe on pa.ssn=pe.ssn where first_name='{}' and last_name='{}' "
        mycursor = db.cursor()
        mycursor.execute(query.format(first_name, last_name))
        people = mycursor.fetchall()
        label_text = "There are {} patients named {} {}\n".format(
            len(people), first_name, last_name
        )
        for person in people:
            label_text += "Name: {} {}\nSSN: {}\nBirthdate: {}\nAddress: {}\nRoom Number:{}\n\n".format(
                person[0], person[1], person[2], person[3], person[4], person[5]
            )
        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.insert("0.0", label_text)
        self.results_box.configure(state=ctk.DISABLED)


class AddPatient(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Enter patient information", width=200)
        first = ctk.CTkEntry(self, placeholder_text="first name", width=200)
        last = ctk.CTkEntry(self, placeholder_text="last name", width=200)
        ssn = ctk.CTkEntry(self, placeholder_text="SSN", width=200)
        street_address = ctk.CTkEntry(
            self, placeholder_text="Street Address", width=200
        )
        city = ctk.CTkEntry(self, placeholder_text="City", width=200)
        state = ctk.CTkEntry(self, placeholder_text="State", width=200)
        zipcode = ctk.CTkEntry(self, placeholder_text="Zip code", width=200)
        birthday = ctk.CTkEntry(
            self, placeholder_text="Birthday: MM-DD-YYYY", width=200
        )
        room_num = ctk.CTkEntry(self, placeholder_text="Room Number", width=200)
        results_box = ctk.CTkTextbox(self, width=500)
        add = ctk.CTkButton(
            self,
            text="Add",
            # command=lambda: self.search(first.get(), last.get(), results_box),
        )
        back = ctk.CTkButton(
            self, text="Go back", command=lambda: controller.show_frame("StartPage")
        )

        elements = [
            label,
            first,
            last,
            ssn,
            street_address,
            city,
            zipcode,
            state,
            birthday,
            room_num,
            results_box,
            add,
            back,
        ]
        for element in elements:
            element.pack()

    def add(self, ssn, address, last_name, first_name, birthdate, room_num):
        query = "insert into person values ({}, '{}, {}, {}, {}, {}', '{}', '{}', STR_TO_DATE('{}','%m-%d-%Y')); "
        mycursor = db.cursor()
        try:
            mycursor.execute(
                query.format(
                    ssn,
                    address,
                    last_name,
                    first_name,
                    birthdate,
                )
            )
            # results_box.configure(state=ctk.NORMAL)
            # results_box.delete("0.0", "end")
            # results_box.insert("0.0", label_text)
            # results_box.configure(state=ctk.DISABLED)
        except Exception as e:
            print(e)
