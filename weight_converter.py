from tkinter import Tk, StringVar, Label, OptionMenu, Entry, Button

class GUI:
    """
    The main project class. It will have pretty much everything needed in the program
    """

    def __init__(self, master:Tk) -> None:
        """
        Creates the widgets inside the master Tk
        """
        self.createwidgets(master)

    def createwidgets(self, master:Tk) -> None:
        """
        Creates the widgets
        """

        def _convert(conversionlabel:Label, value:int, right:str, left:str) -> None:
            """
            Converts the units by assigning them the ratio to kg and using that to find the ratio between themselves
            """
            #The value is always to be multiplied by
            conversiontable = {'Pounds':2.20462, 'Kg':1, 'Ton':0.00110231}
            result = value * conversiontable[right] / conversiontable[left]
            conversionlabel.configure(text=f"{result}")
            
        choices = ['Pounds', 'Kg', 'Ton']

        variabler = StringVar(master)
        variabler.set('Pounds')
        selectionr = OptionMenu(master, variabler, *choices)
        selectionr.grid(row=0, column=0)

        variablel = StringVar(master)
        variablel.set('Pounds')
        selectionl = OptionMenu(master, variablel, *choices)
        selectionl.grid(row=0, column=1)

        entryright = Entry(master)
        entryright.grid(row=1, column=0, columnspan=2)

        conversionlabel = Label(master)
        conversionlabel.grid(row=2,columnspan=2)

        conversionbutton = Button(master, text='Convert!',command=lambda:_convert(conversionlabel, int(entryright.get()), variabler.get(), variablel.get()))
        conversionbutton.grid(row=3,columnspan=2)


if __name__ == '__main__':
    root = Tk()
    GUI(root)
    root.mainloop()