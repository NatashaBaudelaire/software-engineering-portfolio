import sys

def solve():
    N_str = sys.stdin.readline()
    if not N_str:
        return
    N = int(N_str.strip())

    suggestions = []

    for index in range(N):
        line = sys.stdin.readline().strip()
        if not line:
            continue
        parts = line.split()
        topic = parts[0]
        votes = int(parts[-1])
        suggestions.append([topic, votes, index])
    suggestions.sort(key=lambda s: (-s[1], s[2]))

    for topic, votes, _ in suggestions:
        print(f"{topic} {votes}")
if __name__ == "__main__":
    solve()
