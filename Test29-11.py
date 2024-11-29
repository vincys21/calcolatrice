import tkinter as tk
window=tk.Tk()
window.title("Finestra di provass")
window.geometry("1920x1080")
window.resizable(False, False)
window.configure(background="#293133")

etichetta=tk.Label(window, text="RONALDO", fg="#BEBD7F",background="#293133", font=("Helvatica",20))
etichetta.grid(row=1,column=2,sticky="w",padx=6,pady=0)
def stampa_etichetta():
    text = "SIUUUUUUUUUUUM"
    text_output = tk.Label(window, text=text, fg="#008080", font=("Helvatica",16))

    text_output.grid(row=1, column=1,sticky="w")

first_button=tk.Button(text="Clicca qui!",command=stampa_etichetta) #QUESTO È UN BOTTONE
first_button.grid(row=6,column=0,sticky="w")

input_text = tk.Entry(window)
input_text.grid(row=2,column=0,sticky="w")

# FUNZIONE PER STAMPARE UN'ETICHETTA CON INPUT
def stampa_etichetta_input():
    testo= input_text.get()
    text_output1=tk.Label(window,text=testo, fg="#FF0000",font=("Helvatica",16))
    text_output1.grid(row=3, column=0, sticky="w")

#CREAZIOE DEL CAMPO DI INPUT
input_text= tk.Entry(window)
input_text.grid(row=2,column=0,sticky="w")

#CREAZIONE DEL SECONDO BOTTONE
second_button=tk.Button(text="Clicca anche qui!",command=stampa_etichetta) #QUESTO È UN BOTTONE
second_button.grid(row=5,column=0,sticky="w")

# METTIAMO QUI IL WINDSET  

if __name__ == "__main__":
    window.mainloop()