

def pig_latin(word : str) -> str:
    if word[0] in "aeiou":
        return f"{word}way"
    # word[1:]从索引1开始到word的结束
    return f"{word[1:]}{word[0]}way"

def pig_latin_upper(word : str) -> str:
    isAeiou = word[0] in "AEIOUaeopu" 
    if isAeiou:
        return f"{word}way".upper() if word[0].isupper() else f"{word}way"
    else:
        return f"{word[1:]}{word[0]}way".upper() if word[0].isupper() else f"{word[1:]}{word[0]}way"

def pig_lation_upper2(word : str) -> str:
    output_str = f"{word[1:]}{word[0]}way"
    if word[0] in 'AEIOUaeopu':
        output_str = f"{word}way"
    if word[0].isupper():
        output_str = output_str.upper()
    return output_str

def pig_lation_upper3(word : str) -> str:
    if not word:
        return ""
    vowels = "AEIOUaeopu"
    first = word[0]

    # 1.先检查是否元音，拼接词干
    if first in vowels:
        base = f"{word}way"
    else:
        base = f"{word[1:]}{first}way"

    # 2. 判断首字符大写    
    if first.isupper():
        return base.upper();
    return base

if __name__ == "__main__":
   # print(pig_latin("apython"))
   # 从abcdefgh第2位到第6位（不包含）的所有字符
   #s = 'abcdefgh'
   #print(s[2:6])
   # 设置步长2
   #print(s[2:6:2])
   # 从索引0开始，每步长2时，取值
   #print(s[::2]) 
   print(f"pig_latin_upper is {pig_latin_upper("Python")}" )
   print(f"pig_lation_upper2 is {pig_lation_upper2("Python")}")
   print(f"pig_lation_upper3 is {pig_lation_upper3("Python")}")




