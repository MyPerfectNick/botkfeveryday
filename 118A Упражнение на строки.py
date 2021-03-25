s = input().lower().replace("a", "").replace("o", "").replace("y", "").replace("e", "").replace("u", "").replace("i", "")
print("." + ".".join(list(s)))
