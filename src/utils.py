
def extract_arguments(args: tuple[str]):
    data = args[0].split()[1:]
    accumulator = []
    
    for i in data:
        if i.startswith("-"):
            accumulator.append([i, ""])
        elif len(accumulator) > 0 and len(accumulator[-1][1]) == 0:
            accumulator[-1][1] += i
        else:
            accumulator[-1][1] += " " + i
    return accumulator
