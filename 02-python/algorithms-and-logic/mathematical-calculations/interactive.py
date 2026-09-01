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

        pokedex_map = {}
        elements_map = {}

        for _ in range(N):
            try:
                line = sys.stdin.readline().strip()
                if not line:
                    break

                parts = line.split()
                if len(parts) < 2:
                    continue

                pokemon = parts[0]
                element = parts[1]

                pokedex_map[pokemon] = element

                if element not in elements_map:
                    elements_map[element] = []
                elements_map[element].append(pokemon)

            except EOFError:
                break

        while True:
            try:
                command = sys.stdin.readline().strip()
                if not command:
                    break

                if command == 'Pokemon':
                    pokemon_name = sys.stdin.readline().strip()
                    if not pokemon_name:
                        break

                    if pokemon_name in pokedex_map:
                        element = pokedex_map[pokemon_name]
                        quantity = len(elements_map[element])
                        print(f"The Pokémon {pokemon_name} has element {element}. There are {quantity} Pokémon with element {element}")
                    else:
                        print(f"The Pokémon {pokemon_name} does not exist in the Pokédex")

                elif command == 'Element':
                    element_name = sys.stdin.readline().strip()
                    if not element_name:
                        break

                    if element_name in elements_map:
                        pokemon_list = elements_map[element_name]
                        pokemons_str = " ".join(pokemon_list)
                        print("The Pokémon in the Pokédex with this element are:")
                        print(pokemons_str)
                    else:
                        print(f"There are no Pokémon in the Pokédex with element {element_name}")

                else:
                    print("Command is neither Pokémon nor Element. Programme terminated!")
                    break

            except EOFError:
                break
            except Exception:
                break

    except Exception:
        pass

solve()