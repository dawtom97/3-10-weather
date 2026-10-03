# 3-10 Weather

Prosta aplikacja pogodowa napisana w Pythonie, która cyklicznie pobiera aktualne dane pogodowe z API OpenWeather, zapisuje je lokalnie do pliku Excel oraz w bazie danych MySQL.

Projekt zawiera również moduł dashboardu przygotowany w Streamlit, umożliwiający prezentację zapisanych danych pogodowych w formie tabeli, metryk oraz wykresów.

## Funkcjonalności

- pobieranie aktualnej pogody dla wybranego miasta z OpenWeather API,
- zapis temperatury, wilgotności, ciśnienia, zachmurzenia i prędkości wiatru,
- zapis czasu wschodu słońca oraz czasu wykonania pomiaru,
- automatyczny zapis danych do pliku `weather.xlsx`,
- zapis danych do bazy MySQL,
- automatyczne utworzenie tabeli `records`,
- wykonywanie kolejnego pomiaru co 120 sekund,
- dashboard Streamlit do prezentacji zgromadzonych danych.

## Struktura projektu

```text
3-10-weather/
│
├── common/
│   └── functions.py
│
├── services/
│   ├── dashboard.py
│   ├── files.py
│   ├── mysql_db.py
│   └── openweather_api.py
│
├── config.py
└── main.py
```

### Najważniejsze moduły

`main.py` – główny proces aplikacji. Tworzy tabelę w MySQL, pobiera pogodę, zapisuje dane do Excela i bazy danych, a następnie powtarza operację co 120 sekund.

`config.py` – ładuje konfigurację aplikacji ze zmiennych środowiskowych zapisanych w pliku `.env`.

`services/openweather_api.py` – komunikacja z OpenWeather API.

`services/files.py` – zapis i odczyt danych z pliku Excel.

`services/mysql_db.py` – obsługa połączenia z MySQL oraz zapis danych pogodowych.

`services/dashboard.py` – dashboard przygotowany przy użyciu Streamlit.

`common/functions.py` – funkcje pomocnicze, między innymi konwersja timestampu.

## Wymagania

Do uruchomienia projektu potrzebujesz:

- Python 3,
- działającego serwera MySQL,
- klucza API OpenWeather.

Klucz API można uzyskać po utworzeniu konta w OpenWeather:

https://openweathermap.org/

## Instalacja

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/dawtom97/3-10-weather.git
cd 3-10-weather
```

### 2. Utwórz środowisko wirtualne

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 3. Zainstaluj zależności

Repozytorium nie zawiera obecnie pliku `requirements.txt`, dlatego wymagane biblioteki można zainstalować poleceniem:

```bash
pip install python-dotenv requests pandas openpyxl mysql-connector-python streamlit
```

Warto również utworzyć w projekcie plik `requirements.txt`:

```text
python-dotenv
requests
pandas
openpyxl
mysql-connector-python
streamlit
```

Następnie zależności będzie można instalować standardowo:

```bash
pip install -r requirements.txt
```

## Konfiguracja `.env`

W głównym katalogu projektu utwórz plik:

```text
.env
```

Przykładowa konfiguracja:

```env
ENV_OW_API_KEY=your_openweather_api_key
ENV_OW_CITY=Warsaw

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=weather
```

### Zmienne środowiskowe

`ENV_OW_API_KEY` – klucz API OpenWeather.

`ENV_OW_CITY` – miasto, dla którego mają być pobierane dane pogodowe.

`DB_HOST` – adres serwera MySQL, np. `localhost`.

`DB_USER` – użytkownik MySQL.

`DB_PASSWORD` – hasło użytkownika MySQL.

`DB_NAME` – nazwa bazy danych.

> **Uwaga:** port MySQL jest obecnie ustawiony bezpośrednio w kodzie na `3307` w `services/mysql_db.py`. Jeżeli Twój MySQL działa na standardowym porcie `3306`, zmień tę wartość w kodzie lub przenieś port do konfiguracji `.env`.

## Przygotowanie MySQL

Przed pierwszym uruchomieniem aplikacji utwórz bazę danych odpowiadającą wartości `DB_NAME`.

Przykład:

```sql
CREATE DATABASE weather;
```

Tabela `records` zostanie utworzona automatycznie podczas uruchomienia programu.

## Uruchomienie aplikacji

Po skonfigurowaniu `.env` oraz MySQL uruchom:

```bash
python main.py
```

Aplikacja:

```text
OpenWeather API
      ↓
   main.py
      ↓
 ┌────┴─────┐
 ↓          ↓
Excel      MySQL
weather.xlsx
```

Po uruchomieniu program pobiera dane pogodowe, zapisuje je w pliku `weather.xlsx` i bazie MySQL, a następnie czeka 120 sekund przed wykonaniem kolejnego pomiaru.

Program działa w pętli do momentu jego ręcznego zatrzymania, np. za pomocą:

```text
Ctrl + C
```

## Dashboard Streamlit

Projekt posiada również moduł dashboardu:

```text
services/dashboard.py
```

Dashboard prezentuje między innymi:

- aktualną temperaturę,
- temperaturę odczuwalną,
- prędkość wiatru,
- wilgotność, ciśnienie lub zachmurzenie,
- tabelę zapisanych pomiarów,
- wykres zmian temperatury,
- wykres wilgotności.

### Ważne

Dashboard nie jest obecnie w pełni połączony z głównym procesem aplikacji.

W `dashboard.py` źródło danych jest ustawione na:

```python
FILE = "weather_2026_350.csv"
```

natomiast `main.py` zapisuje dane do:

```text
weather.xlsx
```

Przed uruchomieniem dashboardu należy więc ujednolicić źródło danych.

Przykładowo dashboard może odczytywać plik generowany przez aplikację:

```python
df = pd.read_excel("weather.xlsx")
```

Na końcu `services/dashboard.py` można następnie dodać:

```python
if __name__ == "__main__":
    render()
```

i uruchomić dashboard poleceniem:

```bash
streamlit run services/dashboard.py
```

## Bezpieczeństwo

Plik `.env` zawiera klucz API i dane dostępowe do bazy danych, dlatego nie powinien być wysyłany do repozytorium Git.

Warto utworzyć plik `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
weather.xlsx
```

Dobrym rozwiązaniem jest również dodanie pliku `.env.example`:

```env
ENV_OW_API_KEY=
ENV_OW_CITY=

DB_HOST=localhost
DB_USER=
DB_PASSWORD=
DB_NAME=
```

`.env.example` może być przechowywany w repozytorium, ponieważ nie zawiera prawdziwych haseł ani kluczy API.

## Technologie

Python, OpenWeather API, MySQL, Pandas, Streamlit, python-dotenv oraz Excel/OpenPyXL.

## Autor

Projekt: [dawtom97](https://github.com/dawtom97)

Repository:

https://github.com/dawtom97/3-10-weather
