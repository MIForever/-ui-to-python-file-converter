import os
import tkinter as tk

class Converter:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("400x450+451+99")
        try:    
            self.root.iconbitmap('icon.ico')
        except:
            pass
        self.root.minsize(400, 450)
        self.root.maxsize(1370, 750)
        self.root.resizable(True,True)
        self.root.title(".ui to python file converter")
        self.root.configure(bg="#727272")

        self.pyqt_version_label = tk.Label(self.root,text='Select your PyQt version',bg="#727272",fg="white")
        self.pyqt_version_label.place(rely=0.165,relx=0.05,width=140)

        self.options = ['PyQt4','PyQt5']
        self.clicked = tk.StringVar()
        self.clicked.set(self.options[1])

        self.drop = tk.OptionMenu(self.root,self.clicked,*self.options)
        self.drop.place(relx=0.5, rely=0.16, height=25, relwidth=0.20) 

        self.py_path_entry = tk.Entry(self.root)
        self.py_path_entry.place(relx=0.3, rely=0.489, height=20, relwidth=0.65)
        self.py_path_entry.configure(bg="white",font="-family {Sergeo UI} -size 10 -weight bold",
            fg="#000000",insertbackground="black",selectbackground="blue",selectforeground="white")

        self.ui_path_entry = tk.Entry(self.root)
        self.ui_path_entry.place(relx=0.3, rely=0.289, height=20, relwidth=0.65)
        self.ui_path_entry.configure(bg="white",font="-family {Sergeo UI} -size 10 -weight bold",
            fg="#000000",insertbackground="black",selectbackground="blue",selectforeground="white")

        self.convert_btn = tk.Button(self.root,command=self.convert)
        self.convert_btn.place(relx=0.4, rely=0.756, height=30, relwidth=0.2)
        self.convert_btn.configure(bg="#888888",borderwidth="1",fg="#000000",pady="0",text="Convert")

        self.py_txt_lbl = tk.Label(self.root)
        self.py_txt_lbl.place(relx=0.05, rely=0.289, height=21, width=93)
        self.py_txt_lbl.configure(bg="#727272",fg="white",text="Path of .ui file")

        self.ui_txt_lbl = tk.Label(self.root)
        self.ui_txt_lbl.place(relx=0.04, rely=0.489, height=21, width=100)
        self.ui_txt_lbl.configure(bg="#727272",fg="white",text="Path to python file")

        self.info_label = tk.Label(self.root)
        self.info_label.place(relx=0.0, rely=0.867, relheight=60/450, relwidth=1)
        self.info_label.configure(bg="#727272",font="-family {Segoe UI} -size 11 -weight bold")

        self.program_name_lbl = tk.Label(self.root)
        self.program_name_lbl.place(relx=0.0, rely=0.0, relheight=0.11, relwidth=1)
        self.program_name_lbl.configure(bg="#727272",fg="#000000",text=".ui to .py converter",font="-family {Sergeo UI} -size 20 -weight bold")
    
    def run(self):
        self.root.mainloop()

    def convert(self):
        ui_path = self.ui_path_entry.get()
        py_path = self.py_path_entry.get()
        pyqt_version = self.clicked.get()[-1]
        if  py_path!='' and ui_path!='':
            if os.path.exists(ui_path):
                if py_path.endswith(".py") or py_path.endswith(".pyw"):
                    os.system(f'pyuic{pyqt_version} -x {ui_path} -o {py_path}')
                    self.info_label.configure(text='Converting completed successfully',foreground='green')
                else:
                    self.info_label.configure(text='Wrong name for python file!',foreground='red')
            else:
                self.info_label.configure(text='Wrong path for ui file!',foreground='red')
        else:
            self.info_label.configure(text='Entry is empty!',foreground='red')




if __name__ == '__main__':
    converter = Converter()
    converter.run()

