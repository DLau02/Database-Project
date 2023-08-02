import customtkinter as ctk
from dbConfig import db


'''def getUnoccupiedDoctorRooms() -> list[str]:
    # get unoccupied doctor room numbers
    query = "SELECT Room_Num FROM room WHERE room_type='Doctor Office' AND Room_Num NOT IN (SELECT Room_Num FROM doctor);"
    mycursor = db.cursor()
    mycursor.execute(query)
    unoccupied_rooms = mycursor.fetchall()
    rooms = [str(room[0]) for room in unoccupied_rooms]
    if len(rooms) == 0:
        return ["No offices available"]
    return rooms'''


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
        query = "SELECT first_name, last_name, d.ssn FROM doctor AS d JOIN person AS pe ON d.ssn = pe.ssn WHERE first_name=%s AND last_name=%s"
        queryVal = (self.first.get(), self.last.get())
        mycursor = db.cursor()
        mycursor.execute(query, queryVal)
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
        self.date = ctk.CTkEntry(self, placeholder_text="date of birth", width=200)
        self.address = ctk.CTkEntry(self, placeholder_text="address", width=200)
        self.specialty = ctk.CTkEntry(self, placeholder_text="specialty", width=200)
        self.department = ctk.CTkEntry(self, placeholder_text="department", width=200)

        # get unoccupied doctor room numbers
        #optionbox_var = ctk.StringVal(value="No room Available")
        #self.roomNum = ctk.CTkOptionMenu(self, values=getUnoccupiedDoctorRooms(), variable=optionbox_var, command=getUnoccupiedDoctorRooms())
        #self.room_num_label = ctk.CTkLabel(self, text="Room number")

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
        self.address.pack()
        self.date.pack()
        self.specialty.pack()
        self.department.pack()
        #self.room_num_label.pack()
        #self.roomNum.pack(pady=5)
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
        #self.specialty.delete(0, ctk.END)
        #self.specialty.configure(placeholder_text="Specialty")
        self.address.delete(0, ctk.END)
        self.address.configure(placeholder_text = "Address")
        self.date.delete(0, ctk.END)
        self.date.configure(placeholder_text = "Date of birth")
        self.resultsBox.configure(state=ctk.NORMAL)
        self.resultsBox.delete("0.0", "end")
        self.resultsBox.configure(state=ctk.DISABLED)
        super().tkraise()

    def add(self):
        person_query = "INSERT INTO person VALUES (%s, %s, %s, %s, STR_TO_DATE(%s, '%Y-%m-%d'));"
        doctor_query = "INSERT INTO doctor VALUES (%s);"
        query2 = "Insert Into employee Values (%s, %s, %s)"
        queryVal2 = (self.ssn.get(), self.specialty.get(), self.department.get())
        queryVal=(
                    self.ssn.get(),
                    self.address.get(),
                    self.last.get(),
                    self.first.get(),
                    self.date.get(),
        )
        queryValue=(
            self.ssn.get(),
        )

        mycursor = db.cursor()

        try:
            
            mycursor.execute(
                person_query, queryVal
            )
            db.commit()
            mycursor.execute(query2, queryVal2)
            db.commit()
            mycursor.execute(doctor_query, queryValue)
            db.commit()

            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert(
                "0.0",
                "Added Dr. {} {} to the database".format(
                    self.first.get(), self.last.get()
                ),
            )
            self.resultsBox.configure(state=ctk.DISABLED)
        except Exception as e:
            db.rollback()  # Rollback the transaction in case of an error
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            label_text = "Error occurred: {}".format(str(e))
            self.resultsBox.insert("0.0", label_text)
            self.resultsBox.configure(state=ctk.DISABLED)
            '''self.roomNum.configure(
                values=getUnoccupiedDoctorRooms(),
            )'''
            #self.roomNum.set(self.roomNum._values[0])
        '''except:
            self.resultsBox.configure(state=ctk.NORMAL)
            self.resultsBox.delete("0.0", "end")
            self.resultsBox.insert(
                "0.0",
                "Unable to add Dr. {} {} to the database".format(
                    self.first.get(), self.last.get()
                ),
            )

            self.resultsBox.configure(state=ctk.DISABLED)'''
        

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
        # self.roomNumLabel = ctk.CTkLabel(self, text="Room number")
        # self.roomNum = ctk.CTkOptionMenu(self, values=getUnoccupiedDoctorRooms())
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
        # self.roomNumLabel.pack()
        # self.roomNum.pack()
        self.changeBtn.pack()
        self.resultsBox.pack()
        self.back.pack(pady=10)

    def change(self):
        try:
            # personQuery = "UPDATE person SET first_name='{}', last_name='{}' WHERE ssn={};".format(
            #     self.first.get(),
            #     self.last.get(),
            #     self.doctors.get().split(" ")[0],  # ssn
            # )
            # doctorQuery = "UPDATE employee SET specialty='{}' WHERE ssn={}".format(
            #     self.specialty.get(),
            #     # self.roomNum.get(),
            #     self.doctors.get().split(" ")[0],  # ssn
            # )
            personQuery = "UPDATE person SET first_name=%s, last_name=%s WHERE ssn=%s;"
            doctorQuery = "UPDATE employee SET specialty=%s WHERE ssn=%s"
            mycursor = db.cursor()
            mycursor.execute(
                personQuery,
                (self.first.get(), self.last.get(), self.doctors.get().split(" ")[0]),
            )
            mycursor.execute(doctorQuery, (self.specialty.get(),self.doctors.get().split(" ")[0]))
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
        # query = "SELECT first_name, last_name, specialty, room_num FROM doctor AS d JOIN person AS pe ON pe.ssn = d.ssn WHERE d.ssn={};".format(
        #     doctorSsn
        # )
        query = "select * from doctor natural join person natural join employee where ssn=%s"
        mycursor = db.cursor()
        mycursor.execute(query, (doctorSsn,))
        doctor = mycursor.fetchall()[0]

        self.first.delete(0, ctk.END)
        self.first.insert(string=doctor[3], index=0)
        self.last.delete(0, ctk.END)
        self.last.insert(string=doctor[2], index=0)
        self.specialty.delete(0, ctk.END)
        self.specialty.insert(string=doctor[5], index=0)
        # rooms = getUnoccupiedDoctorRooms()
        # rooms.append(str(doctor[3]))
        # self.roomNum.configure(values=rooms)  # append current doctor room number

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
        query = "SELECT first_name, last_name, d.ssn, Specialty FROM specialty_salary AS s, doctor AS d JOIN person AS pe ON d.ssn = pe.ssn WHERE d.ssn=%s"
        queryVal = (self.ssn.get(), )
        mycursor = db.cursor()
        mycursor.execute(query, queryVal)
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
