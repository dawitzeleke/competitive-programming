def countingSort(arr):
    n= len(arr)
    freq_arr=[0]*100
    for num in arr:
        freq_arr[num]+=1
        
    return freq_arr

