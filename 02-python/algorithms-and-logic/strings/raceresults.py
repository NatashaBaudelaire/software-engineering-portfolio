import sys

def solve():
    results = [None] * 8

    for _ in range(8):
        try:
            line = sys.stdin.readline()
            if not line:
                break

            parts = line.strip().split()
            runner = parts[0]
            position = int(parts[1])

            index = position - 1
            if 0 <= index < 8:
                results[index] = runner

        except (ValueError, IndexError):
            continue
    # Print the results
    print("Runner - Position")
    for i in range(8):
        runner = results[i] if results[i] else "N/A"
        position = i + 1
        print(f"{runner} - {position}")

if __name__ == "__main__":
    solve()
