new_moves = 0

def F(towers, i, moves):

    if i == 0:
        return F([towers[0]+1, towers[1],-1] + towers[2:], i, moves+1)
    elif i > 0 and F(towers[:i]+ [towers[i]+1, towers[i+1]-1] + towers[i+2:], i, moves + 1):
        return F(towers[:i]+ [towers[i]+1, towers[i+1]-1] + towers[i+2:], i, moves + 1)


def main():
    cases = int(input().strip())

    for _ in range(cases):

        inputs = list(map(int, input().strip().split()))
        print(inputs)

if __name__ == "__main__":
    main()