import sqlite3
import tkinter as tk

def prediksi():
    nama = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())

    prodi = ""
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prodi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prodi = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prodi = "Bahasa"

    label_hasil.config(text=f"Hasil Prediksi untuk {nama}: {prodi}")

    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        prediksi_fakultas TEXT
                    )''')

    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
                      VALUES (?, ?, ?, ?, ?)''', (nama, nilai_biologi, nilai_fisika, nilai_inggris, prodi))
    
    conn.commit()
    conn.close()

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

label_judul = tk.Label(root, text="Aplikasi prediksi Prodi Pilihan")
label_judul.pack()

label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

button_prediksi = tk.Button(root, text="Hasil Prediksi", command=prediksi)
button_prediksi.pack()

label_hasil = tk.Label(root, text="")
label_hasil.pack()

root.mainloop()