from typing import Any,List,Union
import random

def sum_1():
    sum_reuslt = sum([1,2,3]);
    print(f"sum([1,2,3]) is {sum_reuslt}")

def mysum(* numbers):
    output = 0
    for number in numbers:
        output += number
    return output

def mysum2(*numbers:int | float, init_value: int | float = 0) -> int | float:
    output = init_value
    for number in numbers:
        output += number
    return output
    

def my_avg_1(num_list:int | float) -> int | float:
    if not num_list:
        print("空列表")
        return 0
    total = sum(num_list)
    return total/len(num_list)

def my_avg_2(* numbers):
    if not numbers:
        print("空元组")
        return 0
    total = 0
    for number in numbers:
        total+=number
    return total / len(numbers)

def sum_obj_list(obj_list:list)-> int | float:
    total = 0
    for obj in obj_list:
        if not isinstance(obj,int|float):
            continue
        total += obj
    return total

def sum_obj_list_2(obj_list:List[Any]) -> Union[int,float]:
    # 对列表的数值进行求和，自动逃过非数值和波尔值
    total:Union[int,float] = 0
    for obj in obj_list:
        if isinstance(obj,bool) or not isinstance(obj,(int,float)):
            continue
        total += obj
    return total


if __name__ == "__main__":
    # sum_1();
    # print(f"mysum(10,20,30,40) is {mysum(10,20,30,40)}")
    # print(f"mysum(*[10,20,30,40]) is {mysum(*[10,20,30,40])}")
    # print(f"mysum2(*[1,2,3,4],4) is {mysum2(*[1,2,3,4],4)}")
    # number_list = (1,2,3,4,5)
    # print(f"my_avg_1 is {my_avg_1(number_list)}")
    # print(f"my_avg_2 is {my_avg_2(*number_list)}")
    more_list = [1,"2",3,4]
    total = sum_obj_list_2(more_list)
    print(f"sum_obj_list_2 is {total}")