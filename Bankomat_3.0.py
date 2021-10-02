from tkinter import messagebox
from buttons import *

FONT = ("Courier New", 10, "bold")
BFONT = ("Courier New", 13, "bold")

LIGHT_BLUE = "#abd2fa"
DARK_BLUE = "#7692ff"
numbers = ""


def atm():
    win = Tk()
    win.title("Banka")
    win.config(pady=45, padx=50, bg=LIGHT_BLUE)

    def pop(name):
        """Otvara novi prozor nakon odabira banke."""
        popup = Toplevel()
        popup.title(f"{name}")
        popup.config(pady=50, padx=50, bg=LIGHT_BLUE)

        amount = Label(popup, text="Unesite iznos: ", font=BFONT, bg=LIGHT_BLUE)
        amount.grid(row=0, column=0, columnspan=3)

        def ok_cancel():
            """Zapisuje unesene podatke, a ukoliko su polja prazna, vraća grešku."""
            if amount_entry.get() == "":
                messagebox.showwarning(title="Greška!", message="Polje ne može biti prazno!")
            elif amount_entry:
                with open("data.txt", "a") as data:
                    data.write(f"\n{name} | {amount_entry.get()}KM")
                win.destroy()

        ok = Button(popup, text="Potvrdi", command=ok_cancel, bg=DARK_BLUE, fg="white")
        ok.grid(row=5, column=0)
        cancel = Button(popup, text="Poništi", command=popup.destroy, bg=DARK_BLUE, fg="white")
        cancel.grid(row=5, column=2)

        def brojevi(t):
            global numbers
            numbers += str(t)
            am.set(numbers)

        # Unos podataka
        am = StringVar()
        amount_entry = Entry(popup,
                             relief=RIDGE,
                             bd=5,
                             textvariable=am,
                             bg=LIGHT_BLUE,
                             width=20,
                             font=BFONT)
        # amount_entry.focus()
        amount_entry.grid(row=1, column=0, columnspan=3, pady=5)
        # pin_entry = Entry(popup, width=30, show='*')
        # pin_entry.grid(row=1, column=0, columnspan=3, pady=5)
        NumBtn(popup, "1", 2, 0, lambda t=1: brojevi(t))
        NumBtn(popup, "2", 2, 1, lambda t=2: brojevi(t))
        NumBtn(popup, "3", 2, 2, lambda t=3: brojevi(t))
        NumBtn(popup, "4", 3, 0, lambda t=4: brojevi(t))
        NumBtn(popup, "5", 3, 1, lambda t=5: brojevi(t))
        NumBtn(popup, "6", 3, 2, lambda t=6: brojevi(t))
        NumBtn(popup, "7", 4, 0, lambda t=7: brojevi(t))
        NumBtn(popup, "8", 4, 1, lambda t=8: brojevi(t))
        NumBtn(popup, "9", 4, 2, lambda t=9: brojevi(t))
        NumBtn(popup, "0", 5, 1, lambda t=0: brojevi(t))
        popup.mainloop()

    # Izbor banke
    label = Label(text="Odaberite banku: ",
                  pady=20,
                  font=BFONT,
                  bg=LIGHT_BLUE,
                  fg="#41474D")
    label.grid(row=0, column=0, columnspan=2)

    Banka("UniCredit Bank", row=1, column=0, c=lambda name="UniCredit Bank": pop(name))
    Banka("Nova Banka", row=1, column=1, c=lambda name="Nova Banka": pop(name))
    Banka("Addiko Bank", row=2, column=0, c=lambda name="Addiko Bank": pop(name))
    Banka("Raiffeisen Bank", row=2, column=1, c=lambda name="Raiffeisen Bank": pop(name))
    Banka("MF Banka", row=3, column=0, c=lambda name="MF Banka": pop(name))
    Banka("NLB Banka", row=3, column=1, c=lambda name="NLB Banka": pop(name))
    win.mainloop()


if __name__ == "__main__":
    atm()
