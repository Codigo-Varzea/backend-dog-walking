import pytest
from datetime import date, timedelta
from .walks import Walk, Walks, WalkStatus
from .pets import Pet

@pytest.fixture
def empty_walks():
    return Walks()

@pytest.fixture
def filled_walks(empty_walks, one_walk_waiting):
    empty_walks.create(one_walk_waiting)
    return empty_walks

@pytest.fixture
def today():
    return date.today()

@pytest.fixture
def start_time():
    return date(2021, 7, 13)

@pytest.fixture
def end_time():
    return date(2021, 7, 14)

@pytest.fixture
def new_pet():
    return Pet("Spike", "Bulldog")

@pytest.fixture
def one_walk_waiting(today, new_pet):
    return Walk(today, timedelta(minutes=30), 20000.0, 30000.0, [new_pet])

@pytest.fixture
def today_plus_30(today):
    return today + timedelta(minutes=30)

def test_create_walk(empty_walks, one_walk_waiting, today_plus_30):
    empty_walks.create(one_walk_waiting)

    assert len(empty_walks.fetch_all()) == 1
    assert one_walk_waiting in empty_walks.fetch_all()

    assert one_walk_waiting.price == Walk.get_base_price()
    assert one_walk_waiting.end_date == today_plus_30

def test_delete_walk(filled_walks, one_walk_waiting):
    assert len(filled_walks.fetch_all()) == 1

    filled_walks.delete(one_walk_waiting)

    assert len(filled_walks.fetch_all()) == 0

def test_update_walk(filled_walks):
    walk = filled_walks.fetch_all()[0]

    assert walk.status == WalkStatus.WAITING

    walk.status = WalkStatus.WALKING

    filled_walks.update(walk)

    assert filled_walks.fetch_all()[0].status == WalkStatus.WALKING

def test_get_by_id_walk(filled_walks, one_walk_waiting):
    walk = filled_walks.get_by_id(str(one_walk_waiting.id))

    assert walk == one_walk_waiting