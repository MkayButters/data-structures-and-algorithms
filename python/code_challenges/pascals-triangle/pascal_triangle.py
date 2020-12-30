def pascals_triangle(n=0):
    if type(n) != int:
        return "no bueno, lista es no provechoso"

    else:
        output = []
        for line in range(1, n + 1):
            current_value = 1 # used to represent current value\
            current_line = []
            for i in range(1, line + 1):

                # The first value in a
                # line is always 1
                current_line += [current_value]
                current_value = int(current_value * (line - i) / i)
            output += [current_line]
        return output
