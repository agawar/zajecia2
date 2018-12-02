def funkcjaAcermana(m,n):

    if m==0:
        A = n + 1
    elif m > 0 & n == 0:
        m = m - 1
        n = 1
        A = funkcjaAcermana(m,n)
    elif m > 0 & n > 0:
        n = funkcjaAcermana(m, n-1)
        m = m - 1
        A = funkcjaAcermana(m,n)

    print(A)

funkcjaAcermana(0,1)

