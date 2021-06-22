# 이미 모두 정렬된 경우 종료

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
	n = len(a)
	for i in range(n - 1):
		exchange = 0
		for j in range(n - 1, i, -1):
			if a[j - 1] > a[j]:
				a[j - 1], a[j] = a[j], a[j - 1]
				exchange += 1
		if exchange == 0:
			break
