import tkinter as tk
from tkinter import messagebox

class HotelBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel 'SEJUK ASRI'")
        
        # Ukuran font
        self.large_font = ("Arial", 13)
        self.padding = {'padx': 10, 'pady': 10}
        
        # Font widget dan label
        tk.Label(root, text="Hotel 'SEJUK ASRI'", font=self.large_font).grid(row=0, columnspan=2, **self.padding)
        tk.Label(root, text="Input Nama Petugas: ", font=self.large_font).grid(row=1, column=0, sticky='e', **self.padding)
        self.petugas_entry = tk.Entry(root, font=self.large_font)
        self.petugas_entry.grid(row=1, column=1, **self.padding)
        
        tk.Label(root, text="Input Nama Customer: ", font=self.large_font).grid(row=2, column=0, sticky='e', **self.padding)
        self.customer_entry = tk.Entry(root, font=self.large_font)
        self.customer_entry.grid(row=2, column=1, **self.padding)
        
        tk.Label(root, text="Input tanggal check-in: ", font=self.large_font).grid(row=3, column=0, sticky='e', **self.padding)
        self.checkin_entry = tk.Entry(root, font=self.large_font)
        self.checkin_entry.grid(row=3, column=1, **self.padding)
        
        tk.Label(root, text="Pilih Kode Kamar: ", font=self.large_font).grid(row=4, column=0, sticky='e', **self.padding)
        self.room_var = tk.StringVar(root)
        self.room_var.set("M")  # default value
        self.room_menu = tk.OptionMenu(root, self.room_var, "M", "S", "L", "A")
        self.room_menu.config(font=self.large_font)
        self.room_menu.grid(row=4, column=1, **self.padding)
        
        tk.Label(root, text="Input Lama Sewa: ", font=self.large_font).grid(row=5, column=0, sticky='e', **self.padding)
        self.lama_sewa_entry = tk.Entry(root, font=self.large_font)
        self.lama_sewa_entry.grid(row=5, column=1, **self.padding)
        
        # Membuat tombol untuk submit
        tk.Button(root, text="Submit", command=self.calculate, font=self.large_font).grid(row=6, columnspan=2, **self.padding)
        
        # Text widget untuk output
        self.output_text = tk.Text(root, width=70, height=20, font=self.large_font)
        self.output_text.grid(row=8, columnspan=2, **self.padding)
        
    def calculate(self):
        # Inputan
        nama_petugas = self.petugas_entry.get()
        nama_customer = self.customer_entry.get()
        tanggal_checkin = self.checkin_entry.get()
        kode_kamar = self.room_var.get().upper()
        lama_sewa = int(self.lama_sewa_entry.get())
        
        # Room data
        room_data = {
            'M': ("Melati", 650000),
            'S': ("Sakura", 550000),
            'L': ("Lily", 400000),
            'A': ("Anggrek", 350000)
        }
        
        if kode_kamar not in room_data:
            messagebox.showerror("Error", "Kode kamar tidak valid!")
            return
        
        nama_kamar, harga_per_malam = room_data[kode_kamar]
        jumlah_bayar = harga_per_malam * lama_sewa
        
        # Menghitung discount
        if lama_sewa > 5:
            discount = 0.10
        elif 3 <= lama_sewa <= 5:
            discount = 0.05
        else:
            discount = 0.0
            
        ppn = jumlah_bayar * discount
        total_bayar = jumlah_bayar - ppn

        # Menyimpan informasi total bayar untuk digunakan di jendela pembayaran
        self.total_bayar = total_bayar

        # Menampilkan jendela input pembayaran
        self.input_payment()

    def input_payment(self):
        # Membuat jendela baru untuk input pembayaran
        self.payment_window = tk.Toplevel(self.root)
        self.payment_window.title("Input Pembayaran")
        
        tk.Label(self.payment_window, text="Total Bayar: ", font=self.large_font).grid(row=0, column=0, sticky='e', **self.padding)
        tk.Label(self.payment_window, text=f"Rp. {self.total_bayar}", font=self.large_font).grid(row=0, column=1, **self.padding)
        
        tk.Label(self.payment_window, text="Input Pembayaran: ", font=self.large_font).grid(row=1, column=0, sticky='e', **self.padding)
        self.pembayaran_entry = tk.Entry(self.payment_window, font=self.large_font)
        self.pembayaran_entry.grid(row=1, column=1, **self.padding)
        
        tk.Button(self.payment_window, text="Submit", command=self.finalize_payment, font=self.large_font).grid(row=2, columnspan=2, **self.padding)
        
    def finalize_payment(self):
        pembayaran = float(self.pembayaran_entry.get())
        uang_kembali = pembayaran - self.total_bayar
        
        if uang_kembali < 0:
            messagebox.showerror("Error", "Pembayaran kurang dari total bayar!")
            return
        
        # Room data
        room_data = {
            'M': ("Melati", 650000),
            'S': ("Sakura", 550000),
            'L': ("Lily", 400000),
            'A': ("Anggrek", 350000)
        }
        
        nama_kamar, harga_per_malam = room_data[self.room_var.get()]
        lama_sewa = int(self.lama_sewa_entry.get())
        jumlah_bayar = harga_per_malam * lama_sewa
        discount = 0.10 if lama_sewa > 5 else 0.05 if 3 <= lama_sewa <= 5 else 0.0
        ppn = jumlah_bayar * discount
        total_bayar = jumlah_bayar - ppn
        
        # Menampilkan hasil output di widget
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, f"\t\t\t Bukti Pemesanan Kamar\n")
        self.output_text.insert(tk.END, f"\t\t\t   Hotel 'SEJUK ASRI'\n")
        self.output_text.insert(tk.END, f"===============================================================\n")
        self.output_text.insert(tk.END, f"Nama Petugas: {self.petugas_entry.get()}\t\t\t\t\tNama Customer: {self.customer_entry.get()}\n")
        self.output_text.insert(tk.END, f"\t\t\t\t\tTanggal Check-in: {self.checkin_entry.get()}\n")
        self.output_text.insert(tk.END, f"--------------------------------------------------------------------------------------------------------\n")
        self.output_text.insert(tk.END, f"Nama Kamar Yang di pesan: {nama_kamar}\n")
        self.output_text.insert(tk.END, f"Harga sewa permalam: Rp. {harga_per_malam}\n")
        self.output_text.insert(tk.END, f"Lama sewa: {lama_sewa} malam\n")
        self.output_text.insert(tk.END, f"PPN 10%: Rp. {ppn}\n")
        self.output_text.insert(tk.END, f"Jumlah Bayar: Rp. {jumlah_bayar}\n")
        self.output_text.insert(tk.END, f"Total Bayar (dipotong PPn): Rp. {total_bayar}\n")
        self.output_text.insert(tk.END, f"Pembayaran: Rp. {pembayaran}\n")
        self.output_text.insert(tk.END, f"Uang Kembali: Rp. {uang_kembali}\n")

        self.payment_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelBookingApp(root)
    root.mainloop()
