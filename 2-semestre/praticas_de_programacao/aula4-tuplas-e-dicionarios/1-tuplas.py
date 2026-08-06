#
#^ TUPLAS
minha_tupla = (1, 2, 3)


#^ EXEMPLOS
lat_long_senac = (-23.668559, -46.702251) #coordenada geográfica
vermelho_rgb = (255, 0, 0)  #rgb
amarelo_cmyk = (0, 0, 100, 0)  #cmky

print(vermelho_rgb[0])	# Saída: 255
print(amarelo_cmyk[2])	# Saída: 100


info_cor = ("Vermelho", (255, 0, 0), "#FF0000", True)
print(info_cor) # Saída: ('Vermelho', (255, 0, 0), '#FF0000', True)


r, g, b = vermelho_rgb
print(f'R: {r}, G: {g}, B: {b}')	# Saída: R: 255, G: 0, B: 0


vermelho_rgb[0]  =  200	# Isso resultará em um erro!
