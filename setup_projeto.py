import os
import sys

def criar_estrutura_projeto():
    # Diretório raiz do projeto
    diretorio_base = "projeto_eficiencia_energetica"
    
    # Estrutura principal
    diretorios = [
        # Estrutura geral
        "",
        "data/raw",
        "data/processed",
        "notebooks",
        "models",
        "reports/figures",
        
        # AT1 - Análise Exploratória
        "notebooks/at1_eda",
        
        # AT2 - Modelagem e Avaliação
        "notebooks/at2_modelagem",
        "src",
        "src/preprocessing",
        "src/features",
        "src/models",
        "src/evaluation",
        
        # AT3 - Sistema Web Django
        "django_app",
        "django_app/energy_prediction",
        "django_app/energy_prediction/prediction",
        "django_app/energy_prediction/users",
        "django_app/energy_prediction/templates",
        "django_app/energy_prediction/static",
        "docker",
    ]
    
    # Criar diretórios
    for diretorio in diretorios:
        caminho_completo = os.path.join(diretorio_base, diretorio)
        os.makedirs(caminho_completo, exist_ok=True)
        print(f"Diretório criado: {caminho_completo}")
    
    # Criar arquivos básicos
    arquivos = {
        "README.md": "# Projeto de Eficiência Energética\n\nSistema preditivo para eficiência energética de edifícios usando o UCI Energy Efficiency Dataset.\n",
        "requirements.txt": "# Dependências principais\npandas\nnumpy\nscikit-learn\nmatplotlib\nseaborn\nplotly\njupyter\nxgboost\nlightgbm\ntensorflow\ndjango\npsycopg2-binary\ndjango-crispy-forms\n",
        ".gitignore": "# Arquivos a serem ignorados pelo Git\n__pycache__/\n*.py[cod]\n*$py.class\n*.so\n.Python\nenv/\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\n*.egg-info/\n.installed.cfg\n*.egg\n.env\n.venv\nvenv/\nENV/\n.ipynb_checkpoints\nmodels/*.pkl\nmodels/*.joblib\n",
        "src/__init__.py": "",
        "src/preprocessing/__init__.py": "",
        "src/features/__init__.py": "",
        "src/models/__init__.py": "",
        "src/evaluation/__init__.py": "",
        "notebooks/at1_eda/01_exploracao_inicial.ipynb": "# Notebook placeholder - será substituído pelo notebook real",
        "notebooks/at2_modelagem/01_preprocessamento.ipynb": "# Notebook placeholder - será substituído pelo notebook real",
        "notebooks/at2_modelagem/02_modelagem.ipynb": "# Notebook placeholder - será substituído pelo notebook real",
        "django_app/README.md": "# Aplicação Django para Predição de Eficiência Energética\n\nEste diretório contém a aplicação web desenvolvida com Django para predição de eficiência energética.\n",
        "docker/Dockerfile": "# Dockerfile para a aplicação\nFROM python:3.10\n\nWORKDIR /app\n\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\n\nCOPY . .\n\nEXPOSE 8000\n\nCMD [\"python\", \"django_app/energy_prediction/manage.py\", \"runserver\", \"0.0.0.0:8000\"]\n",
        "docker/docker-compose.yml": "version: '3'\n\nservices:\n  web:\n    build: ..\n    ports:\n      - \"8000:8000\"\n    depends_on:\n      - db\n  db:\n    image: postgres:13\n    environment:\n      - POSTGRES_DB=energy_prediction\n      - POSTGRES_USER=postgres\n      - POSTGRES_PASSWORD=postgres\n    volumes:\n      - postgres_data:/var/lib/postgresql/data/\n\nvolumes:\n  postgres_data:\n"
    }
    
    for caminho_relativo, conteudo in arquivos.items():
        caminho_completo = os.path.join(diretorio_base, caminho_relativo)
        diretorio = os.path.dirname(caminho_completo)
        if not os.path.exists(diretorio):
            os.makedirs(diretorio, exist_ok=True)
        
        # Verificação especial para arquivos .ipynb, que não são arquivos de texto simples
        if caminho_relativo.endswith('.ipynb'):
            # Vamos apenas criar um arquivo vazio, pois os notebooks reais serão criados pelo Jupyter
            with open(caminho_completo, 'w') as f:
                f.write("")
            print(f"Arquivo placeholder criado para notebook: {caminho_completo}")
        else:
            with open(caminho_completo, 'w') as f:
                f.write(conteudo)
            print(f"Arquivo criado: {caminho_completo}")
    
    print("\nEstrutura do projeto criada com sucesso!")
    print(f"Diretório base: {os.path.abspath(diretorio_base)}")
    print("\nPróximos passos:")
    print("1. Baixar o dataset UCI Energy Efficiency")
    print("2. Colocar o dataset na pasta 'data/raw'")
    print("3. Iniciar a análise exploratória no Jupyter Notebook")
    print("\nNota: Temos um problema de autenticação com o Docker que precisaremos resolver antes da AT3.")

if __name__ == "__main__":
    criar_estrutura_projeto()