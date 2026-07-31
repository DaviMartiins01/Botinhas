# 🤖 Bot de Busca e Recomendação de Animes

Bot para **Discord** desenvolvido em Python que utiliza a **Jikan API** para buscar informações sobre animes e facilitar a descoberta de novos títulos diretamente pelo Discord.

O bot permite pesquisar animes pelo nome, consultar lançamentos de uma determinada temporada ou dia da semana e visualizar diversas informações sobre cada obra.

---

## ✨ Funcionalidades

### 🔎 Busca por anime

Pesquise um anime pelo título e receba informações como:

- 📖 Sinopse
- ⭐ Nota e quantidade de usuários
- 📺 Tipo
- 📅 Ano de lançamento
- 🎬 Número de episódios
- 📌 Status
- 🎭 Gêneros
- ⏱️ Duração dos episódios
- 🖼️ Imagem de capa
- 🔗 Outras informações disponibilizadas pela API

### 📅 Animes por temporada

Consulte os animes disponíveis em uma determinada temporada e veja quais títulos estão sendo lançados no período.

### 📆 Animes por dia da semana

Consulte quais animes possuem episódios programados para um determinado dia da semana.

### 💡 Descoberta de animes

Utilize as informações fornecidas pela API para encontrar novos animes e descobrir títulos que podem ser interessantes.

---

## 🖥️ Exemplo

Exemplo de uma busca realizada pelo bot:

<img width="602" height="382" alt="image" src="https://github.com/user-attachments/assets/45747416-5eac-46de-8b6c-501b734c1ec8" />

O bot apresenta as informações de forma organizada através de um **Discord Embed**, tornando a consulta mais agradável e fácil de visualizar.

---

## 🛠️ Tecnologias utilizadas

- 🐍 **Python**
- 💬 **Discord API** — integração com o Discord
- 🔌 **Jikan API** — obtenção dos dados dos animes
- 🌐 **Requests** — comunicação com a API
- 🧩 **Discord Embeds** — apresentação das informações

---

## 🔄 Funcionamento

O fluxo básico do bot funciona da seguinte maneira:

```text
👤 Usuário
    │
    ▼
💬 Comando no Discord
    │
    ▼
🤖 Bot
    │
    ▼
🌐 Jikan API
    │
    ▼
📊 Dados do anime
    │
    ▼
💬 Discord Embed
    │
    ▼
👤 Usuário
