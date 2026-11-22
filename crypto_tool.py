import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันเข้ารหัสข้อความ
def encrypt_text():
    msg = entry_msg.get("1.0", tk.END).strip()
    key_str = entry_key.get().strip()
    
    if not msg:
        messagebox.showwarning("Warning", "Please enter a message!")
        return
    try:
        key = int(key_str)
        encrypted = "".join([chr((ord(char) + key) % 1114112) for char in msg])
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, encrypted)
    except ValueError:
        messagebox.showerror("Error", "Secret Key must be a number!")

# ฟังก์ชันถอดรหัสข้อความ
def decrypt_text():
    cipher = entry_msg.get("1.0", tk.END).strip()
    key_str = entry_key.get().strip()
    
    if not cipher:
        messagebox.showwarning("Warning", "Please enter an encrypted message!")
        return
    try:
        key = int(key_str)
        decrypted = "".join([chr((ord(char) - key) % 1114112) for char in cipher])
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, decrypted)
    except ValueError:
        messagebox.showerror("Error", "Secret Key must be a number!")

# ฟังก์ชันบันทึกผลลัพธ์ลงไฟล์ .txt
def save_to_file():
    output = entry_result.get("1.0", tk.END).strip()
    if not output:
        messagebox.showwarning("Warning", "No output to save!")
        return
    with open("secret_output.txt", "w", encoding="utf-8") as file:
        file.write(output)
    messagebox.showinfo("Saved", "Saved successfully to 'secret_output.txt'!")

# ตั้งค่าหน้าต่างหลัก (GUI)
root = tk.Tk()
root.title("Cyber Cryptography Tool - By Nannapat")
root.geometry("450x420")
root.configure(bg="#1e1e2e")

tk.Label(root, text="TEXT ENCRYPTION & DECRYPTION TOOL", font=("Arial", 12, "bold"), bg="#1e1e2e", fg="#89b4fa").pack(pady=10)

tk.Label(root, text="Enter Message / Ciphertext:", bg="#1e1e2e", fg="white").pack(anchor="w", padx=25)
entry_msg = tk.Text(root, height=4, width=48)
entry_msg.pack(pady=5)

tk.Label(root, text="Enter Numeric Secret Key (e.g., 7):", bg="#1e1e2e", fg="white").pack(anchor="w", padx=25)
entry_key = tk.Entry(root, width=20)
entry_key.pack(anchor="w", padx=25, pady=5)

frame_btn = tk.Frame(root, bg="#1e1e2e")
frame_btn.pack(pady=10)
tk.Button(frame_btn, text="Encrypt", width=12, bg="#a6e3a1", command=encrypt_text).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Decrypt", width=12, bg="#f9e2af", command=decrypt_text).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Save .txt", width=12, bg="#89dceb", command=save_to_file).grid(row=0, column=2, padx=5)

tk.Label(root, text="Output Result:", bg="#1e1e2e", fg="white").pack(anchor="w", padx=25)
entry_result = tk.Text(root, height=4, width=48)
entry_result.pack(pady=5)

root.mainloop()
