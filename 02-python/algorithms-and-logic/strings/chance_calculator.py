def calculate_chance(hour, am_pm, baits):
    if am_pm.lower() not in ["am", "pm"]:
        return "Invalid data."
    if hour < 1 or hour > 12 or baits < 0:
        return "Invalid data."
    if am_pm.lower() == "am":
        hour_24 = 0 if hour == 12 else hour
    else:
        hour_24 = 12 if hour == 12 else hour + 12
    if hour_24 < 5:
        hour_24 += 24
    def current_chance(h):
        if h == 5:
            return 5.0
        previous = current_chance(h - 1)
        h_mod = h % 24

        if 6 <= h_mod <= 15:
            if h_mod % 2 == 0:
                return previous + baits / 2
            else:
                return previous + (previous % 7)
        else:
            if h_mod % 2 == 0:
                return previous + baits
            else:
                return previous + (previous % 10)
    final_chance = current_chance(hour_24)
    result = f"The chance of Slamou appearing is {final_chance:.1f}%."
    if final_chance >= 100:
        result += "\nAnd today it will appear."
    return result
time_input = input("Enter the time (e.g., '6 PM'): ").strip()
baits = int(input("Enter the number of baits: ").strip())

hour, am_pm = time_input.split()
hour = int(hour)

print(calculate_chance(hour, am_pm, baits))