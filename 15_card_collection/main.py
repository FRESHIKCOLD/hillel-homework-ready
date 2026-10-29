import argparse
from pathlib import Path
from collection import CardCollection


def make_parser():
    parser = argparse.ArgumentParser(description="Облік колекції карток")
    parser.add_argument("--db", default=str(Path(__file__).with_name("collection.db")))
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="Додати картку")
    add.add_argument("name")
    add.add_argument("--game", default="Magic: The Gathering")
    add.add_argument("--quantity", type=int, default=1)
    add.add_argument("--notes", default="")
    listing = commands.add_parser("list", help="Перегляд та пошук")
    listing.add_argument("--search", default="")
    update = commands.add_parser("set", help="Змінити кількість")
    update.add_argument("id", type=int)
    update.add_argument("quantity", type=int)
    delete = commands.add_parser("delete", help="Видалити картку")
    delete.add_argument("id", type=int)
    commands.add_parser("stats", help="Статистика колекції")
    export = commands.add_parser("export", help="Експорт CSV")
    export.add_argument("path", nargs="?", default="collection.csv")
    return parser


def main():
    parser = make_parser()
    args = parser.parse_args()
    collection = CardCollection(args.db)
    try:
        if args.command == "add":
            card_id = collection.add(args.name, args.game, args.quantity, args.notes)
            print(f"Додано картку з ID {card_id}")
        elif args.command == "list":
            cards = collection.list_cards(args.search)
            if not cards:
                print("Карток не знайдено")
            for card in cards:
                print(f"{card['id']}: {card['name']} | {card['game']} | {card['quantity']} шт. | {card['notes']}")
        elif args.command == "set":
            collection.update_quantity(args.id, args.quantity)
            print("Кількість оновлено")
        elif args.command == "delete":
            answer = input(f"Видалити картку ID {args.id}? Введіть yes: ")
            if answer.strip().lower() == "yes":
                collection.delete(args.id)
                print("Картку видалено")
            else:
                print("Видалення скасовано")
        elif args.command == "stats":
            stats = collection.statistics()
            print(f"Записів: {stats['entries']}; карток: {stats['total']}")
        elif args.command == "export":
            collection.export_csv(args.path)
            print(f"Збережено: {args.path}")
    except (ValueError, OSError) as error:
        parser.exit(1, f"Помилка: {error}\n")
    finally:
        collection.close()


if __name__ == "__main__":
    main()
