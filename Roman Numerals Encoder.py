def solution(n):
    value = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    symbol = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
    romanNum = ""
    for i in range(len(value)):
      count = int(n / value[i])
      romanNum += symbol[i] * count
      n -= value[i] * count
    return romanNum
