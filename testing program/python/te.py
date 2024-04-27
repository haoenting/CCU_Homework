def getOneBits(n):
    # Write your code here
    count = 0
    elements = []
    while n != 0:
        if n % 2 == 1:
            count += 1
            elements.append(1)
        else:
            elements.append(0)
        n /= 2
    
    elements = elements.reverse()
    total = 1
    print(count)
    for element in elements:
        if element == 1:
            print(total)
        total += 1
        
getOneBits(10)