d = int(input('dias? '))
k = float(input('KM? '))
D = d * 60
K = k * 0.15
print('valor dias {:.2f}, valor km {:.2f} e valor total {:.2f}'.format(D, K, (D+K)))