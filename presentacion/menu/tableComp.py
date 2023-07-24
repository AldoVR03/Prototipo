import tkinter as tk
from tkinter import ttk

custom_font=("Unispace", 12)
class TableComp():
     def __init__(self,root, data) -> None:
          
          self.container=tk.Frame(root)
          self.style=ttk.Style()
          self.style.configure("Custom.Treeview.Heading", font=custom_font, background="brown")
          self.style.configure("Custom.Treeview", font=custom_font)
          self.headers=["NOMBRE", "LIDER", "CAPACIDAD"]
          self.tree = ttk.Treeview(self.container, columns=self.headers, show="headings",style="Custom.Treeview")
          self.data=data
          for header in self.headers:
              self.tree.heading(header, text=header)
              self.tree.column(header, width=140,anchor="center")
              self.tree.heading(header, text=header, command=lambda c=header: self.sort_column(self.tree, c, False))

          self.tree.configure(height=13)
     
     def start(self):     
         for row_data in self.data:
              self.tree.insert("", "end", values=row_data)
     def show(self):
         self.container.pack()
         self.tree.pack(fill="both", expand=True)



     def sort_column(self,tree, col, reverse):
          data = [(self.tree.set(child, col), child) for child in self.tree.get_children("")]
          data.sort(reverse=reverse)

          for index, item in enumerate(data):
              self.tree.move(item[1], "", index)

          tree.heading(col, command=lambda: self.sort_column(tree, col, not reverse))
    

# root = tk.Tk()
# root.title("Treeview con 3 columnas")
# FRAME2=tk.Frame(root)
# headers = ["NOMBRE", "LIDER", "CAPACIDAD"]

data = [("CLAN1","LIDER1",10,22),
        ("CLAN2","LIDER1",10),
        ("CLAN3","LIDER1",10),
        ("CLAN4","LIDER1",10),
        ("CLAN5","LIDER1",10),
        ("CLAN6","LIDER1",10),
        ("CLAN7","LIDER1",10),
        ("CLAN8","LIDER1",10),
        ("CLAN9","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10),
        ("CLAN1","LIDER1",10)]
        
# tree=ClanListView(FRAME2,data)
# tree.start()
# tree.show()
# FRAME2.pack()

# root.mainloop()