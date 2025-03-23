import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path

def pdf_to_images(pdf_path):
    output_folder = r".\output_images"
    os.makedirs(output_folder, exist_ok=True)

    try:
        poppler_path = r".\poppler-24.08.0\Library\bin"
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        for i, image in enumerate(images):
            image_path = os.path.join(output_folder, f"page_{i + 1}.png")
            image.save(image_path, 'PNG')

        messagebox.showinfo("Success", f"Images saved in the output_images folder")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process PDF: {e}")

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_to_images(file_path)

# GUI Setup
root = tk.Tk()
root.title("PDF to Images Converter")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Select a PDF file to convert:")
label.pack()

button = tk.Button(frame, text="Browse PDF", command=select_pdf)
button.pack(pady=10)

root.mainloop()
