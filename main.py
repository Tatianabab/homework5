with open ("ddd.txt", "r") as a:
    for line in a:
        b=line.split(":")
        c=line.split(":")
        print(f"{b[0]}:{c[1]}")


