from rollabledie.dice import RollableDie


def test_upper():
    die = RollableDie()
    assert die.sides ==  6