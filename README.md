# Projekt aplikacji webowej do predykcji spalonych kalorii podczas wysiłku fizycznego

Aplikacja webowa zbudowana w **Streamlit**, umożliwiająca wprowadzanie danych dotyczących wysiłku fizycznego i wyświetlanie predykcji liczby spalonych kalorii na podstawie wytrenowanego modelu uczenia maszynowego.

---

## Jak skutecznie skorzystać z projektu?

Zanim uruchomisz aplikację, musisz uruchomić **Kedro pipelines**, aby:

1. Surowe dane zostały przetworzone na gotowe do treningu.
2. Stworzyć i wytrenować model – pipelines muszą być uruchomione w odpowiedniej kolejności (patrz sekcja [Kedro pipelines](#kedro-pipelines)).

---

## Klonowanie repozytorium

```bash
git clone https://github.com/faust2077/asi_project.git
cd asi_project
```


---

## Zależności Kedro

1. **Instalacja pakietów Kedro (przez pip):**

```bash
pip install -r kedro/requirements.txt
```

2. **Stwórz środowisko Conda wraz ze wszystkimi zależnościami:**

```bash
conda env create -f kedro/environment.yml
```

3. **Aktywuj środowisko Conda:**

```bash
conda activate caltracker-kedro-env
```


---

## Kedro pipelines

Przejdź do folderu `kedro`:

```bash
cd kedro
```

1. **Pipeline przetwarzania danych (uruchom jako pierwszy):**

```bash
kedro run --pipeline=data_processing
```

Ten pipeline przetwarza surowe dane `calories.csv` na dane gotowe do treningu – `preprocessed_data.csv`.
2. **Pipeline treningu modelu (uruchom jako drugi):**

```bash
kedro run --pipeline=model_training
```

Ten pipeline pobiera przetworzone dane `preprocessed_data.csv`, wykonuje operacje związane z uczeniem modelu i zwraca wytrenowany model – `final_model.pkl`.
Pipeline output wskazuje lokalizację w Google Cloud Storage, zatem tam umieszczany jest `final_model.pkl`.

---

## Google Application Credentials

Aplikacja korzysta z Google Cloud Storage do przechowywania modelu, więc potrzebujesz klucza JSON do API, który należy przekazać podczas uruchomienia aplikacji.

### Lokalnie

```bash
export GOOGLE_APPLICATION_CREDENTIALS=ścieżka/do/klucza/gcs/klucz.json
```


### Poprzez Docker

Użyj opcji `-e` w `docker run` (patrz sekcja [Uruchamianie aplikacji w kontenerze Docker](#uruchamianie-aplikacji-w-kontenerze-docker)).

---

## Uruchamianie aplikacji lokalnie

1. **Utwórz i aktywuj środowisko wirtualne:**
    - **Windows (PowerShell):**

```bash
python -m venv .venv
Set-ExecutionPolicy Unrestricted -Scope Process
.venv\Scripts\activate
```
    - **Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. **Zainstaluj wymagane pakiety:**

```bash
pip install -r app/requirements.txt
```

3. **Załaduj klucz API:**

```bash
export GOOGLE_APPLICATION_CREDENTIALS=ścieżka/do/klucza/gcs/klucz.json
```

4. **Uruchom serwer aplikacji:**

```bash
streamlit run app/app.py
```

5. **Otwórz przeglądarkę i przejdź do:**

```
http://localhost:8501
```


---

## Uruchamianie aplikacji w kontenerze Docker

1. **Zbuduj obraz Dockera:**

```bash
docker build -t caltracker:v1.0 .
```

2. **Uruchom aplikację w kontenerze wraz z załadowaniem klucza API:**

```bash
docker run -p 8501:8501 \
  -v ścieżka/do/klucza/gcs/klucz.json:/app/service_account.json \
  -e GOOGLE_APPLICATION_CREDENTIALS=/app/service_account.json \
  caltracker:v1.0
```

3. **Otwórz przeglądarkę i przejdź do:**

```
http://localhost:8501
```


---

**Wskazówki:**

- Upewnij się, że masz wymagane uprawnienia do korzystania z Google Cloud Storage.
- Przed uruchomieniem aplikacji upewnij się, że pipeline'y Kedro zostały poprawnie wykonane.

---

