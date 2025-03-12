# 🎬 AutoClipYoutube - Gerador Automático de Clips de Live

**AutoClipYoutube** é uma ferramenta desenvolvida em Python para **monitorar o chat de transmissões ao vivo no YouTube** e gerar automaticamente **clipes com base em comandos do chat** (ex.: `!clip`).  
O projeto foi pensado para uso **automatizado**, ideal para streamers que desejam registrar momentos importantes da live sem interromper o conteúdo.  

> **⚙️ Projeto pessoal para portfólio, destacando habilidades em automação, integração com APIs e manipulação de vídeo.**

---

## 🚀 Funcionalidades

- ✅ **Monitoramento em tempo real** do chat de lives no YouTube.
- ✅ Identificação de comandos específicos enviados pelos usuários (`!clip`).
- ✅ **Geração automática de clipes** com os últimos 30 segundos da transmissão.
- ✅ Gravação contínua da live para garantir o acesso ao conteúdo a qualquer momento.
- ✅ Sistema de logs completo para acompanhamento da execução.
- ✅ Fácil de rodar localmente com empacotamento em `.exe` (não precisa instalar dependências no cliente).

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **YouTube Data API v3** (leitura de chat, verificação de live)
- **yt-dlp** (gravação contínua da live)
- **ffmpeg** (corte dos clipes com precisão)
- **Subprocessos** (execução de comandos externos via Python)
- **Sistema de logging personalizado**

---

## 🧠 Conceitos Aplicados

- Clean Code e Modularização (organização por responsabilidades: core, services, utils).
- Comunicação com APIs (REST, YouTube API).
- Manipulação de arquivos de vídeo via linha de comando.
- Paralelismo (gravação da live enquanto monitora o chat).
- Tratamento de erros e exceções para garantir robustez.
- Criação de sistema empacotado (executável standalone com PyInstaller).

---

## 💻 Como Executar (Em desenvolvimento!)

1. **Clone o repositório:**

        ```bash
        git clone https://github.com/seuusuario/AutoClipYoutube.git

2. **Configure suas credenciais no config.py:**
    
        API_KEY do YouTube.
        Channel ID da live que deseja monitorar.

3. **Instale as dependências:**

        pip install -r requirements.txt

4. **Execute o projeto:**

        python main.py


## 🌟 Por que esse projeto é importante?

    - Demonstração prática de integração entre sistemas (chat YouTube + captura + vídeo).
    - Aplicação real de automação de processos em um ambiente moderno (streaming).
    - Uso de ferramentas poderosas em conjunto (Python, ffmpeg, yt-dlp).
    - Focado em produtividade para criadores de conteúdo.

## 🤝 Contribuições

    Este é um projeto pessoal, mas sugestões e feedbacks são sempre bem-vindos!
    Se quiser colaborar ou customizar para outras plataformas (ex.: Twitch), sinta-se à vontade para abrir uma issue ou pull request.

## 📫 Contato

    Caso queira saber mais ou contratar um projeto personalizado:
    Robson Caetano
    LinkedIn | Email: robsoncaetano@email.com