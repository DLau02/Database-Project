import customtkinter as ctk
from dbConfig import db


def getUnoccupiedPatientRooms() -> list[str]:
    # get unoccupied patient room numbers
    query = "select room_num from room where room_type='Patient Room' and room_num not in (select room_num from patient);"
    mycursor = db.cursor()
    mycursor.execute(query)
    unoccupied_rooms = mycursor.fetchall()
    rooms = [str(room[0]) for room in unoccupied_rooms]
    if len(rooms) == 0:
        return [""]
    return rooms


class PatientOpts(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Select an option")
        patientBySsn = ctk.CTkButton(
            self,
            text="Search patient by SSN",
            command=lambda: controller.show_frame("PatientBySSN"),
        )
        patientByName = ctk.CTkButton(
            self,
            text="Search patient by name",
            command=lambda: controller.show_frame("PatientByName"),
        )
        addPatient = ctk.CTkButton(
            self,
            text="Add patient",
            command=lambda: controller.show_frame("AddPatient"),
        )
        changePatient = ctk.CTkButton(
            self,
            text="Change patient info",
            command=lambda: controller.show_frame("ChangePatient"),
        )
        back = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: controller.show_frame("StartPage"),
        )

        label.pack(side="top", fill="x", pady=10)
        patientBySsn.pack()
        patientByName.pack()
        addPatient.pack()
        changePatient.pack()
        back.pack()


class PatientByName(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.resultsBox = ctk.CTkTextbox(self, width=500)
        self.label = ctk.CTkLabel(self, text="Search Patient By Name")
        self.label.pack(side="top", fill="x", pady=10)
        self.first = ctk.CTkEntry(self, placeholder_text="first name")
        self.last = ctk.CTkEntry(self, placeholder_text="last name")
        self.searchBtn = ctk.CTkButton(
            self,
            text="Search",
            command=lambda: self.search(),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame("PatientOpts")
        )
        self.first.pack()
        self.last.pack()
        self.searchBtn.pack()
        back.pack()
        self.resultsBox.pack()

    def tkraise(self):
        self.first.delete(0, ctk.END)
        self.first.configure(placeholder_text="First name")
        self.last.delete(0, ctk.END)
        self.last.configure(placeholder_text="Last name")
        self.resultsBox.configure(state=ctk.NORMAL)
        self.resultsBox.delete("0.0", "end")
        self.resultsBox.configure(state=ctk.DISABLED)
        super().tkraise()

    def search(self):
        query = "select first_name,last_name,pa.ssn,address,birthdate,room_num from patient as pa join person as pe on pa.ssn=pe.ssn where first_name='{}' and last_name='{}' ".format(
            self.first.get(), self.last.get()
        )
        mycursor = db.cursor()
        mycursor.execute(query)
        people = mycursor.fetchall()
        labelText = "There are {} patients named {} {}\n".format(
            len(people), self.first.get(), self.last.get()
        )
        for person in people:
            labelText += "Name: {} {}\nSSN: {}\nBirthdate: {}\nAddress: {}\nRoom Number:{}\n\n".format(
                person[0], person[1], person[2], person[3], person[4], person[5]
            )
        self.resultsBox.configure(state=ctk.NORMAL)
        self.resultsBox.delete("0.0", "end")
        self.resultsBox.insert("0.0", labelText)
        self.resultsBox.configure(state=ctk.DISABLED)


class AddPatient(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.resultsBox = ctk.CTkTextbox(self, width=500)

        self.label = ctk.CTkLabel(self, text="Enter patient information", width=200)
        self.first = ctk.CTkEntry(self, placeholder_text="first name", width=200)
        self.last = ctk.CTkEntry(self, placeholder_text="last name", width=200)
        self.ssn = ctk.CTkEntry(self, placeholder_text="SSN", width=200)
        self.address = ctk.CTkEntry(
            self, placeholder_text="Address: Street, City, State Zip", width=200
        )

        self.birthdate = ctk.CTkEntry(
            self, placeholder_text="Birthdate: YYYY-MM-DD", width=200
        )

        # get unoccupied patient room numbers
        self.roomNum = ctk.CTkOptionMenu(self, values=getUnoccupiedPatientRooms())
        self.room_num_label = ctk.CTkLabel(self, text="Room number")

        add = ctk.CTkButton(
            self,
            text="Add",
            command=self.add,
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: controller.show_frame("PatientOpts")
        )

        self.label.pack()
        self.first.pack()
        self.last.pack()
        self.ssn.pack()
        self.birthdate.pack()
        self.address.pack()
        self.room_num_label.pack()
        self.roomNum.pack(pady=5)
        add.pack()
        back.pack()
        self.resultsBox.pack()

    def tkraise(self):
        self.first.delete(0, ctk.END)
        self.first.configure(placeholder_text="First name")
        self.last.delete(0, ctk.END)
        self.last.configure(placeholder_text="Last name")
        self.ssn.delete(0, ctk.END)
        self.ssn.configure(placeholder_text="SSN")
        self.birthdate.delete(0, ctk.END)
        self.birthdate.configure(placeholder_text="Birthdate: YYYY-MM-DD")
        self.resultsBox.configure(state=ctk.NORMAL)
        self.resultsBox.delete("0.0", "end")
        self.resultsBox.configure(state=ctk.DISABLED)
        super().tkraise()

    def add(self):
        person_query = "insert into person values ({}, '{}', '{}', '{}', STR_TO_DATE('{}','%Y-%m-%d'));"
        patient_query = "insert into patient values ({}, {})"
        mycursor = db.cursor()
        try:
            mycursor.execute(
                person_query.format(
                    self.ssn.get(),
                    self.address.get(),
                    self.last.get(),
                    self.first.get(),
                    self.birthdate.get(),
                )
            )
            mycursor.execute(patient_query.format(self.ssn.get(), self.roomNum.get()))
            db.commit()
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert(
                "0.0",
                "Added {} {} to database".format(self.first.get(), self.last.get()),
            )
            self.resultsBox.configure(state=ctk.DISABLED)
            self.roomNum.configure(
                values=getUnoccupiedPatientRooms(),
            )
            self.roomNum.set(self.roomNum._values[0])
        except:
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert(
                "0.0",
                "Unable to add {} {} to the database".format(
                    self.first.get(), self.last.get()
                ),
            )
            self.resultsBox.configure(state=ctk.DISABLED)


class ChangePatient(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.resultsBox = ctk.CTkTextbox(self, width=500)
        self.label = ctk.CTkLabel(
            self, text="Select the patient you would like to change"
        )
        self.patients = ctk.CTkOptionMenu(self, values=self.getPatients())
        self.getPatient = ctk.CTkButton(
            self, text="Get patient", command=self.populateEntries
        )
        self.first = ctk.CTkEntry(self, placeholder_text="First name")
        self.last = ctk.CTkEntry(self, placeholder_text="Last name")
        self.roomNumLabel = ctk.CTkLabel(self, text="Room number")
        self.roomNum = ctk.CTkOptionMenu(self, values=getUnoccupiedPatientRooms())
        self.birthdate = ctk.CTkEntry(self, placeholder_text="Birthdate: YYYY-MM-DD")
        self.address = ctk.CTkEntry(self, placeholder_text="Address")
        self.changeBtn = ctk.CTkButton(self, text="Change", command=self.change)

        self.back = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: self.controller.show_frame("PatientOpts"),
        )

        self.label.pack()
        self.patients.pack()
        self.getPatient.pack()

        self.first.pack()
        self.last.pack()
        self.roomNumLabel.pack()
        self.roomNum.pack()
        self.birthdate.pack()
        self.address.pack()
        self.changeBtn.pack()
        self.resultsBox.pack()
        self.back.pack(pady=10)

    def change(self):
        try:
            personQuery = "update person set first_name='{}', last_name='{}', address='{}', birthdate=STR_TO_DATE('{}','%Y-%m-%d') where ssn={};".format(
                self.first.get(),
                self.last.get(),
                self.address.get(),
                self.birthdate.get(),
                self.patients.get().split(" ")[0],  # ssn
            )
            patientQuery = "update patient set room_num={} where ssn={}".format(
                self.roomNum.get(), self.patients.get().split(" ")[0]
            )
            mycursor = db.cursor()
            mycursor.execute(personQuery)
            mycursor.execute(patientQuery)
            db.commit()
            labelText = "{} information was changed".format(self.patients.get())
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert("0.0", labelText)
            self.resultsBox.configure(state=ctk.DISABLED)
        except Exception as e:
            # print(e)
            labelText = "Unable to change patient {}".format(self.patients.get())
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert("0.0", labelText)
            self.resultsBox.configure(state=ctk.DISABLED)

    def populateEntries(self):
        patientSsn = self.patients.get().split(" ")[0]
        query = "select first_name, last_name,address,birthdate,room_num from patient as pa join person as pe on pe.ssn=pa.ssn where pa.ssn={};".format(
            patientSsn
        )
        mycursor = db.cursor()
        mycursor.execute(query)
        patient = mycursor.fetchall()[0]

        self.first.delete(0, ctk.END)
        self.first.insert(string=patient[0], index=0)
        self.last.delete(0, ctk.END)
        self.last.insert(string=patient[1], index=0)
        self.address.delete(0, ctk.END)
        self.address.insert(string=patient[2], index=0)
        self.birthdate.delete(0, ctk.END)
        self.birthdate.insert(string=patient[3], index=0)
        rooms = getUnoccupiedPatientRooms()
        rooms.append(str(patient[4]))
        self.roomNum.configure(values=rooms)  # append current patient room number

    def getPatients(self) -> list[str]:
        query = "select pa.ssn,first_name,last_name from patient as pa join person as pe on pa.ssn=pe.ssn;"
        mycursor = db.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        patients = [
            str(patient[0]) + " " + str(patient[1]) + " " + str(patient[2])
            for patient in result
        ]
        if len(patients) == 0:
            return [""]
        return patients

    def tkraise(self):
        self.patients.configure(values=self.getPatients())
        self.first.delete(0, ctk.END)
        self.first.configure(placeholder_text="First name")
        self.last.delete(0, ctk.END)
        self.last.configure(placeholder_text="Last name")
        self.address.delete(0, ctk.END)
        self.address.configure(placeholder_text="Address")
        self.birthdate.delete(0, ctk.END)
        self.birthdate.configure(placeholder_text="Birthdate: YYYY-MM-DD")
        super().tkraise()


class PatientBySSN(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.results_box = ctk.CTkTextbox(self, width=500)
        label = ctk.CTkLabel(self, text="Search Patient By SSN")
        self.ssn = ctk.CTkEntry(self, placeholder_text="SSN")
        self.searchBtn = ctk.CTkButton(
            self,
            text="Search",
            command=self.search,
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame("PatientOpts")
        )
        self.entries = [self.ssn]
        label.pack(side="top", fill="x", pady=10)
        self.ssn.pack()
        self.searchBtn.pack()
        back.pack()
        self.results_box.pack()

    def search(self):
        query = "select first_name,last_name,pa.ssn,address,birthdate,room_num from patient as pa join person as pe on pa.ssn=pe.ssn where pa.ssn={}"
        mycursor = db.cursor()
        mycursor.execute(query.format(self.ssn.get()))
        people = mycursor.fetchall()
        labelText = ""
        if len(people) == 0:
            labelText = "There is no patient with ssn {}".format(self.ssn.get())
        else:
            person = people[0]
            labelText = "Name: {} {}\nSSN: {}\nBirthdate: {}\nAddress: {}\nRoom Number:{}\n\n".format(
                person[0], person[1], person[2], person[3], person[4], person[5]
            )
        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.insert("0.0", labelText)
        self.results_box.configure(state=ctk.DISABLED)

    def tkraise(self):
        self.ssn.delete(0, ctk.END)
        self.ssn.configure(placeholder_text="SSN")
        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.configure(state=ctk.DISABLED)
        super().tkraise()
