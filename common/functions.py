from datetime import datetime

# Funkcja przeliczająca milisekundy na format godzina:minuta:sekunda
from_ts = lambda x: datetime.fromtimestamp(x).strftime('%H:%M:%S')

# Funkcja przeliczająca stopnie Kelvina na Celsjusza, zaokraglona do dwóch miejsc po przecinku

# Funkcja przeliczająca m/s na km/h, zaokraglona do dwóch miejsc po przecinku
