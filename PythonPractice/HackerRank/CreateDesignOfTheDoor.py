# Variant 1
def create_design_of_the_door(N, M):
    sym = ".|."
    word = "WELCOME"
    dif = "-"
    j = 1
    for i in range(0, M):
        if i != N:
            if i == (N-1)/2:
                print(word.center(M, dif))
                j += - 25
            elif N-i > (N+1)/2:
                print((sym*j).center(M, dif))
                j += 2
            elif N-i < (N+1)/2:
                print((sym*j).center(M, dif))
                j += - 2
        else:
            break


# Variant 2
def create_design_of_the_door2(N, M):
    sym_1, sym_2, central_word = ".|.", "-", "WELCOME"
    pattern = [(sym_1*(2*i+1)).center(M, sym_2) for i in range(0, M)]
    print("\n".join(pattern[:int(N/2)] + [central_word.center(M, sym_2)] + pattern[int(N/2)-1::-1]))


N, M = map(int, input().split())
create_design_of_the_door2(N, M)





