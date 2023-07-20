def get_badge(donations):
    if donations <= 3:
        return "BRONZE"
    elif donations <= 6:
        return "SILVER"
    else:
        return "GOLD"

# Input number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    donations = int(input())
    badge = get_badge(donations)
    print(badge)
