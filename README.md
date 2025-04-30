# Todo Workshop

Prosta aplikacja Python CLI typu todo, przygotowana do ćwiczeń z __code review__ 😄

## Cel warsztatu

Celem ćwiczenia jest:
- Przećwiczenie praktyki code review
- Praca z pull requestami na GitHubie
- Zachowanie działającego projektu na końcu warsztatu

---

## Wymagania wstępne

### Obowiązkowo:
- Konto na [GitHub](https://github.com)

#### Opcjonalnie (do pracy lokalnej):
- Python 3.x zainstalowany lokalnie
- Git zainstalowany lokalnie

#### Alternatywnie:
- Konto na [replit.com](https://replit.com)
- Skopiowanie repozytorium i uruchomienie go tam

---

## Jak uruchomić

```bash
python todo.py add "Zrób plan warsztatu"
python todo.py list
python todo.py export
python todo.py done 1
```

---

## Jak działać

### z lokalnym repo

#### zaciągnięcie brancha

`git clone https://github.com/odpaleniek1337/todo-workshop.git`

`git checkout main`

`git pull`

`git checkout 'nazwa brancha'`

#### po przejrzeniu/stestowaniu

`git checkout main`

`git pull`

`git checkout 'nazwa brancha'`

tu mogą pojawić się merge konflikty - do rozwiązania

`git merge main`

`git push -u origin 'nazwa brancha'`

### z replit

- Testowanie i działanie na replicie - skopiowanie repo
- Popisać z asystentem, żeby wygenerował klikalne 'run' w pliku .replit

#### Github

- Po spushowaniu tworzymy pull requesta
- Łączymy z głównym branchem

## Przygotowane branche

Poniżej lista branchy do napisania/przejrzenia, przetestowania i ewentualnego poprawienia:

### 1 rzut

#### Proste

- [ ] `feature_add_priority`
- [ ] `feature_add_due_date`
- [ ] `feature_delete_done_task`

#### Średnie
- [ ] `feature_add_csv_export`
- [ ] `feature_add_logging` - zamienić printy na logowanie

### 2 rzut

Nowe funkcjonalności lub usprawnienia:

- [ ] Edycja istniejącego zadania
- [ ] Obsługa kategorii / tagów - taski mogą mieć kategorie/tagi - dodanie filtracji - np todo.py filter tag "zakupy"

### 3 rzut

- [ ] `feature_advanced_logging` - dodać logowanie jako dekorator dla funkcji
    - przy wywoływaniu oraz kończeniu wywoływania funkcji powinno się logować
    - powinno działać gdy podawana jest flaga --debug
    - jeśli jest debug - printuje wszystko, jeśli nie ma tej flagi powinno printować tylko potrzebne informacje 
- [ ] `feature_input_validation` - rozważenie edge casów - kiedy skrypt może nie zadziałać, kiedy coś może się zepsuć
- [ ] własna inwencja

