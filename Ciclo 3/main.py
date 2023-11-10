import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get()) / 100
        imc = peso / (altura ** 2)
        resultado_imc.set(f"IMC: {imc:.2f}")
    except ValueError:
        resultado_imc.set("Preencha peso e altura corretamente.")

def reiniciar():
    entry_nome.delete(0, 'end')
    entry_endereco.delete(0, 'end')
    entry_altura.delete(0, 'end')
    entry_peso.delete(0, 'end')
    resultado_imc.set("IMC: ")

root = customtkinter.CTk()
root.geometry("700x500")
root.title("Cálculo de IMC")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

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

root.mainloop()