# Considere dois países: A com 80.000 habitantes e taxa de crescimento anual de 3%, e B com 200.000 habitantes e taxa de 1,5%. 
# Determine quantos anos serão necessários para que a população do país A ultrapasse a população do país B.

pais_a = 80000
pais_b = 200000
contador = 0

while pais_a <= pais_b:
    pais_a = pais_a + (pais_a * 0.03)
    pais_b = pais_b + (pais_b * 0.015)
    contador += 1
    print (f"Ano: {contador}. País A = {pais_a} habitantes. País B = {pais_b} habitantes")

print()
print(f"Foram necessários {contador} anos para que o país A ultrapassasse a população do país B.")
