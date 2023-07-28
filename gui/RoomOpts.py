import customtkinter as ctk
from dbConfig import db


class RoomOpts(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Select an option")
        
        Room_Status = ctk.CTkButton(
            self,
            text="Search Room",
            command=lambda: controller.show_frame("Room_Status"),
        )
        Assign_Room = ctk.CTkButton(
            self,
            text="Assign Room",
            command=lambda: controller.show_frame("Assign_Room"),
        )
        back = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: controller.show_frame("StartPage"),
        )

        label.pack(side="top", fill="x", pady=10)
        Room_Status.pack()
        Assign_Room.pack()
        back.pack()


class Room_Status(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.results_box=ctk.CTkTextbox(self, width=500)
        label = ctk.CTkLabel(self, text="Search Room")
        label.pack(side="top", fill="x", pady=10)
        Room_Num = ctk.CTkEntry(self, placeholder_text="Room_Num")
        search = ctk.CTkButton(
            self,
            text="Search",
            command=lambda: self.search(Room_Num.get()),
        )
        back = ctk.CTkButton(
            self, text="Back", command=lambda: self.goto_room_opts()
        )
        self.entries = [Room_Num]
        Room_Num.pack()
        search.pack()
        back.pack()
        self.results_box.pack()

    def clear_entries(self):
        pass

    def goto_room_opts(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)
        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.configure(state=ctk.DISABLED)
        self.controller.show_frame("RoomOpts")

    def search(self, Room_Num: int):
        query = " select Room_Num, Room_type, SSN from room where Room_Num = '{}' "
        mycursor = db.cursor()
        mycursor.execute(query.format(Room_Num))

        # Fetch the results (assuming you expect only one row)
        result = mycursor.fetchone()

        if result:
            Room_Num, room_type, SSN = result
            label_text = "Room Number: {}\nRoom Type: {}\nSSN: {}\n\n".format(
                Room_Num, room_type, SSN
            )
        else:
            label_text = "Room not found."

        self.results_box.configure(state=ctk.NORMAL)
        self.results_box.delete("0.0", "end")
        self.results_box.insert("0.0", label_text)
        self.results_box.configure(state=ctk.DISABLED)



class Assign_Room(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Assign Room", width=200)
        Room_Num = ctk.CTkEntry(self, placeholder_text="Room_Num", width=200)
        Room_type = ctk.CTkEntry(self, placeholder_text="Room_type", width=200)
        ssn = ctk.CTkEntry(self, placeholder_text="SSN", width=200)
        
        results_box = ctk.CTkTextbox(self, width=500)
        add = ctk.CTkButton(
            self,
            text="Add",
            command=lambda: self.add(ssn.get(), Room_Num.get(), Room_type.get(), results_box),
        )
        back = ctk.CTkButton(
            self, text="Go back", command=lambda: controller.show_frame("StartPage")
        )

        elements = [
            label,
            ssn,
            Room_Num,
            Room_type,
            results_box,
            add,
            back,
        ]
        for element in elements:
            element.pack()
    
    def add(self, ssn, Room_Num, Room_type, results_box):
        query = " INSERT INTO room (SSN, Room_Num, Room_type) VALUES ('{}', '{}', '{}') "
        mycursor = db.cursor()
        try:
            mycursor.execute(
                query.format(
                    ssn,
                    Room_Num,
                    Room_type
                )
            )
            db.commit()  # Commit the transaction to save the changes in the database
            results_box.configure(state=ctk.NORMAL)
            results_box.delete("0.0", "end")
            label_text = "Information added successfully!"
            results_box.insert("0.0", label_text)
            results_box.configure(state=ctk.DISABLED)
        except Exception as e:
            db.rollback()  # Rollback the transaction in case of an error
            results_box.configure(state=ctk.NORMAL)
            results_box.delete("0.0", "end")
            label_text = "Error occurred: {}".format(str(e))
            results_box.insert("0.0", label_text)
            results_box.configure(state=ctk.DISABLED)
        
