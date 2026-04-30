# Question 8: AlternatingPath
#
# Given an origin and a destination in a directed graph in which edges can be blue or red,
# determine the length of the shortest path from the origin to the destination in which
# the edges traversed alternate in color. Return -1 if no such path exists.
#
# Examples:
#
# Input: [(A, B, "blue"), (A, C, "red"), (B, D, "blue"), (B, E, "blue"), (C, B, "red"),
#          (D, C, "blue"), (A, D, "red"), (D, E, "red"), (E, C, "red")]
#
# Input: origin = A, destination = E
# Output: 4 (path: A→D (red), D→C (blue), C→B (red), B→E (blue))
#
# Input: origin = E, destination = D
# Output: -1 (only path is: E→C (red), C→B (red), B→D (blue))
#          — invalid because red follows red (not alternating)


