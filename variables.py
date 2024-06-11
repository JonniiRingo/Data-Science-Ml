def test(A, B):
    a = A
    b = B


    c = a
    a = b
    b = c

    return(a, b)

  

A = input()
B = input()

answer = test(A, B)

print(answer)
