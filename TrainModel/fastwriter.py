import os
import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class App:
    def __init__(self, root, files):
        self.files = files
        self.index = 0
        self.data = {}
        self.root = root
        self.root.title("Data Marker")

        self.text = tk.Text(root, state='disabled')
        self.text.pack(fill=tk.BOTH, expand=True)

        self.is_recipe_var = tk.StringVar()
        self.is_continuous_var = tk.StringVar()
        self.many_recipes_var = tk.StringVar()

        self.is_recipe_entry = tk.Entry(root, textvariable=self.is_recipe_var)
        self.is_recipe_entry.pack()
        self.is_recipe_entry.bind('<KeyRelease>', self.check_and_move_focus)

        self.is_continuous_entry = tk.Entry(root, textvariable=self.is_continuous_var)
        self.is_continuous_entry.pack()
        self.is_continuous_entry.bind('<KeyRelease>', self.check_and_move_focus)

        self.many_recipes_entry = tk.Entry(root, textvariable=self.many_recipes_var)
        self.many_recipes_entry.pack()
        self.many_recipes_entry.bind('<KeyRelease>', self.check_and_move_focus)

        self.next_button = tk.Button(root, text="Next", command=self.next_file)
        self.next_button.pack()

        self.prev_button = tk.Button(root, text="Previous", command=self.prev_file)
        self.prev_button.pack()

        self.root.bind('<Up>', lambda event: self.prev_file())
        self.root.bind('<Down>', lambda event: self.next_file())

        self.csv_file = open('output.csv', 'w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['filename', 'is_recipe', 'is_continuous', 'many_recipes'])
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.load_file()

    def load_file(self):
        filename = self.files[self.index]
        file_number = os.path.splitext(os.path.basename(filename))[0].rsplit('_', 1)[-1]
        with open(filename, 'r') as file:
            content = file.read()
        self.text.config(state='normal')
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, f"File Number: {file_number}\n\n{content}")
        self.text.config(state='disabled')

        data = self.data.get(filename, ["", "", ""])
        self.is_recipe_var.set(data[0])
        self.is_continuous_var.set(data[1])
        self.many_recipes_var.set(data[2])

        self.is_recipe_entry.focus_set()

    def save_data(self):
        filename = self.files[self.index]
        book_name = os.path.splitext(os.path.basename(filename))[0]
        data = [self.is_recipe_var.get(), self.is_continuous_var.get(), self.many_recipes_var.get()]
        self.data[book_name] = data

    def next_file(self):
        self.save_data()
        if self.index < len(self.files) - 1:
            self.index += 1
            self.load_file()
        else:
            messagebox.showinfo("Information", "This is the last file.")

    def prev_file(self):
        self.save_data()
        if self.index > 0:
            self.index -= 1
            self.load_file()
        else:
            messagebox.showinfo("Information", "This is the first file.")

    def check_and_move_focus(self, event):
        widget = event.widget
        if len(widget.get()) == 1:
            if widget == self.is_recipe_entry:
                self.is_continuous_entry.focus_set()
            elif widget == self.is_continuous_entry:
                self.many_recipes_entry.focus_set()
            elif widget == self.many_recipes_entry:
                self.next_button.focus_set()
    def on_close(self):
        with open('output.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for book_name, data in self.data.items():
                csv_writer.writerow([book_name] + data)
        self.root.destroy()
        
    def __del__(self):
        self.csv_file.close()

def main():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    directory = filedialog.askdirectory()
    files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]
    files.sort(key=lambda f: int(os.path.splitext(os.path.basename(f))[0].rsplit('_', 1)[-1]))
    app = App(root, files)
    root.mainloop()

if __name__ == "__main__":
    main()