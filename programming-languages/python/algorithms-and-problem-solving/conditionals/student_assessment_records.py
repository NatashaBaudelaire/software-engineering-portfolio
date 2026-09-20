from collections import OrderedDict

Q = int(input("Enter number of records: "))
database = OrderedDict()

for _ in range(Q):
    entry = input().split()
    name = entry[0]
    assessment = entry[1]
    mark = float(entry[2])
    
    if name not in database:
        database[name] = OrderedDict()
    database[name][assessment] = mark

N = int(input("Enter number of commands: "))
commands = []
for _ in range(N):
    cmd = input().strip()
    arg = input().strip()
    commands.append((cmd, arg))

for cmd, arg in commands:
    if cmd == "add":
        name, assessment, mark = arg.split()
        mark = float(mark)
        if name not in database:
            database[name] = OrderedDict()
        database[name][assessment] = mark
    elif cmd == "search":
        name = arg
        if name not in database:
            print(f"{name} does not exist in the system\n")
        else:
            print(f"{name}:")
            for asmt, mk in database[name].items():
                print(f"-{asmt}: {mk:.2f}")
            print()
    elif cmd == "query":
        assessment = arg
        found = False
        has_it = []
        does_not_have = []
        for student, assessments in database.items():
            if assessment in assessments:
                has_it.append((student, assessments[assessment]))
                found = True
            else:
                does_not_have.append(student)
        if not found:
            print(f"No one has the assessment {assessment}\n")
        else:
            print(f"{assessment}:")
            for st, mk in has_it:
                print(f"-{st}: {mk:.2f}")
            if does_not_have:
                print("Do not have: " + ", ".join(does_not_have) + "\n")
            else:
                print("Do not have: \n")
