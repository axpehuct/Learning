def log_action(filename, action):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(action + "\n")

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for data in f:
             print(data.strip())


log_action("test.txt", "hey")
read_file("test.txt")