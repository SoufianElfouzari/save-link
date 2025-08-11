import tkinter as tk
import variablen as var
import actions
import storage

def setup_gui():
    root = tk.Tk()
    root.title("Save - Links")
    root.geometry("500x500")
    root.resizable(False, False)

    root.iconbitmap("resources/Icon.ico")

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.LEFT, fill=tk.Y)

    link_list = tk.Listbox(root, yscrollcommand=scrollbar.set, width=50, height=30)
    link_list.place(x=20)

    scrollbar.config(command=link_list.yview)

    act = actions.Actions(root, link_list)

    open_button = tk.Button(root, text="open", font=("Default", 10), width=10, bg="lightgreen", command=act.open, relief='solid')
    open_button.place(x=370, y=20)

    add_button = tk.Button(root, text="add", font=("Default", 10), width=10, bg="lightblue", command=act.add, relief='solid')
    add_button.place(x=370, y=80)

    delete_button = tk.Button(root, text="delete", font=("Default", 10), width=10, bg="#FF4F63", command=act.delete, relief='solid')
    delete_button.place(x=370, y=140)

    delete_all_button = tk.Button(root, text="delete all", font=("Default", 10), width=10, bg="#D31815", command=act.delete_all, relief='solid')
    delete_all_button.place(x=370, y=200)

    edit_button = tk.Button(root, text="edit", font=("Default", 10), width=10, bg="#D1BA47", command=act.edit, relief='solid')
    edit_button.place(x=370, y=260)

    # Lade gespeicherte Links in die Listbox
    storage.load()
    for name in var.saved_links_name:
        link_list.insert(tk.END, name)

    return root
