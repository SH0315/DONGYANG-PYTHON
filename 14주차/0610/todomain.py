# todomain.py (나올수도)
from todolist import create_task, list_tasks, tasks

# 할 일 목록 작업
create_task(tasks, "청소하기")
create_task(tasks, "식료품 쇼핑하기")
create_task(tasks, "운동하기")

print("할 일 목록:")
list_tasks(tasks)
