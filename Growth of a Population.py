def nb_year(p0, percent, aug, p):
    population=p0
    n=0
    while population < p:
        population=population*(percent/100+1)+aug
        n+=1
    return n
