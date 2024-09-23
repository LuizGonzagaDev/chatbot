import tkinter as tk
from tkinter import scrolledtext
import openai

# Definir a chave da API (substitua pela sua)
openai.api_key ="sua chave api"

# Função para enviar a mensagem ao modelo GPT
def enviar_mensagem():
    mensagem = entrada_texto.get()  # Capturar o texto digitado pelo usuário
    if mensagem.strip() == "":  # Ignorar mensagens vazias
        return
    
    # Adicionar a mensagem do usuário na caixa de texto
    texto_conversa.insert(tk.END, f"Você: {mensagem}\n")
    entrada_texto.delete(0, tk.END)  # Limpar a entrada de texto

    # Processar a mensagem com o GPT
    lista_mensagens.append({"role": "user", "content": mensagem})
    resposta = openai.ChatCompletion.create(
        model="gpt versao",  # ou "gpt-3.5-turbo"
        messages=lista_mensagens,
    )
    
    # Pegar a resposta da API
    resposta_chat = resposta['choices'][0]['message']['content']
    lista_mensagens.append({"role": "assistant", "content": resposta_chat})
    
    # Adicionar a resposta do bot na caixa de texto
    texto_conversa.insert(tk.END, f"Bot: {resposta_chat}\n")
    texto_conversa.yview(tk.END)  # Scroll para a parte mais recente da conversa

# Configuração da janela principal
janela = tk.Tk()
janela.title("Chatbot com GPT")

# Caixa de texto com scroll para exibir a conversa
texto_conversa = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
texto_conversa.grid(column=0, row=0, columnspan=2)
texto_conversa.configure(state="normal")  # Para permitir a adição de texto

# Entrada de texto onde o usuário digita
entrada_texto = tk.Entry(janela, width=40, font=("Arial", 12))
entrada_texto.grid(column=0, row=1)

# Botão para enviar a mensagem
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem, font=("Arial", 12))
botao_enviar.grid(column=1, row=1)

# Lista de mensagens para o contexto do chat
lista_mensagens = []

# Iniciar a interface
janela.mainloop()