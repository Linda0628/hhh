## workshop 1 ====================================================================================
name = 'Bowen Zhang'
age = 24
birthday = '27th September'
lover = 'Linda'
college = 'UoE and UCC'
print(f'Hi, my name is {name}, and I am {age} years old, my birthday is {birthday}')
print(f'I love {lover}, my college is {college}')
print('just try how to PULL it into VScode')
print('just try how to PULL it into VScode from terminal')

name_1 = 'ZBW'
name_2 = 'Linda'
age_1 = 24
age_2 = 22
birthday_1 = '10th April'
birthday_2 = '28th June'
judge = age_1 < age_2
print(f'Is {name_1} younger than {name_2}? {judge}')


## workshop 2 ====================================================================================
# Task 1: (P, Q)-Fibonacci sequence with loop and function========================================
def new_fibo(p,q,n):
    fibo = [1,1]
    for i in range(2,n):
        fibo.append( p*fibo[i-2] + q*fibo[i-1] )
    return(fibo)
print( new_fibo(6,4,10) )

# Task 3 =========================================================================================
# （1） Elements up to n
'''''''''''''''
方法一
'''''''''''''''
def golomb_seq(n):
    '''
    Returns a list containing the elements
    of the Golomb sequence starting with
    G(1) = 1
    G(2) = 2
    and for i>2, G(i) is the number of times that i
    appears in the sequence.
    Returns all elements smaller than or equal to n.
    '''
    # Initialise G(1), G(2), and G(3) = 2 since 2 must appear twice (G(2) = 2)
    G = [1, 2, 2]
    # Append terms until G(n)
    for i in range(3, n+1):
        for j in range(G[i-1]):  # j:  0 到 G[i-1]-1
            # Append the number i, G(i) times
            G.append(i)
    return G 
g = golomb_seq(20) 
print(g)

'''''''''''''''
方法二
'''''''''''''''
def golomb_seq_2(n):
    '''
    Another possible solution, concatenating lists.
    '''
    # Initialise G(1), G(2), and G(3) = 2 since 2 must appear twice (G(2) = 2)
    G = [1, 2, 2]

    for i in range(3, n+1):
        # Concatenate the appropriate number of elements i
        G += G[i-1] * [i]

    return G
g = golomb_seq_2(20)
print(g)


# （2） First n elements
'''''''''''''''
方法一
'''''''''''''''
def golomb_seq_recur(n):
    '''
    Returns a list containing the first n elements of the
    Golomb sequence starting with G(1) = 1.
    Uses the recurrence relation given on oeis.org/A001462.
    '''
    G = [1]
    for i in range(1, n):
        G.append(1 + G[i - G[G[i-1]-1]])
    return G
g = golomb_seq_recur(20)
print(g)
'''''''''''''''
方法二
'''''''''''''''
import math
def golomb(n):
    '''
    Returns G(n), the nth element of the Golomb sequence
    calculated explicitly.
    '''
    phi = (1 + math.sqrt(5)) / 2                    # golden ratio
    Gn = round(phi**(2 - phi) * n**(phi - 1))       # explicit formula
    return Gn
    
g_expl = [1]
for i in range(2, 21):
    g_expl.append(golomb(i))

print(g_expl)
print(g[:20])

