# 평균을 구하는 함수.yumi
def f_avg(data):
    list = sum(data)/len(data)
    return list

#합계를 구하는 함수.baik
def f_sum(data):
  list = sum(data)
  return list

#오름차순으로 정렬해주는 함수.choi
def f_sort(list):
    list.sort()
    return list

#내림차순으로 정렬해주는 함수.ijioo
def f_desc(data):
    list = data.sort(reverse=True)
    return list


