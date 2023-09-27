first = ["🥬", "🥬", "🥬"]
second = ["🥬", "🥬", "🥬"]
third = ["🥬", "🥬", "🥬"]
print(first)
print(second)
print(third)

print("Place the rabbit: 🐇")
place = int(input("Enter the number of row and column where you want put the 🐇: "))

if place == 11:
    first.remove("🥬")
    first.insert(0, "🐇")
    print(first)
    print(second)
    print(third)

elif place == 12:
    first.remove("🥬")
    first.insert(1, "🐇")
    print(first)
    print(second)
    print(third)

elif place == 13:
    first.remove("🥬")
    first.insert(2, "🐇")
    print(first)
    print(second)
    print(third)

elif place == 21:
    second.remove("🥬")
    second.insert(0, "🐇")
    print(first)
    print(second)
    print(third)

elif place == 22:
    second.remove("🥬")
    second.insert(1, "🐇")
    print(first)
    print(second)
    print(third)

elif place == 23:
    second.remove("🥬")
    second.insert(2, "🐇")
    print(first)
    print(second)
    print(third)

elif place == 31:
    third.remove("🥬")
    third.insert(0, "🐇")
    print(first)
    print(second)
    print(third)

elif place == 32:
    third.remove("🥬")
    third.insert(1, "🐇")
    print(first)
    print(second)
    print(third)

elif place == 33:
    third.remove("🥬")
    third.insert(2, "🐇")
    print(first)
    print(second)
    print(third)
