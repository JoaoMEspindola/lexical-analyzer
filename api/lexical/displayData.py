import pandas as pd
import tkinter as tk
from tkinter import ttk

def displayResult(lista_tokens, tabela_simbolos):
    tabela_tokens = pd.DataFrame({'Token': lista_tokens})
    tabela_tokens.insert(0, 'Número', range(1, len(tabela_tokens) + 1))

    tabela_simbolos_formatada = pd.DataFrame(list(tabela_simbolos.items()), columns=['Símbolo', 'Valor'])

    root = tk.Tk()
    root.title("Resultado")

    frame_tokens = ttk.Frame(root, width=400, height=300)
    frame_tokens.pack(padx=10, pady=10, fill='both', expand=True)

    ttk.Label(frame_tokens, text="Lista de tokens").pack()

    tree_tokens = ttk.Treeview(frame_tokens)
    tree_tokens['columns'] = ('Número', 'Token')
    tree_tokens.heading('#0', text='', anchor='w')
    tree_tokens.heading('Número', text='Número')
    tree_tokens.heading('Token', text='Token')

    for index, row in tabela_tokens.iterrows():
        tree_tokens.insert('', 'end', text='', values=(row['Número'], row['Token']))

    tree_tokens.pack(fill='both', expand=True)

    frame_simbolos = ttk.Frame(root, width=400, height=300)
    frame_simbolos.pack(padx=10, pady=10, fill='both', expand=True)

    ttk.Label(frame_simbolos, text="Tabela de Símbolos").pack()

    tree_simbolos = ttk.Treeview(frame_simbolos)
    tree_simbolos['columns'] = ('Símbolo', 'Valor')
    tree_simbolos.heading('#0', text='', anchor='w')
    tree_simbolos.heading('Símbolo', text='Símbolo')
    tree_simbolos.heading('Valor', text='Valor')

    for index, row in tabela_simbolos_formatada.iterrows():
        tree_simbolos.insert('', 'end', text='', values=(row['Símbolo'], row['Valor']))

    tree_simbolos.pack(fill='both', expand=True)
    root.mainloop()