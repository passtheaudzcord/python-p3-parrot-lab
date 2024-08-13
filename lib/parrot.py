def parrot(message=None):
    if message is None:
        print("Squawk!")
        return "Squawk!"
    else:
        print(message)
        return message
