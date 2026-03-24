import time
station = {"송내" : 3, "중동" : 4, "부천":5}

for name, delay in station.items():
    print("→", end= " " )
    time.sleep(1)
    print("다음역은 " + name + "입니다")

    for j in range(1, delay + 1):
        print("▶" * j)
        time.sleep(1)
       
    print("이번역은 " + name + "입니다")


