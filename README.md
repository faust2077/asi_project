# Projekt aplikacji webowej do predykcji spalonych kalorii podczas wysiłku fizycznego

Aplikacja webowa zbudowana w Streamlit, umożliwiająca wprowadzanie danych dotyczących wysiłku fizycznego i wyświetlanie predykcji liczby spalonych kalorii na podstawie wytrenowanego modelu uczenia maszynowego.

## Klonowanie repozytorium

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/faust2077/asi_project.git
   cd asi_project
   ```

## Uruchamianie aplikacji lokalnie
   
1. Utwórz i aktywuj środowisko wirtualne:
   
- Windows (PowerShell):

   ```bash
   python -m venv .venv
   Set-ExecutionPolicy Unrestricted -Scope Process
   .venv\Scripts\activate
   ```

- Linux/macOS:

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

2. Zainstaluj wymagane pakiety:
   
   ```bash
   pip install -r app/requirements.txt
   ```
    
3. Uruchom serwer aplikacji:

   ```bash
   streamlit run app/app.py
   ```
   
4. Otwórz przeglądarkę i przejdź do:

   http://localhost:8501

## Uruchamianie aplikacji w kontenerze Docker

1. Zbuduj obraz Dockera:

   ```bash
   docker build -t caltracker:v1.0 .
   ```
    
2. Uruchom aplikację w kontenerze:

   ```bush
   docker run -p 8501:8501 caltracker:v1.0
   ```
   
3. Otwórz przeglądarkę i przejdź do:

   http://localhost:8501


