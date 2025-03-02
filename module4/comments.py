true_lines = [1 for line in open(0) if line.strip().startswith("#")]
print(sum(true_lines))
