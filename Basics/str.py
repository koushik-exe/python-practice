import sys

if len(sys.argv) == 3:
    print(f"Word count: {len(sys.argv[1:])}")
    initials = sys.argv[1:]
    hot_box = []
    for word in initials:
        hot_box.append(word[0].upper())
    print("".join(hot_box))
else:
    print("Pleae provide the Correct Name")