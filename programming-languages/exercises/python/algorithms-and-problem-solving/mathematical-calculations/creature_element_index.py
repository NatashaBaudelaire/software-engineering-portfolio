import sys

def solve():
    try:
        try:
            n_line = sys.stdin.readline()
            if not n_line:
                return
            N = int(n_line.strip())
        except EOFError:
            return
        except ValueError:
            return

        creature_index_map = {}
        elements_map = {}

        for _ in range(N):
            try:
                line = sys.stdin.readline().strip()
                if not line:
                    break

                parts = line.split()
                if len(parts) < 2:
                    continue

                creature = parts[0]
                element = parts[1]

                creature_index_map[creature] = element

                if element not in elements_map:
                    elements_map[element] = []
                elements_map[element].append(creature)

            except EOFError:
                break

        while True:
            try:
                command = sys.stdin.readline().strip()
                if not command:
                    break

                if command == 'Creature':
                    creature_name = sys.stdin.readline().strip()
                    if not creature_name:
                        break

                    if creature_name in creature_index_map:
                        element = creature_index_map[creature_name]
                        quantity = len(elements_map[element])
                        print(f"The Creature {creature_name} has element {element}. There are {quantity} Creatures with element {element}")
                    else:
                        print(f"The Creature {creature_name} does not exist in the CreatureIndex")

                elif command == 'Element':
                    element_name = sys.stdin.readline().strip()
                    if not element_name:
                        break

                    if element_name in elements_map:
                        creature_list = elements_map[element_name]
                        creatures_str = " ".join(creature_list)
                        print("The Creatures in the CreatureIndex with this element are:")
                        print(creatures_str)
                    else:
                        print(f"There are no Creatures in the CreatureIndex with element {element_name}")

                else:
                    print("Command is neither Creature nor Element. Programme terminated!")
                    break

            except EOFError:
                break
            except Exception:
                break

    except Exception:
        pass

solve()