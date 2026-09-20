import sys


def analyse_invasion():
    """Simulate Skrull invasion events and print outcomes (British English)."""
    MESSAGE_ATTACK = "Order an immediate attack; this time we shall dominate Earth"
    MESSAGE_RETREAT = "Not worth continuing, let us retreat and devise a new plan"
    MESSAGE_WAIT = "We are not ready to attack yet; we shall wait a little longer"
    MESSAGE_FAILURE = "Complete failure, there are no Skrulls left infiltrating"


    try:
        M = int(sys.stdin.readline())
        I = int(sys.stdin.readline())
        N = int(sys.stdin.readline())
    except Exception:
        return


    earth_alert = 0
    skrulls_infiltrated = I
    finished = False

    for _ in range(N):
        if finished:
            break

        try:
            event = sys.stdin.readline().strip()
        except Exception:
            break

        if event == "Substitution":
            try:
                new_infiltrators = int(sys.stdin.readline())
                skrulls_infiltrated += new_infiltrators
            except Exception:
                continue

        elif event == "Exposure":
            earth_alert += 30

        elif event == "Counter-attack":
            try:
                detected = int(sys.stdin.readline())
                skrulls_infiltrated -= detected
            except Exception:
                continue

        # Check final conditions
        if skrulls_infiltrated <= 0:
            skrulls_infiltrated = 0
            print(MESSAGE_FAILURE)
            finished = True
        elif skrulls_infiltrated >= M:
            print(MESSAGE_ATTACK)
            finished = True
        elif earth_alert >= 100:
            print(MESSAGE_RETREAT)
            finished = True

    if not finished:
        print(MESSAGE_WAIT)

analyse_invasion()
