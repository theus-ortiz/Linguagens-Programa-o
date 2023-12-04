import customtkinter
import sqlite3
from tkinter import ttk

def criar_tabela():
    connection = sqlite3.connect("imc_database.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            endereco TEXT,
            altura REAL,
            peso REAL,
            imc REAL
        )
    ''')

    connection.commit()
    connection.close()

def inserir_dados_no_banco(nome, endereco, altura, peso, imc):
    connection = sqlite3.connect("imc_database.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO pacientes (nome, endereco, altura, peso, imc)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, endereco, altura, peso, imc))

    connection.commit()
    connection.close()

def exibir_dados_salvos():
    connection = sqlite3.connect("imc_database.db")
    cursor = connection.cursor()

    cursor.execute('''
        SELECT nome, endereco, altura, peso, imc FROM pacientes
    ''')

    dados_salvos = cursor.fetchall()
    connection.close()

    return dados_salvos

def criar_aba_dados_salvos():
    for widget in aba_dados_salvos.winfo_children():
        widget.destroy()

    dados_salvos = exibir_dados_salvos()
    for i, dado in enumerate(dados_salvos):
        customtkinter.CTkLabel(master=aba_dados_salvos, text=f"Dado {i + 1}").grid(row=i, column=0, padx=10, pady=5)
        for j, valor in enumerate(dado):
            customtkinter.CTkLabel(master=aba_dados_salvos, text=valor).grid(row=i, column=j + 1, padx=10, pady=5)

def calcular_imc():
    try:
        nome = entry_nome.get()
        endereco = entry_endereco.get()
        altura = float(entry_altura.get()) / 100
        peso = float(entry_peso.get())
        imc = peso / (altura ** 2)

        inserir_dados_no_banco(nome, endereco, altura, peso, imc)

        resultado_imc.set(f"IMC: {imc:.2f}")

        criar_aba_dados_salvos()

    except ValueError:
        resultado_imc.set("Preencha peso e altura corretamente.")

def reiniciar():
    entry_nome.delete(0, 'end')
    entry_endereco.delete(0, 'end')
    entry_altura.delete(0, 'end')
    entry_peso.delete(0, 'end')
    resultado_imc.set("IMC: ")

criar_tabela()

root = customtkinter.CTk()
root.geometry("700x500")
root.title("Cálculo de IMC")

notebook = ttk.Notebook(root)
notebook.pack(pady=20, padx=60, fill="both", expand=True)

frame = customtkinter.CTkFrame(master=root)
notebook.add(frame, text="Cálculo de IMC")

customtkinter.CTkLabel(master=frame, text="Nome do Paciente").pack(pady=5, padx=10)
entry_nome = customtkinter.CTkEntry(master=frame)
entry_nome.pack(pady=5, padx=10)

customtkinter.CTkLabel(master=frame, text="Endereço Completo").pack(pady=5, padx=10)
entry_endereco = customtkinter.CTkEntry(master=frame)
entry_endereco.pack(pady=5, padx=10)

customtkinter.CTkLabel(master=frame, text="Altura (Cm)").pack(pady=5, padx=10)
entry_altura = customtkinter.CTkEntry(master=frame)
entry_altura.pack(pady=5, padx=10)

customtkinter.CTkLabel(master=frame, text="Peso (kg)").pack(pady=5, padx=10)
entry_peso = customtkinter.CTkEntry(master=frame)
entry_peso.pack(pady=5, padx=10)

resultado_imc = customtkinter.StringVar()
resultado_imc.set("IMC: ")
customtkinter.CTkLabel(master=frame, text="IMC: ",  textvariable=resultado_imc).pack(pady=1, padx=1)

customtkinter.CTkButton(master=frame, text="Calcular", command=calcular_imc).pack(side="left", pady=10, padx=25)
customtkinter.CTkButton(master=frame, text="Reiniciar", command=reiniciar).pack(side="left", pady=10, padx=45)
customtkinter.CTkButton(master=frame, text="Sair", command=root.destroy).pack(side="right", pady=10, padx=25)

aba_dados_salvos = ttk.Frame(notebook)
notebook.add(aba_dados_salvos, text="Dados Salvos")
criar_aba_dados_salvos()

root.mainloop()
