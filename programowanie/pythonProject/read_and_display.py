import json


def read_and_display_data(input_file):
    with open(input_file, 'r') as file: # otworzenie pliku w trybie odczytu r - read
        data = json.load(file) # odczytuje zawartość pliku file i przetwarza ją jako JSON,
        # zwracając wynik w postaci obiektu Python

    for item in data[:10]:  # tylko pierwsze 10 pozycji
        print(f"ID: {item['id']}, Title: {item['title']}")


input_file = "photos.json"
read_and_display_data(input_file)
