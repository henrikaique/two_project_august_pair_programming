

# 📚 Documentação dos Projetos Python (Tkinter)
Esta coleção reúne três aplicações desktop interativas desenvolvidas em Python com a biblioteca Tkinter, explorando desde a integração com APIs externas até a construção de simuladores e interfaces educativas.

1. 🐾 Pokédex Python (Tkinter + PokéAPI)
📌 Explicação do Projeto
A Pokédex Python é uma aplicação desktop interativa que se conecta à PokéAPI para buscar e exibir dados detalhados sobre qualquer Pokémon em tempo real. O foco principal é demonstrar o consumo de APIs REST e a apresentação dinâmica de dados em uma interface gráfica.

🚀 Funcionalidades
🔍 Busca Dinâmica: Pesquisa por nome (ex: pikachu) ou por ID (ex: 25).

📊 Estatísticas Base: Exibição gráfica e organizada do status do Pokémon (HP, Ataque, Defesa, etc.).

📏 Informações Detalhadas: Exibição de tipos, altura, peso e habilidades.

⚡ Atalho de Busca: Suporte à tecla Enter para facilitar a navegação.

2. 💰 Simulador Financeiro - Padrão B3
📌 Explicação do Projeto
O Simulador Financeiro é uma aplicação bancária e de investimentos educacional. O projeto simula operações reais de conta corrente, compra de criptoativos e consulta de extrato financeiro. Ele utiliza o componente de abas (ttk.Notebook) para organizar visualmente as diferentes seções do aplicativo.

🚀 Funcionalidades
💳 Conta Corrente: Realização de depósitos (Entrada) e saques (Saída) com validação contínua de valores e alertas para saldo insuficiente.

₿ Criptoativos (Bitcoin): Módulo de compra simulada de BTC com cotação fixa e cálculo de frações adquiridas.

📜 Extrato Dinâmico: Atualização automática de uma lista em tempo real com o histórico de todas as movimentações da sessão.

🎨 UI Customizada: Design estilizado em abas com uma paleta de cores inspirada no mercado financeiro.

3. 🏛️ História Financeira: Eufrásia Teixeira Leite
📌 Explicação do Projeto
Este projeto é uma interface educativa e multimídia dedicada à história de Eufrásia Teixeira Leite, uma figura histórica brasileira pioneira no mercado de investimentos global. O programa combina requisições HTTP para carregar recursos visuais da web e uma linha do tempo interativa via botões acionáveis.

🚀 Funcionalidades
🖼️ Carregamento de Imagem Web: Download e renderização direta da foto histórica a partir dos servidores da Wikimedia via requisição HTTP.

🛡️ Tratamento de Erros: Exibição de mensagem informativa e layout alternativo caso não haja conexão com a internet.

📅 Linha do Tempo Interativa: Botões organizados por datas marcantes que disparam janelas pop-up (messagebox) com detalhes e curiosidades.

🛠️ Bibliotecas para Instalar
Para garantir que todos os programas funcionem corretamente no seu ambiente Python, você precisará de bibliotecas padrão e externas.

📦 Bibliotecas Nativas (Já inclusas no Python)
Estas bibliotecas vêm pré-instaladas por padrão no Python:

tkinter: Módulo principal para criação da interface gráfica e janelas de alerta (messagebox).

io: Manipulação de dados de entrada e saída em memória (usado para ler os bytes da imagem).

📥 Bibliotecas Externas (Necessário Instalar)
As bibliotecas a seguir devem ser instaladas via terminal/prompt de comando:

requests: Responsável por fazer as requisições HTTP para a PokéAPI e para baixar a foto de Eufrásia Teixeira Leite.

pillow (PIL): Biblioteca de processamento de imagem necessária para abrir, redimensionar e exibir imagens web no Tkinter.

💻 Comando para Instalação
Abra o seu terminal ou prompt de comando e execute:

Bash
pip install requests pillow
📋 Pré-requisitos & Como Executar
Certifique-se de ter o Python 3.x instalado em sua máquina.

Instale as bibliotecas externas descritas no passo acima.

Execute o arquivo do projeto desejado via terminal:

Bash
python seu_arquivo.py
📄 Licença
Todos os projetos contidos neste repositório são livres para fins de estudo, aprendizado e modificação. Sinta-se à vontade para praticar, criar forks, aprimorar a interface ou adaptar o código para seus próprios exercícios!
