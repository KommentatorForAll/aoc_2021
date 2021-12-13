

def get_number_of_routes(current, visited, cons, visited_twice=False):
    if current == "end":
        return 1
    total = 0        
    for connection in cons:
        first, second = connection
        if second == current:
            first, second = second, first

        if first == current:
            if not (second == second.lower() and second in visited):
                total += get_number_of_routes(second, visited + [second], cons, visited_twice)
            elif not visited_twice and second != "start":
                total += get_number_of_routes(second, visited + [second], cons, True)
    return total


def main():
    with open("input.txt", "r") as file:
        connections = [tuple(connection.split("-")) for connection in file.read().split("\n")]

    # Replace False with True to get part 1 solution
    routes = get_number_of_routes("start", ["start"], connections, False)
    print(routes)


if __name__ == '__main__':
    main()
