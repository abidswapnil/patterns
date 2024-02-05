def generate_pattern(N):
  # Create a 2D list with dimensions (2*N - 1) x (2*N - 1) filled with 0s
  pattern = [[0] * (2 * N - 1) for _ in range(2 * N - 1)]
  
  # Fill the pattern with the desired numbers
  for i in range(N):
    for j in range(i, 2 * N - 1 - i):
      pattern[i][j] = N - i
      pattern[j][i] = N - i
      pattern[2 * N - 2 - i][j] = N - i
      pattern[j][2 * N - 2 - i] = N - i
  
  # Print the pattern
  for row in pattern:
    print(' '.join(map(str, row)))


# Test the function with N = 6
N = 6
generate_pattern(N)
