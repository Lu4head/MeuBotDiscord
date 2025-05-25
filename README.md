# Bot para discord

### Instalação

1. Clone o repositório
```bash
git clone https://github.com/Vinicius-Mendes/bot-discord.git
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
