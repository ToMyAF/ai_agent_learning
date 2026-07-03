from typing import Optional,Union,List,Dict

# 1.基础类型古提示（对标C#：string name，int age）
def greet(name:str,age:int) -> str:
    return f"{name} is {age} years old"

# 2.Optional = 可空类型（对标C#：string?）
def get_user(id:int) -> Optional[str]:
    if id == 1:
        return "Alice"
    return None # 允许返回None

# 3.Union = 多种类型（对标C#：object 或 联合类型）
def parse_value(value:Union[str,int]) ->str:
    return str(value)

# python 3.10+ 新语法（对标C#的string | null
def parse_value_v2(value:str | int) -> str:
    return str(value)

# 4. List 和 Dict（对标C#：List<string>，Dictionary<string,int>)
def process_items(items:List[str],mapping:Dict[str,int]) -> List[int]:
    return [mapping[item] for item in items if item in mapping]

# 测试运行
if __name__ == "__main__":
    print(greet("Bob",30))
    print(get_user(1))
    print(parse_value(123))
    print(process_items(["a","b"],{"a":1,"b":2}))
