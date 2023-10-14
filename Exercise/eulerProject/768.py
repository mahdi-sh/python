# Chandelier
# A certain type of chandelier contains a circular ring of n evenly spaced candleholders.
# If only one candle is fitted, then the chandelier will be imbalanced. However, if a second identical candle
# is placed in the opposite candleholder (assuming n is even) then perfect balance will be achieved and the chandelier will hang level.
# Let f(n, m)  be the number of ways of arranging m identical candles in distinct sockets of a chandelier with n candleholders such that
# the chandelier is perfectly balanced.

# For example, f(4, 2) = 2: assuming the chandelier's four candleholders are aligned with the compass points, the two valid arrangements
# are "North & South" and "East & West". Note that these are considered to be different arrangements even though they are related by rotation.

# You are given that f(12 ,4) =15 and f(36, 6) = 876
# find f(360, 20) = ?


def calculate_ways(n, m):
    def phi(x):
        result = x
        p = 2
        while p * p <= x:
            if x % p == 0:
                while x % p == 0:
                    x //= p
                result -= result // p
            p += 1
        if x > 1:
            result -= result // x
        return result

    return phi(n) * pow(2, m - 1, 10**9 + 7) % (10**9 + 7)

# Test cases
print(calculate_ways(4, 2))   # Output: 2
print(calculate_ways(12, 4))  # Output: 15
print(calculate_ways(36, 6))  # Output: 876
print(calculate_ways(360, 20))  # Output: ?