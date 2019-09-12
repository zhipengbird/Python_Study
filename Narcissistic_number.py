def Narcissistic(num):
    length = len(str(num))
    count = length    
    num_sum = 0    
    while count:        
        num_sum += ((num // 10 ** (count - 1)) % 10) ** length     
        count -= 1    
    else:       
        if num_sum == num:            
            print("%d is %d bit narcissistic_number" % (num, length))
        else: 
            pass                       

if __name__ == '__main__':
    for i in range(100,1000000):
        Narcissistic(i)