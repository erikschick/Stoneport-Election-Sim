from random import gauss
import numpy
from collections import namedtuple, defaultdict

vote_dist = namedtuple("vote_dist", ("joyce", "madelaine", "dirk", "terri"))


BULK_TEST_MODE = False


def by_value_descending(kv):
    k, v = kv
    return -1 * v

def roll(dist):
    return numpy.clip(gauss(*dist), 0, 100)

def calc_district(district_name, dist):
    return {
        "Joyce Ruby": roll(dist.joyce),
        "Madelaine Hightower": roll(dist.madelaine),
        "Dirk Rugman": roll(dist.dirk),
        "Terri Engleshaff": roll(dist.terri),
    }

def district(district_name, dist):
    if BULK_TEST_MODE:
        _bulk_district(district_name, dist)
        return
    
    votes = calc_district(district_name, dist)
    total = sum(votes.values())
    print("**__{} opinion polls__**".format(district_name))
    for name, vote in sorted(votes.items(), key=by_value_descending):
        print("{:>19}: {:0.0f}%".format(name, 100 * vote/total))
    print()

def _bulk_district(district_name, dist):
    wins = defaultdict(int)
    win_pct = defaultdict(list)
    for _ in range(2000):
        votes = calc_district(district_name, dist)
        votes = sorted(votes.items(), key=by_value_descending)
        winner = votes[0]
        wins[winner[0]] += 1
        win_pct[winner[0]].append(winner[1] - votes[1][1])
    total_wins = sum(wins.values())
    wins = {name: 100 * w/total_wins for name, w in wins.items()}
    print("{} bulk test winner".format(district_name))
    for name, w in sorted(wins.items(), key=by_value_descending):
        print("  {}: {:0.0f}% (avg {:0.0f}% lead)".format(name, w, numpy.average(win_pct[name])))
    print()
    


district('Blue Ridge', vote_dist(
    joyce=(40, 5),
    madelaine=(10, 5),
    dirk=(40, 10),
    terri=(10, 10),
))
district('Northgate', vote_dist(
    joyce=(33, 5),
    madelaine=(40, 2),
    dirk=(27, 5),
    terri=(0, 5),
))
district('Ovenswarmth', vote_dist(
    joyce=(45, 3),
    madelaine=(30, 5),
    dirk=(20, 5),
    terri=(2, 5),
))
district('Worker\'s Purse', vote_dist(
    joyce=(55, 10),
    madelaine=(1, 2),
    dirk=(10, 2),
    terri=(34, 5),
))
district('Crow\'s Nest', vote_dist(
    joyce=(39, 1),
    madelaine=(31, 3),
    dirk=(28, 5),
    terri=(0, 2),
))
district('Market Square', vote_dist(
    joyce=(50, 10),
    madelaine=(5, 10),
    dirk=(30, 5),
    terri=(10, 5),
))
district('Graveyard Docks', vote_dist(
    joyce=(50, 10),
    madelaine=(25, 15),
    dirk=(25, 15),
    terri=(0, 1),
))
district('Shipyard', vote_dist(
    joyce=(48, 2),
    madelaine=(44, 4),
    dirk=(16, 10),
    terri=(1, 10),
))
district('Tower District', vote_dist(
    joyce=(45, 15),
    madelaine=(45, 10),
    dirk=(10, 5),
    terri=(0, 2),
))
