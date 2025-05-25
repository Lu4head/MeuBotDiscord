<h1 align="center">
  <br>
  RPG Discord Bot
  <br>
</h1>

<h4 align="center">Rolar dados, ajuda para criação de ficha, trilha sonora</h4>

<p align="center">
  <a href="#Visão Geral">Visão Geral</a>
  •
  <a href="#installation">Instalação</a>
  •
  <a href="">Documentação</a>
</p>

# Visão Geral

Este é um bot de discord para auxiliar jogadores de RPG oferencendo uma série de funcionalidades para facilitar o processo de criação de fichas, jogabilidade e melhorar a experiência de jogo.


# Instalação

1. Clone o repositório
```bash
git clone https://github.com/Lu4head/MeuBotDiscord.git
```

2. Crie o ambiente virutal python
```bash
python -m venv .venv
```

3. Ative o ambiente virutal

    a. Linux
    ```bash
    source .venv/bin/activate
    ```
    b. Windows
    ```bash
    .venv\Scripts\activate
    ```

4. Instale as dependências
```bash
pip install -r requirements.txt
```

5. Crie o arquivo .env com as variáveis de ambiente (exemplo de como deve ficar o arquivo em .env.example)
    - Chaves de API obtidas nos sites oficiais do Discord DEV e Google Gemini API

6. Inicie a aplicação com:
```bash
python main.py
```

### Extras:
- Documentação da API do Discord: https://discord.com/developers/docs/intro
- Documentação da API do Google Gemini: https://developers.generativeai.google/
- Documentação da biblioteca discord.py : https://discordpy.readthedocs.io/en/stable/index.html
