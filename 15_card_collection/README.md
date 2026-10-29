# Основний проєкт: облік колекції карток

Це запропонована реалізована тема. Погодження викладачем ще не отримане — умова ДЗ 15 вимагає узгодити проєкт.

Консольна програма на Python + SQLite. Вміє додавати картки, шукати за назвою, змінювати кількість, видаляти з підтвердженням, рахувати статистику та експортувати CSV. Дані зберігаються між запусками. SQL-параметри захищають введений текст від інтерпретації як SQL.

Команди з цієї папки:

```bash
python main.py add "Sol Ring" --quantity 2
python main.py add "The Ur-Dragon" --quantity 1 --notes "Commander"
python main.py list
python main.py list --search Dragon
python main.py set 1 4
python main.py stats
python main.py export collection.csv
python main.py delete 1
python -m pytest test_collection.py -v
```

`collection.py` — зберігання і логіка; `main.py` — команди; `test_collection.py` — тести.
За замовчуванням створюється порожня `collection.db` поряд із програмою. Власну базу можна вказати перед командою: `python main.py --db test.db list`.
Пошук через SQLite lower() нечутливий до регістру для латиниці; для кирилиці використовуй відповідний регістр.
CSV зберігає введений текст без змін. Проєкт є локальним навчальним застосунком.

Що пояснити на захисті: клас та об'єкти, параметризовані запити, PRIMARY KEY, CRUD, argparse, обробка ValueError, pytest fixtures, збереження у файлі SQLite.
