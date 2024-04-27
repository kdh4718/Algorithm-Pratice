word_list = [list(input()) for i in range(5)]

for i in range(15):
    for j in range(5):
        try:
            print(word_list[j][i], end="")
        except:
            continue