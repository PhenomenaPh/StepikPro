for block in open(0):
    if not block.strip().startswith("#"):
        print(block, end="")
