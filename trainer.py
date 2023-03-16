with open("data.txt", "a+") as f:
    f.seek(0)
    data = f.read()
    data = data.split("\n")

    conversations = []
    for str in data:
        l = str.split("\t")
        conversations.extend((l[0], l[1]))
    print(conversations)   