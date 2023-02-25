import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


def button_function():
    print("pressed")


def get_app():
    app = customtkinter.CTk()
    app.geometry("600x350")

    button = customtkinter.CTkButton(
        master=app,
        text="Press Me",
        command=button_function
    )

    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return app
