import tkinter as tk


class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x400+300+100")
        self.title("Calculator")
        self.UIinit()

    def UIinit(self):

        # creating an entry frame and placing an entry box into it
        entry_frame = tk.Frame(self,bg='#e1e3e6')
        entry_value = tk.StringVar()
        entry = tk.Entry(entry_frame,textvar=entry_value,font="Verdana 20")
        entry.grid(row=0,column=0, sticky='nsew',padx=3,pady=3)

        def click(event):
            text = event.widget.cget('text')
            if text == "=":
                if entry_value.get().isdigit():
                    value = int(entry_value.get())
                else:
                    value = eval(entry.get())
                entry_value.set(value)
                entry.update()
            elif text == "c":
                entry_value.set("")
            else:
                entry_value.set(entry_value.get() + text)
                entry.update()

        button_frame = tk.Frame(self,bg='white')

        button_9 = tk.Button(button_frame,text='9',font='Verdana 20')
        button_9.grid(row=0,column=0,sticky='nsew')
        button_9.bind("<Button-1>",click)

        button_8 = tk.Button(button_frame,text='8',font='Verdana 20')
        button_8.grid(row=0,column=1,sticky='nsew')
        button_8.bind("<Button-1>",click)

        button_7 = tk.Button(button_frame,text='7',font='Verdana 20')
        button_7.grid(row=0,column=2,sticky='nsew')
        button_7.bind("<Button-1>",click)

        button_plus = tk.Button(button_frame,text='+',font='Verdana 20')
        button_plus.grid(row=0,column=3,sticky='nsew')
        button_plus.bind("<Button-1>",click)

        button_6 = tk.Button(button_frame,text='6',font='Verdana 20')
        button_6.grid(row=1,column=0,sticky='nsew')
        button_6.bind("<Button-1>",click)

        button_5 = tk.Button(button_frame,text='5',font='Verdana 20')
        button_5.grid(row=1,column=1,sticky='nsew')
        button_5.bind("<Button-1>",click)

        button_4 = tk.Button(button_frame,text='4',font='Verdana 20')
        button_4.grid(row=1,column=2,sticky='nsew')
        button_4.bind("<Button-1>",click)

        button_minus = tk.Button(button_frame,text='-',font='Verdana 20')
        button_minus.grid(row=1,column=3,sticky='nsew')
        button_minus.bind("<Button-1>",click)

        button_3 = tk.Button(button_frame,text='3',font='Verdana 20')
        button_3.grid(row=2,column=0,sticky='nsew')
        button_3.bind("<Button-1>",click)

        button_2 = tk.Button(button_frame,text='2',font='Verdana 20')
        button_2.grid(row=2,column=1,sticky='nsew')
        button_2.bind("<Button-1>",click)

        button_1 = tk.Button(button_frame,text='1',font='Verdana 20')
        button_1.grid(row=2,column=2,sticky='nsew')
        button_1.bind("<Button-1>",click)

        button_multiply = tk.Button(button_frame,text='*',font='Verdana 20')
        button_multiply.grid(row=2,column=3,sticky='nsew')
        button_multiply.bind("<Button-1>",click)

        button_ok = tk.Button(button_frame,text='ok',font='Verdana 20')
        button_ok.grid(row=3,column=0,sticky='nsew')
        button_ok.bind("<Button-1>",click)

        button_0 = tk.Button(button_frame,text='0',font='Verdana 20')
        button_0.grid(row=3,column=1,sticky='nsew')
        button_0.bind("<Button-1>",click)

        button_dot = tk.Button(button_frame,text='.',font='Verdana 20')
        button_dot.grid(row=3,column=2,sticky='nsew')
        button_dot.bind("<Button-1>",click)

        button_equal = tk.Button(button_frame,text='=',font='Verdana 20')
        button_equal.grid(row=3,column=3,sticky='nsew')
        button_equal.bind("<Button-1>",click)

        button_frame.grid_columnconfigure(0,weight=1)
        button_frame.grid_columnconfigure(1,weight=1)
        button_frame.grid_columnconfigure(2,weight=1)
        button_frame.grid_columnconfigure(3,weight=1)

        button_frame.grid_rowconfigure(0,weight=1)
        button_frame.grid_rowconfigure(1,weight=1)
        button_frame.grid_rowconfigure(2,weight=1)
        button_frame.grid_rowconfigure(3,weight=1)

        entry_frame.grid_columnconfigure(0,weight=1)
        entry_frame.pack(fill='x',padx=3,pady=3)
        button_frame.pack(fill='both',expand=True)


if __name__ == '__main__':
    root = app()
    root.mainloop()