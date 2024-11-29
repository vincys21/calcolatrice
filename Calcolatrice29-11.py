import tkinter as tk
window=tk.Tk()
window.title("Finestra di provass")
window.geometry("1920x1080")
window.resizable(False, False)
window.configure(background="#293133")

Esercizio=tk.Label(window, text="Calcolatrice Semplice", fg="#BEBD7F",background="#293133", font=("Helvatica",20))
Esercizio.grid(row=0,column=5,sticky="w",padx=0,pady=0)

def Operazione():
    Risultato = "Il risultato è:"
    Risultato_output = tk.Label(window, text=Risultato, fg="#008080", font=("Helvatica",16))
    Risultato_output.grid(row=1, column=5,sticky="w")

def Addizione():
    pass

def Sottrazione():
    pass

def Moltiplicazione():
    pass

def Divisione():
    pass


num1=tk.Entry(window)
num1.grid(row=3,column=4,sticky="w")

num2=tk.Entry(window)
num2.grid(row=3,column=6,sticky="w")

somma=tk.Button(window,text="+",command=Addizione)
somma.grid(row=3,column=5,sticky="w")

sottrazione=tk.Button(window,text="-",command=Sottrazione)
sottrazione.grid(row=4,column=5,sticky="w")

moltiplicazione=tk.Button(window,text="*",command=Moltiplicazione)
moltiplicazione.grid(row=5,column=5,sticky="w")

divisione=tk.Button(window,text="/",command=Divisione)
divisione.grid(row=6,column=5,sticky="w")



# Bottone_Addizione=tk.Button(window, text="+")
# Bottone_Addizione.grid(row=6,column=0,sticky="w")




if __name__ == "__main__":
    window.mainloop()