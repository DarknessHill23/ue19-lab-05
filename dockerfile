# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY app.py requirements.txt ./

# Installer les dépendances
RUN pip install -r requirements.txt

# Définir le point d'entrée
CMD ["python", "app.py"]
