import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import importlib

MODULI = {
    "torch": "torch",
    "transformers": "transformers",
    "pillow": "pillow",
    "pdf2image": "pdf2image",
    "beautifulsoup4": "bs4",
    "requests": "requests",
    "opencv-python": "cv2",
    "streamlit": "streamlit",
    "numpy": "numpy"
}

def proveri_i_instaliraj():
    report_box.delete('1.0', tk.END)
    neuspesne = []

    for prikaz, interni_naziv in MODULI.items():
        try:
            importlib.import_module(interni_naziv)
            report_box.insert(tk.END, f"✅ {prikaz} je već instaliran\n")
        except ImportError:
            report_box.insert(tk.END, f"➕ Instaliram: {prikaz}...\n")
            try:
                subprocess.check_call(["pip", "install", prikaz])
                report_box.insert(tk.END, f"✅ {prikaz} uspešno instaliran\n")
            except Exception as e:
                report_box.insert(tk.END, f"❌ Greška pri instalaciji {prikaz}: {e}\n")
                neuspesne.append(prikaz)

    if neuspesne:
        msg = "⚠️ Neke biblioteke nisu mogle da se instaliraju:\n" + ", ".join(neuspesne)
        messagebox.showwarning("Instalacija završena", msg)
    else:
        messagebox.showinfo("Završeno", "✅ Provera i instalacija su uspešno završene.")

# === GUI interfejs ===
root = tk.Tk()
root.title("🔧 Instalacija Python biblioteka")
root.geometry("580x460")
root.resizable(False, False)

tk.Label(root, text="📦 Provera i instalacija potrebnih modula", font=("Helvetica", 14, "bold")).pack(pady=10)
tk.Button(root, text="Pokreni proveru i instalaciju", command=proveri_i_instaliraj, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=12, pady=6).pack()

report_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Consolas", 10))
report_box.pack(padx=10, pady=15)

root.mainloop()