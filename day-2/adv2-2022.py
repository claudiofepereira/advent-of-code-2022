
win = 6
draw = 3
loss = 0

rock = 1
paper = 2
scissors = 3

game_scores_1 = {
    'A X': draw + rock,
    'A Y': win + paper,
    'A Z': loss + scissors,
    'B X': loss + rock,
    'B Y': draw + paper,
    'B Z': win + scissors,
    'C X': win + rock,
    'C Y': loss + paper,
    'C Z': draw + scissors,
}

# X -> loss, Y -> draw, Z -> win

game_scores_2 = {
    'A X': loss + scissors,
    'A Y': draw + rock,
    'A Z': win + paper,
    'B X': loss + rock,
    'B Y': draw + paper,
    'B Z': win + scissors,
    'C X': loss + paper,
    'C Y': draw + scissors,
    'C Z': win + rock,
}


def main(rounds, game_scores, part):
    points = 0
    rounds = [round for round in open('adv2-2022.txt', 'r').read().split('\n')]
    points = sum([game_scores.get(round, 0) for round in rounds])
    print(f'Points for part {part}: {points}')

if __name__ == '__main__':
    rounds = [round for round in open('adv2-2022.txt', 'r').read().split('\n')]
    main(rounds, game_scores_2, 2)