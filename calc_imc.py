import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title('Calculadora de IMC')
app.maxsize(width=400, height=400)
app.minsize(width=400, height=400)
app.configure(background='#e1e8e5')

resultado_imc = tk.Label(app, text='', font=('Lucida', 11, 'bold'), background='#e1e8e5', justify='center')
resultado_imc.place(bordermode='inside', x=75, y=320)

def limpar_dados():
    altura = input_altura.delete(0, tk.END)
    peso = input_peso.delete(0, tk.END)
    resultado_imc.config(text='', background='#e1e8e5')

def salvar_dados():
    try:
        altura = input_altura.get()
        peso = input_peso.get()
        imc = round(float(peso)/(float(altura)*float(altura)),1)
        if imc < 16.9:
            resultado_imc.config(text=f'Seu IMC é de: {imc} - Muito abaixo do peso')
        elif imc >=17 and imc <=18.4:
            resultado_imc.config(text=f'Seu IMC é de: {imc} - Abaixo do peso')
        elif imc >=18.5 and imc <=24.9:
            resultado_imc.config(text=f'Seu IMC é de: {imc} - Peso Normal')
        elif imc >=25 and imc <=29.9:
            resultado_imc.config(text=f'Seu IMC é de: {imc} - Acima do Peso')
        elif imc >=30 and imc <=34.9:
            resultado_imc.config(text=f'Seu IMC é de: {imc} - Obesidade Grau I')
        elif imc >=35 and imc <=40:
            resultado_imc.config(text=f'Seu IMC é de: {imc} - Obesidade Grau II')
        else:
            resultado_imc.config(text=f'Seu IMC é de: {imc} - Obesidade Grau III')
            
    except(ValueError):
        messagebox.showinfo(title="Atenção", message='Preencha as informações de Altura e Peso')

titulo = tk.Label(app, text='Calculadora de IMC', font=('Lucida', 15, 'bold'), background='#e1e8e5')
titulo.pack(pady=10)

msg = tk.Label(app, text='IMC é a sigla para Índice de Massa Corpórea, \nparâmetro adotado pela Organização Mundial de Saúde \npara calcular o peso ideal de cada pessoa.', font=('Lucida', 10, 'bold'), background='#e1e8e5')
msg.pack(fill='both', pady=10)

inf_altura = tk.Label(app, text='Informe sua altura: (ex:1.70)', font=('Lucida', 10, ''), background='#e1e8e5')
inf_altura.pack()

input_altura = tk.Entry(app, width=10, justify='center')
input_altura.pack(pady=15)

inf_peso = tk.Label(app, text='Informe seu peso: (ex:70.2)', font=('Lucida', 10, ''), background='#e1e8e5')
inf_peso.pack()

input_peso = tk.Entry(app, width=10, justify='center')
input_peso.pack(pady=15)

btt_calc = tk.Button(app, text='Calcular', width=7, background='Green', fg='White', border=3, command=salvar_dados)
btt_calc.place(width=50, x=120, y=266)

btt_out = tk.Button(app, text='Sair', width=7, background='Green', fg='White', border=3, command=app.destroy)
btt_out.pack(side='bottom')

btt_out = tk.Button(app, text='Limpar', width=7, background='Green', fg='White', border=3, command=limpar_dados)
btt_out.place(width=50, x=231, y=266)



app.mainloop()