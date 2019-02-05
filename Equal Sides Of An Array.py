def find_even_index(arr):
    size=len(arr)
    #global sum3
    sum3=1
    for j in range(0,size):
        sum1=sum(arr[:j])
        sum2=sum(arr[j+1:])
        sum3=sum1-sum2
        if sum3 == 0:
            break
        else:
            j=-1
    return j
