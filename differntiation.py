# sample polynomial dictionary i am working with
# 5x^3+3x^2+7
sampleEquation = {
    "term1": (5, 3),  # 5x^3
    "term2": (3, 2),  # 3x^2
    "term3": (7, 0)   # 7 (constant)
}

def differntiate(polynomial):
    diffrentiatedPolynomial={}
    for term,values in polynomial.items():
        coefficient=values[0]
        power=values[1]
        coefficient*=power
        power-=1
        if (coefficient==0 and power==-1):
            continue
        diffrentiatedPolynomial.update({term:(coefficient,power)})
    return diffrentiatedPolynomial

print(differntiate(sampleEquation))