import sys
import customtkinter as ctk
from PatientOpts import *
from SupplyOpts import (
    SupplyOpts,
    AddMedication,
    SearchMedication,
    AddEquipment,
    SearchEquipment,
    SuppliesforProcedure,
)
from Invoice import Invoice, ViewInvoice, AddInvoice, UpdateInvoice

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.geometry("800x500")
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (
            StartPage,
            PatientOpts,
            AddPatient,
            PatientByName,
            PatientBySSN,
            ChangePatient,
            SupplyOpts,
            AddMedication,
            SearchMedication,
            AddEquipment,
            SearchEquipment,
            SuppliesforProcedure,
            Invoice,
            ViewInvoice,
            AddInvoice,
            UpdateInvoice
        ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
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
        Invoice = ctk.CTkButton(
            self,
            text="Invoices",
            command=lambda: controller.show_frame("Invoice"),
        )
        exit_btn = ctk.CTkButton(self, text="Exit", command=lambda: sys.exit(0))

        label.pack(side="top", fill="x", pady=10)
        patient_by_name.pack()
        SupplyOpts.pack()
        Invoice.pack()
        exit_btn.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
