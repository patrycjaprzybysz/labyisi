import requests #zapytania http
import json #manipulacja danymi


def save_data(api_url, output_file):
    response = requests.get(api_url) # wysałnie zapytania do api i zapisanie odp do response
    data = response.json() #przetworzenie zapytania do formatu json wynik jako obiekt

    with open(output_file, 'w') as file: # otwiera plik o wskazanej nazwie i robi tak
        # ze plik zostanie automatycznie zamkniety po wykonaniu kodu (w- with)
        json.dump(data, file, indent=4) #apisuje dane data do pliku file w formacie JSON z
        # wcięciami ustawionymi na 4 spacje


api_url = "https://jsonplaceholder.typicode.com/photos"
output_file = "photos.json"
save_data(api_url, output_file)

print(f"Dane zostały zapisane do pliku {output_file}.")


