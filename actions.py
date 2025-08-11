import tkinter as tk
import webbrowser
from tkinter import messagebox
import variablen as var
import storage

class Actions:
    def __init__(self, root, link_list):
        self.root = root
        self.link_list = link_list

    def open(self):
        try:
            selected_name = self.link_list.get("anchor")
            index = var.saved_links_name.index(selected_name)
            webbrowser.open(var.saved_links[index])
        except Exception:
            if selected_name == '':
                MsgBox = messagebox.showinfo('Keine URLS Hinzugefügt', "Sie haben noch keine URLS Hinzugefügt")
            pass

    def add(self):
        add_bg = tk.Label(self.root, width=150, height=120)
        add_bg.place(x=0, y=0)

        tk.Label(add_bg, text="Name: ", font=("Default", 15)).place(x=20, y=20)
        add_name = tk.Entry(self.root, width=35, font=("Default", 15), bg="lightgrey")
        add_name.place(x=90, y=25)

        tk.Label(add_bg, text="URL: ", font=("Default", 15)).place(x=20, y=80)
        add_url = tk.Entry(self.root, width=35, font=("Default", 15), bg="lightgrey")
        add_url.place(x=90, y=83.5)

        def done():
            name = add_name.get().strip()
            url = add_url.get().strip()
            if name and url:
                var.saved_links_name.append(name)
                var.saved_links.append(url)
                self.link_list.insert(tk.END, name)
                storage.save()
                cleanup()
            else:
                messagebox.showwarning("Warnung", "Bitte Name und URL eingeben!")

        def cancel():
            cleanup()

        def cleanup():
            add_bg.destroy()
            add_name.destroy()
            add_url.destroy()
            done_button.destroy()
            cancel_button.destroy()

        done_button = tk.Button(self.root, text="Done", font=("Default", 12), width=50, bg="#F6694F", command=done)
        done_button.place(x=20, y=130)

        cancel_button = tk.Button(self.root, text="Cancel", font=("Default", 12), width=50, bg="red", command=cancel)
        cancel_button.place(x=20, y=180)

    def delete(self):
        try:
            selected_name = self.link_list.get("anchor")
            index = var.saved_links_name.index(selected_name)
            var.saved_links_name.pop(index)
            var.saved_links.pop(index)
            self.link_list.delete(index)
            storage.save()
        except Exception:
            if selected_name == '':
                MsgBox = messagebox.showinfo('Keine URLS Hinzugefügt', "Sie haben noch keine URLS Hinzugefügt")
            pass

    def delete_all(self):
        selected_name = self.link_list.get("anchor")
        if selected_name != "":
            MsgBox = messagebox.askquestion('Delete All', 'Bist du dir sicher?')
            if MsgBox == 'yes':
                var.saved_links_name.clear()
                var.saved_links.clear()
                self.link_list.delete(0, tk.END)
                storage.save()
        else:
            if selected_name == "":
                MsgBox = messagebox.showinfo('Keine URLS Hinzugefügt', "Sie haben noch keine URLS Hinzugefügt")

    def edit(self):
        try:
            selected_name = self.link_list.get("anchor")
            index = var.saved_links_name.index(selected_name)
        except Exception:
            return  # No selection or error

        edit_bg = tk.Label(self.root, width=150, height=120)
        edit_bg.place(x=0, y=0)

        tk.Label(edit_bg, text="Name: ", font=("Default", 15)).place(x=20, y=20)
        edit_name = tk.Entry(self.root, width=35, font=("Default", 15), bg="lightgrey")
        edit_name.insert(0, var.saved_links_name[index])
        edit_name.place(x=90, y=25)

        tk.Label(edit_bg, text="URL: ", font=("Default", 15)).place(x=20, y=80)
        edit_url = tk.Entry(self.root, width=35, font=("Default", 15), bg="lightgrey")
        edit_url.insert(0, var.saved_links[index])
        edit_url.place(x=90, y=83.5)

        def done():
            new_name = edit_name.get().strip()
            new_url = edit_url.get().strip()
            if new_name and new_url:
                var.saved_links_name[index] = new_name
                var.saved_links[index] = new_url

                self.link_list.delete(index)
                self.link_list.insert(index, new_name)

                cleanup()
                storage.save()
            else:
                messagebox.showwarning("Warnung", "Bitte Name und URL eingeben!")

        def cancel():
            cleanup()

        def cleanup():
            edit_bg.destroy()
            edit_name.destroy()
            edit_url.destroy()
            done_button.destroy()
            cancel_button.destroy()

        done_button = tk.Button(self.root, text="Done", font=("Default", 12), width=50, bg="#F6694F", command=done)
        done_button.place(x=20, y=130)

        cancel_button = tk.Button(self.root, text="Cancel", font=("Default", 12), width=50, bg="red", command=cancel)
        cancel_button.place(x=20, y=180)

    def credit(self):
        credit_bg = tk.Label(self.root, width=150, height=120)
        credit_bg.place(x=0, y=0)

        tk.Label(credit_bg, text="Programmiert von Soufian El", font=("Default", 28)).place(x=0, y=0)

        def back():
            credit_bg.destroy()
            back_button.destroy()

        back_button = tk.Button(self.root, text="Back", font=("Default", 12), width=50, bg="red", command=back)
        back_button.place(x=20, y=450)
