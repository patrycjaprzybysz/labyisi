
FROM python:3.9

# katalog /app w kontenerze
WORKDIR /app

# kopiowanie zawartosci folderu pythonProject z hosta do kontenera w katalogu /app
COPY code/pythonProject/ /app

# Skrypt pythona uruchomiony
CMD ["python", "script.py"]
