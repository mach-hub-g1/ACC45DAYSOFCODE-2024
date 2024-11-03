# cook your dish here
def find_winner_and_lead(N, rounds):
    cumulative_score_player1 = 0
    cumulative_score_player2 = 0
    max_lead = 0
    winner = 0

    for i in range(N):
        score_player1, score_player2 = rounds[i]
        cumulative_score_player1 += score_player1
        cumulative_score_player2 += score_player2

        if cumulative_score_player1 > cumulative_score_player2:
            lead = cumulative_score_player1 - cumulative_score_player2
            if lead > max_lead:
                max_lead = lead
                winner = 1
        else:
            lead = cumulative_score_player2 - cumulative_score_player1
            if lead > max_lead:
                max_lead = lead
                winner = 2

    return winner, max_lead

# Example input processing
N = int(input().strip())
rounds = [tuple(map(int, input().strip().split())) for _ in range(N)]

winner, max_lead = find_winner_and_lead(N, rounds)
print(winner, max_lead)
