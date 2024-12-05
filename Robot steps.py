def robot_steps(n):
  if n == 0:
    return 1
  elif n < 0:
    return 0
  ways = [0] * (n + 1)
  ways[0] = 1
  for i in range(1, n + 1):
    ways[i] += ways[i - 1]
    if i >= 2:
      ways[i] += ways[i - 2]
    if i >= 3:
      ways[i] += ways[i - 3]
  return ways[n]
n = int(input("Enter the distance in meters: "))
num_ways = robot_steps(n)
print(f"The robot can walk {n} meters in {num_ways} ways.")
