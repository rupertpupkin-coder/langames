from src.algorithm import conclusion
from src.algorithm import find_gamers


def test_find_conclusion_no_one_installed_game_means_yellow():
    assert conclusion(['not installed']) == 'YELLOW'

def test_find_conclusion_all_installed_game_means_green():
    assert conclusion(['installed']) == 'GREEN'

def test_find_conclusion_no_one_owns_game_means_red():
    assert conclusion(['not owned']) == 'RED'

def test_find_conclusion_one_installed_one_not_installed_yellow():
    assert conclusion(['not installed', 'installed']) == 'YELLOW'

def test_find_conclusion_not_owned_installed_red():
    assert conclusion(['not owned', 'installed']) == 'RED'




def test_find_gamers(data):
    assert find_gamers({gamer['name'] for gamer in data['gamers']}) == 'Agneta'



# TODO: Add more tests for find_conclusion! At least enough to cover states RED, YELLOW and GREEN




# TODO: Add tests for find_gamers. Hint: either load data/gamers.json into the test, or make up some test data here!
# (do you prefer separate test data file, or hard-coding the test data in the test? Discuss!)


