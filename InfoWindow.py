from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


class InfoWindow:
    def __init__(self, win, address_bookObj, contact_name=None):
        self.frame_photo = Frame(win, height=100, width=300)
        self.frame_info = Frame(win, height=150, width=300)
        self.frame_button = Frame(win, height=50, width=300)
        self.frame_photo.place(x=300, y=0)
        self.frame_info.place(x=300, y=100)
        self.frame_button.place(x=300, y=250)

        self.address_book = address_bookObj

        if contact_name is not None:
            self.contact = self.address_book.searchList(contact_name)
            self.show_contact()
        else:
            self.new_contact()

    def stating_page(self):
        self.frame_photo.configure(background="grey")
        self.frame_info.configure(background="yellow")
        self.frame_button.configure(background="blue")

    def create_infoLabel(self):
        Label(self.frame_info, text="Name:").grid(row=0, column=0, sticky=W, padx=10, pady=8)
        Label(self.frame_info, text="Address:").grid(row=2, column=0, sticky=W, padx=10, pady=8)
        Label(self.frame_info, text="Phone:").grid(row=1, column=0, sticky=W, padx=10, pady=8)
        Label(self.frame_info, text="Email:").grid(row=3, column=0, sticky=W, padx=10, pady=8)

    def new_contact(self):
        self.create_infoLabel()

        name = Entry(self.frame_info,width=30)
        address = Entry(self.frame_info,width=30)
        phone = Entry(self.frame_info,width=30)
        email = Entry(self.frame_info,width=30)

        name.grid(row=0, column=1)
        address.grid(row=1, column=1)
        phone.grid(row=2, column=1)
        email.grid(row=3, column=1)

    def show_contact(self):
        self.show_photo()
        self.create_infoLabel()

        self.nameLabel = Label(self.frame_info, text=self.contact.get("Name"),width=30)
        self.nameLabel.grid(row=0, column=1)
        self.phoneLabel = Label(self.frame_info, text=self.contact.get("Phone"),width=30)
        self.phoneLabel.grid(row=1, column=1)
        self.addressLabel = Label(self.frame_info, text=self.contact.get("Address"),width=30)
        self.addressLabel.grid(row=2, column=1)
        self.emailLabel = Label(self.frame_info, text=self.contact.get("Email"),width=30)
        self.emailLabel.grid(row=3, column=1)

        self.button1 = Button(self.frame_button, text="edit", command=self.edit_contact,width=10)
        self.button2 = Button(self.frame_button, text="delete", command=self.delete_contact,width=10)
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)

    def edit_contact(self):
        self.create_infoLabel()

        self.nameLabel.grid_forget()
        self.addressLabel.grid_forget()
        self.phoneLabel.grid_forget()
        self.emailLabel.grid_forget()

        self.nameEntry = Entry(self.frame_info,width=30)
        self.nameEntry.insert(END, self.contact.get("Name"))
        self.phoneEntry = Entry(self.frame_info,width=30)
        self.phoneEntry.insert(END, self.contact.get("Phone"))
        self.addressEntry = Entry(self.frame_info,width=30)
        self.addressEntry.insert(END, self.contact.get("Address"))
        self.emailEntry = Entry(self.frame_info,width=30)
        self.emailEntry.insert(END, self.contact.get("Email"))

        self.nameEntry.grid(row=0, column=1)
        self.phoneEntry.grid(row=1, column=1)
        self.addressEntry.grid(row=2, column=1)
        self.emailEntry.grid(row=3, column=1)

        self.button_editPhoto = Button(self.frame_photo, text="edit", command=self.edit_photo)
        self.button_editPhoto.grid(row=0, column=1)

        self.button1.configure(text="save",command=lambda: self.save_contact(self.nameEntry.get(), self.phoneEntry.get(),
                                                                     self.addressEntry.get(), self.emailEntry.get()))
        self.button2.configure(text="cancel", command=self.cancel)

    def save_contact(self, name, address, phone, email):
        # new_info = [name, phone, email, address]
        # if self.address_book.isNameInAddressBook(self.contact["Name"]):
        #     self.address_book.editContact(new_info)
        # else:
        #     self.address_book.add_contact(new_info)
        # self.show_contact()
        pass

    def delete_contact(self):
        # self.address_book.deleteContact(self.contact["Name"])
        pass

    def cancel(self):
        self.button1.grid_forget()
        self.button2.grid_forget()
        self.button_editPhoto.grid_forget()
        self.nameEntry.grid_forget()
        self.phoneEntry.grid_forget()
        self.addressEntry.grid_forget()
        self.emailEntry.grid_forget()

        self.show_contact()

    def show_photo(self):
        image = Image.open("blank_profile.jpg")
        # FixMe blank profile has to be initialized
        # use if to see how to initialize
        image = image.resize((100, 100), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)

        self.image = Label(self.frame_photo, image=self.photo, height=100, width=100)
        self.image.grid(row=0, column=0)

    def edit_photo(self):
        # FixMe need to save the photo
        file_path = filedialog.askopenfilename()

        image = Image.open(file_path)
        image = image.resize((100, 100), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(image)
        self.image.configure(image=self.photo)

    def exit_window(self):
        self.frame_photo.destroy()
        self.frame_info.destroy()
        self.frame_button.destroy()


def main():
    root = Tk()
    IW = InfoWindow(root)
    IW.show_contact()
    # IW.new_contact()
    root.mainloop()


if __name__ == "__main__":
    main()
