def binary_search(books, book, start, end):
    if start > end:
        return start, False
    mid = (start + end) // 2
    if books[mid] == book:
        return mid, True
    elif books[mid] > book:
        return binary_search(books, book, start, mid - 1)
    else:
        return binary_search(books, book, mid + 1, end)

def process_actions(books, actions):
    for action, book in actions:
        pos, found = binary_search(books, book, 0, len(books) - 1)
        if action == "search":
            if found:
                print(f"The book {book} is at position {pos + 1}")
            else:
                print(f"Could not find the book {book}")
        elif action == "insert":
            if found:
                print(f"{book} is already at position {pos + 1}")
            else:
                books.insert(pos, book)
                print(f"{book} was successfully placed at position {pos + 1}")

n = int(input("Enter number of books: "))
books = [input("Enter book title: ").strip() for _ in range(n)]
k = int(input("Enter number of actions: "))
actions = [tuple(input("Enter action and book title: ").split(maxsplit=1)) for _ in range(k)]

process_actions(books, actions)
