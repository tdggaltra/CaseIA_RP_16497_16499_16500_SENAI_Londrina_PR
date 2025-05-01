# 🌱 Projeto de Eficiência Energética - SENAI Londrina/PR
**por Tiago Dutra Galvão**

Este é um sistema web desenvolvido com Django para realizar predições de **eficiência energética em edifícios**, com base em atributos físicos do imóvel. O sistema permite a criação de usuários, realização de predições de carga de aquecimento/resfriamento, histórico das predições e visualização dos dados.

## 🚀 Funcionalidades

- Registro e login de usuários.
- Área de perfil pessoal.
- Cadastro e gerenciamento de usuários restrito a superusuários (CRUD).
- Interface para inserção de dados de edifícios.
- Predição de carga térmica com modelo de Machine Learning.
- Armazenamento e listagem do histórico de predições.

## 📦 Tecnologias utilizadas

- Python 3.10+
- Django 5.2
- PostgreSQL
- Scikit-learn (para o modelo de ML)
- Bootstrap 4 (via CDN)
- HTML5 / CSS3
- Docker & Docker Compose 🐳

---

## 📁 Estrutura do projeto

```bash
├── energy_prediction/ # Configurações principais do Django
├── users/ # App para autenticação e gerenciamento de usuários
├── prediction/ # App responsável pelas predições
├── templates/ # Templates HTML da aplicação
├── static/ # Arquivos estáticos (opcional)
├── models/ # Modelos de ML e pré-processamento
├── manage.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Como rodar o projeto

### 🐳 Usando Docker (Recomendado)

**1. Pré-requisitos**
- Docker e Docker Compose instalados e em execução

**2. Clone o repositório**
```bash
git clone https://github.com/tdggaltra/CaseIA_RP_16497_16499_16500_SENAI_Londrina_PR.git
cd CaseIA_RP_16497_16499_16500_SENAI_Londrina_PR
```

**3. Inicie os containers**
```bash
docker-compose up --build
```

**4. Acesse a aplicação**
Abra seu navegador e acesse: http://localhost:8000

**5. Credenciais padrão**
```
Usuário: admin
Email: admin@admin.com
Senha: Senai@2025
```

**6. Parar os containers**
```bash
# Pressione Ctrl+C no terminal
# Ou em outro terminal execute:
docker-compose down
```

### 💻 Execução Local (Alternativa)

**1. Clone o repositório**
```bash
git clone https://github.com/tdggaltra/CaseIA_RP_16497_16499_16500_SENAI_Londrina_PR.git
cd CaseIA_RP_16497_16499_16500_SENAI_Londrina_PR/django_app
```

**2. Crie e ative um ambiente virtual**
```bash
python3 -m venv venv
source venv/bin/activate # no Linux/Mac
venv\Scripts\activate # no Windows
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure o banco de dados PostgreSQL**
Crie o banco manualmente via terminal ou GUI (como DBeaver ou pgAdmin):
```sql
CREATE DATABASE energy_prediction;
```

No arquivo `settings.py`, configure as credenciais:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'energy_prediction',
        'USER': 'postgres',
        'PASSWORD': 'postgres', # ou sua senha real
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**5. Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Crie um superusuário**
```bash
python manage.py createsuperuser
```

**7. Inicie o servidor**
```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

---

## 📊 Modelo de Machine Learning

- Os modelos e pré-processadores estão armazenados em `models/` (como `preprocessor.pkl` e `model.pkl`).
- Eles são carregados automaticamente pelo sistema para realizar as predições.
- Você pode treinar ou atualizar o modelo via notebooks na pasta `at2_modelagem`.

---

## 🐛 Problemas comuns

- **Erro 500 após logout**: certifique-se de que a URL de logout redireciona para a página de login (já tratado).
- **Erro de template não encontrado**: verifique se os templates estão em `templates/{app_name}/arquivo.html` e se `DIRS` em `settings.py` inclui o caminho certo.
- **Erro com Docker**: se enfrentar problemas com "container já existe", execute `docker-compose down` e tente novamente.
- **Erro de conexão com o banco de dados no Docker**: verifique se o host está definido como "db" no settings.py quando usando Docker.
- **ModuleNotFoundError**: verifique se todas as dependências estão instaladas no container. Você pode adicionar bibliotecas faltantes no arquivo requirements.txt e reconstruir com `docker-compose up --build`.

---

## 🐳 Comandos Docker Úteis

- **Listar containers em execução**: `docker ps`
- **Ver logs da aplicação**: `docker-compose logs -f web`
- **Ver logs do banco de dados**: `docker-compose logs -f db`
- **Entrar no shell do container**: `docker-compose exec web bash`
- **Executar comandos Django**: `docker-compose exec web bash -c "cd django_app && python manage.py COMANDO"`
- **Backup do banco de dados**: `docker-compose exec db pg_dump -U postgres energy_prediction > backup.sql`

---

## 📌 To-Do / Melhorias futuras

- Exportar resultados em PDF.
- Adicionar testes automatizados.
- Melhorar visualizações gráficas dos históricos.
- Hospedar no Heroku/Vercel com banco externo.
- Implementar CI/CD para deploy automático.

---

## 🤝 Agradecimentos

Projeto desenvolvido no contexto da **Case IA RP 16497/16499/16500 do SENAI Londrina/PR**, com o objetivo de aplicar inteligência artificial para soluções sustentáveis em eficiência energética.

---

## 📜 Licença

Este projeto é de uso educacional. Consulte o autor Tiago Dutra Galvão (tdggalvao@gmail.com) para usos comerciais.