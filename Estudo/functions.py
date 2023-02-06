

def sum_hour(*hours):
    val = [0,0]

    for hour in hours:
        hour = hour.split(':')
        h = int(hour[0])
        m = int(hour[-1])
        
        val[0] += h
        val[1] += m
    
    if val[1] > 60:
        while val[1] > 60:
            val[1] -= 60
            val[0] += 1

    return f"{val[0]}:{val[1]}"


print(sum_hour('01:20','02:22','06:60'))
