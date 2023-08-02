import customtkinter as ctk
from dbConfig import db

def getUnoccupiedDoctorRooms() -> list[str]:
    # get unoccupied doctor room numbers
    query = "SELECT room_num FROM room WHERE room_type='Doctor Office' AND room_num NOT IN (SELECT room_num FROM doctor);"
    mycursor = db.cursor()
    mycursor.execute(query)
    unoccupied_rooms = mycursor.fetchall()
    rooms = [str(room[0]) for room in unoccupied_rooms]
    if len(rooms) == 0:
        return [""]
    return rooms

class DoctorOpts(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Select an option")
        doctorBySSN = ctk.CTkButton(
            self,
            text="Search doctor by SSN",
            command=lambda: controller.show_frame("DoctorBySSN"),
        )
        doctorByName = ctk.CTkButton(
            self,
            text="Search doctor by name",
            command=lambda: controller.show_frame("DoctorByName"),
        )
        addDoctor = ctk.CTkButton(
            self,
            text="Add doctor",
            command=lambda: controller.show_frame("AddDoctor"),
        )
        changeDoctor = ctk.CTkButton(
            self,
            text="Change doctor info",
            command=lambda: controller.show_frame("ChangeDoctor"),
        )
        back = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: controller.show_frame("StartPage"),
        )

        label.pack(side="top", fill="x", pady=10)
        doctorBySSN.pack()
        doctorByName.pack()
        addDoctor.pack()
        changeDoctor.pack()
        back.pack()


class DoctorByName(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.results_box = ctk.CTkTextbox(self, width=500)
        label = ctk.CTkLabel(self, text="Search Doctor By Name")
        self.first = ctk.CTkEntry(self, placeholder_text="First name")
        self.last = ctk.CTkEntry(self, placeholder_text="Last name")
        self.searchBtn = ctk.CTkButton(
            self,
            text="Search",
            command=self.search,
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame("DoctorOpts")
        )
        self.entries = [self.first, self.last]
        label.pack(side="top", fill="x", pady=10)
        self.first.pack()
        self.last.pack()
        self.searchBtn.pack()
        back.pack()
        self.results_box.pack()

    def search(self):
        query = "SELECT first_name, last_name, d.ssn FROM doctor AS d JOIN person AS pe ON d.ssn = pe.ssn WHERE first_name='{}' AND last_name='{}'".format(
            self.first.get(), self.last.get()
        )
        mycursor = db.cursor()
        mycursor.execute(query)
        doctors = mycursor.fetchall()
        labelText = ""
        if len(doctors) == 0:
            labelText = "There is no doctor named {} {}".format(
                self.first.get(), self.last.get()
            )
        else:
            labelText = "Doctors named {} {}:\n".format(
                self.first.get(), self.last.get()
            )
            for doctor in doctors:
                labelText += "Name: {} {}\nSSN: {}\n\n".format(
                    doctor[0], doctor[1], doctor[2]
                )

        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.insert("0.0", labelText)
        self.results_box.configure(state=ctk.DISABLED)

    def tkraise(self):
        self.first.delete(0, ctk.END)
        self.first.configure(placeholder_text="First name")
        self.last.delete(0, ctk.END)
        self.last.configure(placeholder_text="Last name")
        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.configure(state=ctk.DISABLED)
        super().tkraise()


class AddDoctor(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.resultsBox = ctk.CTkTextbox(self, width=500)

        self.label = ctk.CTkLabel(self, text="Enter doctor information", width=200)
        self.first = ctk.CTkEntry(self, placeholder_text="first name", width=200)
        self.last = ctk.CTkEntry(self, placeholder_text="last name", width=200)
        self.ssn = ctk.CTkEntry(self, placeholder_text="SSN", width=200)
        self.specialty = ctk.CTkEntry(
            self, placeholder_text="Specialty", width=200
        )

        # get unoccupied doctor room numbers
        self.roomNum = ctk.CTkOptionMenu(self, values=getUnoccupiedDoctorRooms())
        self.room_num_label = ctk.CTkLabel(self, text="Room number")

        add = ctk.CTkButton(
            self,
            text="Add",
            command=self.add,
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: controller.show_frame("DoctorOpts")
        )

        self.label.pack()
        self.first.pack()
        self.last.pack()
        self.ssn.pack()
        self.specialty.pack()
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
        self.specialty.delete(0, ctk.END)
        self.specialty.configure(placeholder_text="Specialty")
        self.resultsBox.configure(state=ctk.NORMAL)
        self.resultsBox.delete("0.0", "end")
        self.resultsBox.configure(state=ctk.DISABLED)
        super().tkraise()

    def add(self):
        person_query = "INSERT INTO person VALUES ({}, '{}', '{}', NULL, NULL);"
        doctor_query = "INSERT INTO doctor VALUES ({}, '{}', '{}');"
        mycursor = db.cursor()
        try:
            mycursor.execute(
                person_query.format(
                    self.ssn.get(),
                    self.last.get(),
                    self.first.get(),
                )
            )
            mycursor.execute(
                doctor_query.format(
                    self.ssn.get(), self.specialty.get()
                )
            )
            db.commit()
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert(
                "0.0",
                "Added Dr. {} {} to the database".format(self.first.get(), self.last.get()),
            )
            self.resultsBox.configure(state=ctk.DISABLED)
            self.roomNum.configure(
                values=getUnoccupiedDoctorRooms(),
            )
            self.roomNum.set(self.roomNum._values[0])
        except:
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert(
                "0.0",
                "Unable to add Dr. {} {} to the database".format(
                    self.first.get(), self.last.get()
                ),
            )
            self.resultsBox.configure(state=ctk.DISABLED)


class ChangeDoctor(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.resultsBox = ctk.CTkTextbox(self, width=500)
        self.label = ctk.CTkLabel(
            self, text="Select the doctor you would like to change"
        )
        self.doctors = ctk.CTkOptionMenu(self, values=self.getDoctors())
        self.getDoctor = ctk.CTkButton(
            self, text="Get doctor", command=self.populateEntries
        )
        self.first = ctk.CTkEntry(self, placeholder_text="First name")
        self.last = ctk.CTkEntry(self, placeholder_text="Last name")
        self.specialty = ctk.CTkEntry(self, placeholder_text="Specialty")
        self.roomNumLabel = ctk.CTkLabel(self, text="Room number")
        self.roomNum = ctk.CTkOptionMenu(self, values=getUnoccupiedDoctorRooms())
        self.changeBtn = ctk.CTkButton(self, text="Change", command=self.change)

        self.back = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: self.controller.show_frame("DoctorOpts"),
        )

        self.label.pack()
        self.doctors.pack()
        self.getDoctor.pack()

        self.first.pack()
        self.last.pack()
        self.specialty.pack()
        self.roomNumLabel.pack()
        self.roomNum.pack()
        self.changeBtn.pack()
        self.resultsBox.pack()
        self.back.pack(pady=10)

    def change(self):
        try:
            personQuery = "UPDATE person SET first_name='{}', last_name='{}' WHERE ssn={};".format(
                self.first.get(),
                self.last.get(),
                self.doctors.get().split(" ")[0],  # ssn
            )
            doctorQuery = "UPDATE doctor SET specialty='{}', room_num={} WHERE ssn={}".format(
                self.specialty.get(), self.roomNum.get(), self.doctors.get().split(" ")[0]
            )
            mycursor = db.cursor()
            mycursor.execute(personQuery)
            mycursor.execute(doctorQuery)
            db.commit()
            labelText = "Dr. {} information was changed".format(self.doctors.get())
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert("0.0", labelText)
            self.resultsBox.configure(state=ctk.DISABLED)
        except Exception as e:
            labelText = "Unable to change Dr. {}".format(self.doctors.get())
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert("0.0", labelText)
            self.resultsBox.configure(state=ctk.DISABLED)

    def populateEntries(self):
        doctorSsn = self.doctors.get().split(" ")[0]
        query = "SELECT first_name, last_name, specialty, room_num FROM doctor AS d JOIN person AS pe ON pe.ssn = d.ssn WHERE d.ssn={};".format(
            doctorSsn
        )
        mycursor = db.cursor()
        mycursor.execute(query)
        doctor = mycursor.fetchall()[0]

        self.first.delete(0, ctk.END)
        self.first.insert(string=doctor[0], index=0)
        self.last.delete(0, ctk.END)
        self.last.insert(string=doctor[1], index=0)
        self.specialty.delete(0, ctk.END)
        self.specialty.insert(string=doctor[2], index=0)
        rooms = getUnoccupiedDoctorRooms()
        rooms.append(str(doctor[3]))
        self.roomNum.configure(values=rooms)  # append current doctor room number

    def getDoctors(self) -> list[str]:
        query = "SELECT d.ssn, first_name, last_name FROM doctor AS d JOIN person AS pe ON d.ssn = pe.ssn;"
        mycursor = db.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        doctors = [
            str(doctor[0]) + " " + str(doctor[1]) + " " + str(doctor[2])
            for doctor in result
        ]
        if len(doctors) == 0:
            return [""]
        return doctors

    def tkraise(self):
        self.doctors.configure(values=self.getDoctors())
        self.first.delete(0, ctk.END)
        self.first.configure(placeholder_text="First name")
        self.last.delete(0, ctk.END)
        self.last.configure(placeholder_text="Last name")
        self.specialty.delete(0, ctk.END)
        self.specialty.configure(placeholder_text="Specialty")
        self.resultsBox.configure(state=ctk.NORMAL)
        self.resultsBox.delete("0.0", "end")
        self.resultsBox.configure(state=ctk.DISABLED)
        super().tkraise()


class DoctorBySSN(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.results_box = ctk.CTkTextbox(self, width=500)
        label = ctk.CTkLabel(self, text="Search Doctor By SSN")
        self.ssn = ctk.CTkEntry(self, placeholder_text="SSN")
        self.searchBtn = ctk.CTkButton(
            self,
            text="Search",
            command=self.search,
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame("DoctorOpts")
        )
        self.entries = [self.ssn]
        label.pack(side="top", fill="x", pady=10)
        self.ssn.pack()
        self.searchBtn.pack()
        back.pack()
        self.results_box.pack()

    def search(self):
        query = "SELECT first_name, last_name, d.ssn, Specialty FROM specialty_salary AS s, doctor AS d JOIN person AS pe ON d.ssn = pe.ssn WHERE d.ssn={}".format(
            self.ssn.get()
        )
        mycursor = db.cursor()
        mycursor.execute(query)
        doctors = mycursor.fetchall()
        labelText = ""
        if len(doctors) == 0:
            labelText = "There is no doctor with SSN {}".format(self.ssn.get())
        else:
            doctor = doctors[0]
            labelText = "Name: {} {}\nSSN: {}\n\n".format(
                doctor[0], doctor[1], doctor[2]
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