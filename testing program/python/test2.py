# 1. 按照所需時間排序
# 2. 找預約時間比較早的
# 3. 超過30分鐘就跳過
# 4. 結束時間要晚於12.前(360)

# 顧客人數、按摩師數量
customers, masseurs = map(int, input().split(','))
# 各顧客的服務時間
service_times = list(map(int, input().split(',')))
# 各顧客的預約時間
reserve_times = list(map(int, input().split(',')))
# 各顧客的服務營收
earn_each_customer = list(map(int, input().split(',')))

# 按照服務時間排序
# 這邊使用insertion sort，因為我猜測資不會超過30個
for count in range(1, customers):
    key = service_times[count]
    key2 = reserve_times[count]
    key3 = earn_each_customer[count]
    j = count - 1

    while j >= 0 and key < service_times[j]:
        service_times[j + 1] = service_times[j]
        reserve_times[j + 1] = reserve_times[j]
        earn_each_customer[j + 1] = earn_each_customer[j]
        j = j - 1

    service_times[j + 1] = key
    reserve_times[j + 1] = key2
    earn_each_customer[j + 1] = key3

# 按照預約時間排序
key = service_times[0]
index = 0
for count in range(1, customers):
    if service_times[count] != key:
        for count2 in range(index + 1, count):
            key1 = reserve_times[count2]
            key2 = service_times[count2]
            key3 = earn_each_customer[count2]
            j = count2 - 1

            while j >= index and key1 < reserve_times[j]:
                service_times[j + 1] = service_times[j]
                reserve_times[j + 1] = reserve_times[j]
                earn_each_customer[j + 1] = earn_each_customer[j]
                j = j - 1

            reserve_times[j + 1] = key1
            service_times[j + 1] = key2
            earn_each_customer[j + 1] = key3

        index = count
        key = service_times[count]

# 初始化收入
sum = 0
total = 0
# 初始化按摩師時間
masseur = [0]*masseurs
# 每個按摩師都先配一個
for count in range(masseurs):
    masseur[count] += service_times[count] + reserve_times[count]
    sum += earn_each_customer[count]
    total += 1
# 接著看
for count in range(masseurs, customers):
    min = 360  # 一定在12點之前
    num = 0
    for count2 in range(masseurs):
        if masseur[count2] < min:  # 找到結束時間最短的
            num = count2
            min = masseur[count2]
    # 如果不用等超過半小時
    if (masseur[num] - reserve_times[count]) <= 30:
        # 如果超過12點
        if(masseur[num] + service_times[count] > 360):
            break
        masseur[num] += service_times[count]
        sum += earn_each_customer[count]
        total += 1

print(total, sum, sep=',')
