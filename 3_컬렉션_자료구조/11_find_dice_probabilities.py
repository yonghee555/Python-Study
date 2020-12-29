from collections import Counter, defaultdict
from typing import DefaultDict


def find_dice_probabilities(S, n_faces=6):
    if S > 2 * n_faces or S < 2:
        return None

    cdict = Counter()
    ddict = defaultdict(list)

    for dice1 in range(1, n_faces + 1):
        for dice2 in range(1, n_faces + 1):
            cdict[dice1 + dice2] += 1
            ddict[dice1 + dice2].append([dice1, dice2])

    return [cdict[S], ddict[S]]

def test_find_dice_probabilities():
    S = 5
    n_faces = 6
    results = find_dice_probabilities(S, n_faces)
    print(results)
    assert(results[0] == 4)
    print("테스트 통과!")

if __name__ == "__main__":
    test_find_dice_probabilities()