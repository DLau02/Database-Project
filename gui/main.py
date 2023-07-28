import sys
import customtkinter as ctk
import mysql.connector
from PatientOpts import PatientByName, PatientOpts, AddPatient
from SupplyOpts import SupplyOpts, AddMedication

from dbConfig import db

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.geometry("800x500")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PatientOpts, AddPatient, PatientByName, SupplyOpts, AddMedication):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Select an option")

        patient_by_name = ctk.CTkButton(
            self,
            text="Patient",
            command=lambda: controller.show_frame("PatientOpts"),
        )
        SupplyOpts = ctk.CTkButton(
            self,
            text="Supplies", 
            command=lambda: controller.show_frame("SupplyOpts"),
        )
        exit_btn = ctk.CTkButton(self, text="Exit", command=lambda: sys.exit(0))

        label.pack(side="top", fill="x", pady=10)
        patient_by_name.pack()
        SupplyOpts.pack()
        exit_btn.pack()


class DoctorByName(ctk.CTkFrame):
    pass


class ChangePatientRoom(ctk.CTkFrame):
    pass


class SearchSupply(ctk.CTkFrame):
    pass


class SearchSupplyByName(ctk.CTkFrame):
    pass


class SearchSupplyByNumber(ctk.CTkFrame):
    pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
