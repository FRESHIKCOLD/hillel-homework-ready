import csv
import pytest
from collection import CardCollection


@pytest.fixture
def collection():
    result = CardCollection(":memory:")
    yield result
    result.close()


def test_add_search_update_delete(collection):
    card_id = collection.add("Sol Ring", "MTG", 2)
    assert collection.list_cards("ring")[0]["quantity"] == 2
    collection.update_quantity(card_id, 5)
    assert collection.statistics() == {"entries": 1, "total": 5}
    collection.delete(card_id)
    assert collection.list_cards() == []
    assert collection.statistics() == {"entries": 0, "total": 0}


@pytest.mark.parametrize("quantity", [-1, 1.5, True])
def test_invalid_quantity(collection, quantity):
    with pytest.raises(ValueError):
        collection.add("Sol Ring", "MTG", quantity)
    assert collection.statistics()["entries"] == 0


def test_empty_name(collection):
    with pytest.raises(ValueError):
        collection.add("  ", "MTG")


def test_missing_id(collection):
    with pytest.raises(ValueError):
        collection.update_quantity(999, 2)
    with pytest.raises(ValueError):
        collection.delete(999)


def test_export(collection, tmp_path):
    collection.add("Картка, приклад", "MTG", 3, "Український текст")
    path = tmp_path / "cards.csv"
    collection.export_csv(path)
    with path.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))
    assert rows[0]["name"] == "Картка, приклад"
    assert rows[0]["quantity"] == "3"


def test_persistence(tmp_path):
    database = tmp_path / "test.db"
    first = CardCollection(database)
    first.add("Dragon", "MTG")
    first.close()
    second = CardCollection(database)
    try:
        assert second.list_cards()[0]["name"] == "Dragon"
    finally:
        second.close()


def test_search_is_literal(collection):
    collection.add("100% Magic", "MTG")
    collection.add("Other", "MTG")
    assert len(collection.list_cards("%")) == 1
    assert collection.list_cards("' OR 1=1 --") == []
