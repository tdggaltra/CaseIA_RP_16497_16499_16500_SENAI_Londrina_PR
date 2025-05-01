# 🏢 Projeto de Eficiência Energética de Edifícios

Este projeto implementa um sistema preditivo voltado para eficiência energética de edifícios, capaz de prever o consumo de energia para aquecimento e resfriamento com base em características arquitetônicas e construtivas dos imóveis.

## 📋 Descrição do Projeto

O projeto é dividido em três etapas principais:

1. **AT1 - Análise Exploratória dos Dados (EDA)** 📊: Análise detalhada do conjunto de dados UCI Energy Efficiency para entender as características e relações entre as variáveis.

2. **AT2 - Modelagem e Avaliação de Algoritmos** 🤖: Implementação e comparação de diferentes técnicas de aprendizado supervisionado para prever a carga de aquecimento e resfriamento.

3. **AT3 - Sistema Web para Predição** 🌐: Desenvolvimento de uma aplicação web com Django que permite aos usuários realizar predições utilizando os modelos treinados.

## 📈 Conjunto de Dados

O projeto utiliza o conjunto de dados público UCI Energy Efficiency Dataset, que contém 768 amostras de edifícios com as seguintes características:

- **Variáveis de entrada (8)**:
  - X1: Relative Compactness (Compacidade Relativa)
  - X2: Surface Area (Área da Superfície)
  - X3: Wall Area (Área da Parede)
  - X4: Roof Area (Área do Telhado)
  - X5: Overall Height (Altura Total)
  - X6: Orientation (Orientação)
  - X7: Glazing Area (Área Envidraçada)
  - X8: Glazing Area Distribution (Distribuição da Área Envidraçada)

- **Variáveis de saída (2)**:
  - Y1: Heating Load (Carga de Aquecimento) 🔥
  - Y2: Cooling Load (Carga de Resfriamento) ❄️

## ⚙️ Requisitos e Instalação

### Pré-requisitos

- Python 3.10 ou superior 🐍
- Conda (Anaconda ou Miniconda) 🐘
- PostgreSQL (para AT3) 🐘
- Git 🐙

### Clonando o Repositório

```bash
git clone https://github.com/tdggaltra/CaseIA_RP_16497_16499_16500_SENAI_Londrina_PR.git
cd CaseIA_RP_16497_16499_16500_SENAI_Londrina_PR
```

### 🛠️ Configuração do Ambiente

1. **Criar e ativar o ambiente conda**:

```bash
# Criar ambiente conda
conda create --name analise_preditiva python=3.10

# Ativar o ambiente
conda activate analise_preditiva

# Adicionar o ambiente como kernel do Jupyter
conda install ipykernel
python -m ipykernel install --user --name=analise_preditiva --display-name="Python (Análise Preditiva)"
```

2. **Instalar dependências**:

```bash
# Instalar pacotes para análise e modelagem
conda install pandas numpy matplotlib seaborn scikit-learn jupyter

# Instalar bibliotecas adicionais
conda install -c conda-forge xgboost lightgbm shap statsmodels plotly

# Para o sistema web Django
conda install django
pip install psycopg2-binary django-crispy-forms
```

## 📁 Estrutura do Projeto

```
projeto_eficiencia_energetica/
├── data/
│   ├── raw/                    # Dados brutos
│   └── processed/              # Dados processados
├── notebooks/
│   ├── at1_eda/                # Notebooks de análise exploratória
│   └── at2_modelagem/          # Notebooks de modelagem
├── src/
│   ├── preprocessing/          # Módulos de pré-processamento
│   ├── features/               # Engenharia de features
│   ├── models/                 # Implementação dos modelos
│   └── evaluation/             # Avaliação de modelos
├── models/                     # Modelos treinados salvos
├── reports/
│   └── figures/                # Visualizações e gráficos
└── django_app/                 # Aplicação web Django
```

## ▶️ Executando o Projeto

### AT1 - Análise Exploratória dos Dados 📊

1. **Ativar o ambiente conda**:
```bash
conda activate analise_preditiva
```

2. **Iniciar Jupyter Notebook**:
```bash
cd projeto_eficiencia_energetica
jupyter notebook
```

3. **Abrir os notebooks da AT1**:
- Navegue para a pasta `notebooks/at1_eda/`
- Abra o notebook `01_exploracao_inicial.ipynb`
- Selecione o kernel "Python (Análise Preditiva)"
- Execute as células do notebook para realizar a análise exploratória

### AT2 - Modelagem e Avaliação de Algoritmos 🤖

1. **Executar os notebooks na seguinte ordem**:
- `notebooks/at2_modelagem/01_preprocessamento.ipynb`: Pré-processamento dos dados
- `notebooks/at2_modelagem/02_modelagem.ipynb`: Implementação dos modelos de regressão
- `notebooks/at2_modelagem/03_otimizacao_hiperparametros.ipynb`: Otimização dos hiperparâmetros
- `notebooks/at2_modelagem/04_analise_modelos.ipynb`: Análise detalhada dos melhores modelos

2. **Resultados**:
- Os modelos treinados serão salvos na pasta `models/`
- As visualizações serão salvas em `reports/figures/`
- Os resultados das avaliações serão salvos em `reports/resultados_modelos.csv` e `reports/resultados_modelos_otimizados.csv`

### AT3 - Sistema Web para Predição 🌐

1. **Configurar o banco de dados PostgreSQL**:

```bash
# Criar banco de dados PostgreSQL
createdb energy_prediction
```

2. **Configurar e executar a aplicação Django**:

```bash
# Navegar para a pasta django_app
cd projeto_eficiencia_energetica/django_app

# Configurar o banco de dados no arquivo settings.py
# Executar migrações
python manage.py makemigrations
python manage.py migrate

# Criar usuário padrão para testes
python manage.py create_default_user
# E-mail: admin@admin.com
# Password: Senai@2025

# Iniciar o servidor de desenvolvimento
python manage.py runserver
```

3. **Acessar a aplicação**:
- Abra um navegador e acesse `http://localhost:8000`
- Faça login com as credenciais padrão ou crie um novo usuário
- Utilize a interface para realizar predições de eficiência energética

## 🔍 Detalhes da Implementação

### Análise Exploratória (AT1) 📊

A análise exploratória inclui:
- Estatísticas descritivas das variáveis
- Análise de correlação entre variáveis
- Visualização de distribuições e relações
- Identificação de outliers
- Análise de multicolinearidade
- Insights para modelagem

### Modelagem (AT2) 🤖

Os modelos implementados incluem:
- Regressão Linear 📈
- Ridge e Lasso (com regularização) 🔧
- Random Forest 🌲
- Gradient Boosting 📈
- XGBoost 🚀
- Redes Neurais (MLP) 🧠

Cada modelo é avaliado utilizando:
- RMSE (Root Mean Squared Error) 📉
- MAE (Mean Absolute Error) 📊
- R² (Coeficiente de Determinação) 📈

Os melhores modelos são otimizados através de:
- Validação cruzada (K-Fold) ↔️
- Grid Search para otimização de hiperparâmetros 🎛️
- Análise de importância de features 🔍

### Sistema Web (AT3) 🌐

A aplicação Django inclui:
- Sistema de login e autenticação 🔐
- Gerenciamento de usuários (CRUD) 👥
- Interface para testes do modelo de regressão 📊
- Banco de dados PostgreSQL para armazenar predições 💾
- Visualização e exclusão de predições salvas 📋

## 📝 Resultados e Conclusões

Os melhores modelos para predição das cargas de aquecimento (🔥) e resfriamento (❄️) são baseados em algoritmos de ensemble (como XGBoost e Gradient Boosting), que conseguem capturar relações não-lineares complexas entre as variáveis.

As características mais importantes para a eficiência energética são a altura total, a compacidade relativa e a área da superfície do edifício.

## 👥 Contribuição

Para contribuir com este projeto:
1. Faça um fork do repositório 🍴
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`) 🌿
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`) ✅
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`) 📤
5. Abra um Pull Request 📩

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Contato

Tiago Dutra Galvão de Almeida - [tdggaltra@gmail.com](mailto:tdggaltra@gmail.com) - [GitHub](https://github.com/tdggaltra)

Link do projeto: [https://github.com/tdggaltra/CaseIA_RP_16497_16499_16500_SENAI_Londrina_PR](https://github.com/tdggaltra/CaseIA_RP_16497_16499_16500_SENAI_Londrina_PR)