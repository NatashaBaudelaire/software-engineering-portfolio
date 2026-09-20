import sys

def parse_value(value_str):
    value_str = value_str.strip()
    if value_str.startswith('(') and value_str.endswith(')'):
        try:
            coords = value_str[1:-1].split(',')
            x = int(coords[0].strip())
            y = int(coords[1].strip())
            return (x, y)
        except ValueError:
            return None
    else:
        try:
            return int(value_str)
        except ValueError:
            return None

def format_output(result):
    if isinstance(result, tuple):
        return f"({result[0]},{result[1]})"
    else:
        return str(result)

def add_vectors(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def subtract_vectors(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def scalar_multiplication(v1, scalar):
    return (v1[0] * scalar, v1[1] * scalar)

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

operation_functions = {
    '+': add_vectors,
    '-': subtract_vectors,
    '*': scalar_multiplication,
    '.': dot_product
}

def solve():
    try:
        N_str = sys.stdin.readline()
        if not N_str:
            return
        N = int(N_str.strip())
    except:
        return

    results = []
    
    for _ in range(N):
        try:
            line = sys.stdin.readline().strip()
            if not line:
                continue

            if line.startswith('('):
                end_v1 = line.find(')')
                if end_v1 != -1:
                    value1_str = line[:end_v1 + 1].strip()
                    remainder = line[end_v1 + 1:].strip()
                else:
                    continue
            else:
                parts = line.split(maxsplit=2)
                if len(parts) < 3:
                    continue
                value1_str = parts[0]
                remainder = " ".join(parts[1:])

            operator = None
            value2_str = None
            
            for op in operation_functions.keys():
                if remainder.startswith(f"{op} "):
                    operator = op
                    value2_str = remainder[len(op) + 1:].strip()
                    break

            if not operator or not value2_str:
                continue

            v1 = parse_value(value1_str)
            v2 = parse_value(value2_str)
            
            if v1 is None or v2 is None:
                continue

            func = operation_functions[operator]
            result = func(v1, v2)

            results.append(format_output(result))
            
        except Exception:
            continue
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()
