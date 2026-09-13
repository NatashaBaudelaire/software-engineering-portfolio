from collections import deque
import sys

def solve():
    print("=== Treasure Hunt Simulator ===\n")

    try:
        N = int(sys.stdin.readline())
        T = int(sys.stdin.readline())
        C = int(sys.stdin.readline())
    except:
        return

    if N == T:
        print("We're already here, sailor!")
        return

    MAX_ISLAND = 1000

    Q = deque([(N, 0)])  # BFS queue
    visited = {N}
    min_moves = -1

    while Q:
        P, M = Q.popleft()

        if M >= C:
            continue

        M_next = M + 1
        next_positions = []

        next_positions.append(5 * P)

        if P >= 2 and P % 2 == 0:
            next_positions.append(P // 2)
        if P >= 1 and P % 2 != 0:
            next_positions.append((P - 1) // 2)

        next_positions.append(P + 1)

        for D in next_positions:
            if 0 <= D < MAX_ISLAND:
                if D == T:
                    min_moves = M_next
                    Q.clear()  # Stop BFS
                    break
                if D not in visited:
                    visited.add(D)
                    Q.append((D, M_next))

        if min_moves != -1:
            break

    if min_moves == -1:
        print("We will need a bigger boat")
    elif min_moves <= C:
        if min_moves < C:
            print("The treasure is ours!")
        elif min_moves == C:
            print("We arrived by the skin of Neptune's teeth!")

solve()
