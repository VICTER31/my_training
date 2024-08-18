
def get_password(n):
    password = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if n%(i+j)==0:
                if i<j:
                    password.append(i)
                    password.append(j)
    return password

result1 = get_password(20)
print(*result1, sep='')