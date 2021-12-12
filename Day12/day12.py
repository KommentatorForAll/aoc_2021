

def getNumberOfRoutes(current, visited, cons, visited_twice=False):
    if current == "end":
        return 1
    total = 0        
    for connection in cons:
        first, second = connection
        if second == current:
            first, second = second, first

        if first == current:
            if not (second == second.lower() and second in visited):
                total += getNumberOfRoutes(second, visited + [second], cons, visited_twice)
            elif not visited_twice and second != "start":
                total += getNumberOfRoutes(second, visited + [second], cons, True)
    return total


def main():
    with open("input.txt", "r") as file:
        connections = [tuple(connection.split("-")) for connection in file.read().split("\n")]

    routes = getNumberOfRoutes("start", ["start"], connections, False) # Replace False with True to get part 1 solution
    print(routes)


if __name__ == '__main__':
    main()
