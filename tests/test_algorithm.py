import json
from pathlib import Path

from src.algorithm import conclusion, find_gamers



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




def test_find_name_of_gamer():
    data = json.loads(Path('./data/gamers.json').read_text(encoding='utf8'))
    all_gamers = find_gamers(data)
    assert 'Agneta' in all_gamers


def test_find_all_name_of_gamers():
    data = json.loads(Path('./data/gamers.json').read_text(encoding='utf8'))
    all_gamers = find_gamers(data)
    assert all_gamers == {'Björn', 'Benny', 'Anni-Frid', 'Agneta'}

def test_find_name_bjoern():
    data = json.loads(Path('./data/gamers.json').read_text(encoding='utf8'))
    all_gamers = find_gamers(data)
    assert 'Björn' in all_gamers

def test_find_all_name_of_gamers2():
    data = json.loads(Path('./data/gamers.json').read_text(encoding='utf8'))
    all_gamers = find_gamers(data)
    assert all_gamers == {'Benny', 'Björn', 'Anni-Frid', 'Agneta'}


def test_find_name_of_gamer_hehe():
    data =  {
        "gamers": [
            {
                "name": "Agneta",
                "games": [
                    {
                        "game": "Alien Swarm",
                        "installed": True
                    },
                    {
                        "game": "Quake III: Arena",
                        "installed": True
                    },
                    {
                        "game": "Wreckfest",
                        "installed": False
                    },
                    {
                        "game": "Brawlhalla",
                        "installed": True
                    }
                ]
            }
        ]
    }

    all_gamers = find_gamers(data)
    assert 'Agneta' in all_gamers



# TODO: Add tests for find_gamers. Hint: either load data/gamers.json into the test, or make up some test data here!
# (do you prefer separate test data file, or hard-coding the test data in the test? Discuss!)