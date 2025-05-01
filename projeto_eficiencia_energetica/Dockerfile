# Imagem base com Python 3.10
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Evita que Python gere arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Não armazena em buffer a saída do Python para terminal
ENV PYTHONUNBUFFERED=1

# Instala as dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Atualiza pip
RUN pip install --upgrade pip

# Copia o requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto para o container
COPY . .

# Expõe a porta que o Django usará
EXPOSE 8000

# Define o comando padrão
CMD ["python", "django_app/manage.py", "runserver", "0.0.0.0:8000"]
