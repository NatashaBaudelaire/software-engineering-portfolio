import sys

def solve():
    try:
        k_str = sys.stdin.readline().strip()
        if not k_str:
            return  
        K = int(k_str)
    except:
        return 

    players_ping = []

    for _ in range(K):
        try:
            line = sys.stdin.readline().strip()
            if not line:
                continue 

            parts = line.split()
            name = parts[0]
            ping_str_ms = parts[1]

            ping_value = int(ping_str_ms[:-2]) 

            players_ping.append((name, ping_value))
        except:
            continue

    if not players_ping:
        return

    highest_ping = players_ping[0][1] 
    lowest_ping = players_ping[0][1]

    for _, current_ping in players_ping:
        if current_ping > highest_ping:
            highest_ping = current_ping
        if current_ping < lowest_ping:
            lowest_ping = current_ping

    players_highest_ping = []
    players_lowest_ping = []

    for name, current_ping in players_ping:
        if current_ping == highest_ping:
            players_highest_ping.append(name)
        if current_ping == lowest_ping:
            players_lowest_ping.append(name)

    str_highest = ", ".join(players_highest_ping)
    str_lowest = ", ".join(players_lowest_ping)

    output_formatted = (
        f"The highest ping is {highest_ping}ms, of player(s) {str_highest}. "
        f"And the lowest is {lowest_ping}ms, of player(s) {str_lowest}."
    )

    print(output_formatted)

solve()
