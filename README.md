# 🌐 IBGE Dashboard - Indicadores Socioeconômicos do Brasil

Projeto web em Python com o microframework **Bottle**, que consome a **API pública do IBGE** para exibir gráficos dinâmicos de indicadores sociais e econômicos do Brasil.

---

## 🚀 Demonstração

![Gráfico de turistas](static/data/chegada_turistas.png)
![Gráfico de educação](static/data/gastos_educacao.png)

---

## 🧠 Funcionalidades

- ✅ Consome dados da [API oficial do IBGE](https://servicodados.ibge.gov.br).
- ✅ Trata e organiza os dados usando **pandas**.
- ✅ Gera gráficos com **matplotlib**.
- ✅ Renderiza página HTML com **Bootstrap 5**.
- ✅ Estrutura modular (routes, templates, utilitários).
- ✅ CSS customizado com responsividade.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia     | Versão     | Descrição                              |
|----------------|------------|----------------------------------------|
| Python         | 3.12+      | Linguagem principal                    |
| Bottle         | 0.12.25    | Microframework web                     |
| Requests       | 2.31.0     | Consumo da API                         |
| Pandas         | 2.2.2      | Manipulação de dados                   |
| Matplotlib     | 3.9.0      | Visualização de dados                  |
| HTML/CSS       | -          | Interface                             |
| Bootstrap      | 5.3        | Layout responsivo                      |

---

## ▶️ Como executar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/jcarlossc/bottle-ibge.git

# Acesse o diretório
cd bottle-ibge

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate           # Windows
source venv/bin/activate        # Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py

# Para sair do ambiente virtual
deactivate
```
---

## ▶️ Acesse no navegador: 
```
    http://localhost:8080
```

---

📌 Possíveis melhorias
- Adicionar filtro para seleção de indicadores.
- Geração interativa de gráficos com Plotly.
- Implementar cache local com SQLite.
- Deploy em servidor (Render, Vercel ou Heroku).

---

## 📄 Licença
Este projeto está licenciado sob a MIT License.

---

## Comandos importantes:

```bash
python -m venv venv               # Cria um ambiente virtual
venv\Scripts\activate             # Ativa o ambiente no Windows
source venv/bin/activate          # Ativa o ambiente no Linux/macOS
deactivate                        # Encerra o ambiente virtual

pip install nome-pacote           # Instala um pacote
pip uninstall nome-pacote         # Remove um pacote
pip freeze > requirements.txt     # Gera (ou atualiza) o arquivo de dependências
pip install -r requirements.txt   # Instala pacotes listados no requirements.txt
pip list                          # Lista pacotes instalados
pip show nome-pacote              # Exibe detalhes de um pacote
```