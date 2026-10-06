def isento(pcd, valor_compra, cadastro_app, minutos):
	if pcd:
		return True
	return minutos <= 240 and (valor_compra >= 150.00 or cadastro_app)
