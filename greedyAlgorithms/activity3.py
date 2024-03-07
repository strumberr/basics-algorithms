

def min_moves_to_permutation(a):

    a_sorted = sorted(a)

    moves = 0

    for i, val in enumerate(a_sorted, start=1):
        moves += abs(val - i)
        
    return moves


a = [11, 2, 1, 3]

min_moves = min_moves_to_permutation(a)

print(min_moves)

