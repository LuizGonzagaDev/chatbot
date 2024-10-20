Correções e melhorias:
Substituir o modelo: A linha onde você especifica o modelo "gpt versao" precisa ser corrigida. Utilize um modelo válido, como "gpt-3.5-turbo" ou "gpt-4" se você tiver acesso.

Tratamento de exceções: Para evitar que erros interrompam o fluxo, adicione um bloco try-except ao redor da chamada da API.

Melhorar a formatação e a clareza: Você pode melhorar a disposição da interface para que o campo de entrada e o botão fiquem visualmente mais ajustados.

Melhorias e explicações:
Substituição do modelo: Alterei a linha do modelo para "gpt-3.5-turbo" ou "gpt-4". Lembre-se de usar o modelo que sua chave API tem permissão para acessar.

Tratamento de erros: Adicionei um try-except ao redor da chamada openai.ChatCompletion.create para capturar e exibir erros de conexão ou processamento da API.

Interface gráfica: A interface continua simples, com um campo de entrada para a mensagem, um botão para enviar e uma área com ScrolledText para exibir as conversas.

Como testar:
Instalação das dependências:

openai: Use pip install openai para instalar a biblioteca da OpenAI.
tkinter: Geralmente já está incluído na instalação padrão do Python.
Substitua a chave da API: Certifique-se de substituir sua chave api pela sua chave de API da OpenAI para que o código funcione corretamente.

Agora, você pode usar a interface gráfica para interagir com o modelo GPT diretamente da sua aplicação!
