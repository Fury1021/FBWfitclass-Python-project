def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1:
                    bestIdx = j
                elif blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j

        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]

    print("Process No.   Process Size	 Block no.")
    for i in range(n):
        print(i + 1, "	          	  ", processSize[i],
              end="		 ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == '__main__':
    blockSize = []
    processSize = []

    print("Enter block sizes. Type 'done' when finished:")
    while True:
        size_input = input()
        if size_input.lower() == 'done':
            break
        blockSize.append(int(size_input))

    print("Enter process sizes. Type 'done' when finished:")
    while True:
        size_input = input()
        if size_input.lower() == 'done':
            break
        processSize.append(int(size_input))

    m = len(blockSize)
    n = len(processSize)

    bestFit(blockSize, m, processSize, n)
