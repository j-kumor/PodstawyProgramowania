class C:
    def __init__(self, sectors):
        self.sectors = sectors  # A dictionary with sector names as keys and number of fans as values

    def m1(self, s, n):
        # If the sector exists, update its number of fans
        if s in self.sectors:
            self.sectors[s] = n
        else:
            # Otherwise, add a new sector with the given number of fans
            self.sectors[s] = n

    def m2(self, s):
        # Sum the number of fans in the sectors listed in the string 's'
        total_fans = 0
        for sector in s:
            if sector in self.sectors:
                total_fans += self.sectors[sector]
        return total_fans

# Sample usage
stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})

# Change the number of fans in sector 'G'
stadium.m1("G", 130)

# Calculate the sum of fans in sectors 'GD'
print(stadium.m2("GD"))  # Expected: 280

# Calculate the sum of fans in sectors 'KEJ'
print(stadium.m2("KEJ"))  # Expected: 110
