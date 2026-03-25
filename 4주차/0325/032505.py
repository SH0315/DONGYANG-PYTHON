# While 문
week = [6700, 6500, 7000, 12000, 5000, 1000, 3450]
weekname = ["월", "화", "수", "목", "금", "토", "일"]
#최대로 많이 걸은 걸음수
maxWeek = max(week)
maxIndex = week.index(maxWeek)
maxWeekName = weekname[maxIndex]
print(f"최대 도보수는 {maxWeek} 이고 {maxWeekName}요일 입니다")

#평균값
print(f"평균 도보수는 {sum(week) / len(week)} 입니다")

#6000보 이상인 요일 구하기
for n in range (len(week)) :
    if week[n] >= 6000:
        print(f"{weekname[n]}요일: {week[n]}보")






