N = int(input("Enter the number of votes: ").strip())
impostor = input("Enter the impostor's name: ").strip()

votes = {}
voters = set()
all_players = set()

for _ in range(N):
    line = input().strip()
    name, vote = line.split(": ")
    voters.add(name)
    all_players.add(name)
    all_players.add(vote)

    if vote in votes:
        votes[vote] += 1
    else:
        votes[vote] = 1
if len(voters) < len(all_players):
    missing = len(all_players) - len(voters)
    print(f"Incomplete voting. Votes from {missing} player(s) are missing")
else:
    max_votes = 0
    expelled = None
    tie = False

    for player, count in votes.items():
        if count > max_votes:
            max_votes = count
            expelled = player
            tie = False
        elif count == max_votes and player != expelled:
            tie = True
    if tie or max_votes == 0:
        print("Tie. No one was expelled")
    else:
        if expelled == impostor:
            print(f"{expelled} was expelled with {max_votes} vote(s). They were the IMPOSTOR")
        else:
            print(f"{expelled} was expelled with {max_votes} vote(s). They were INNOCENT")
