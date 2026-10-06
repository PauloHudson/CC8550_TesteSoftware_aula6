def isento(pcd, valor_compra, cadastro_app, minutos):
	if pcd:
		return True
	if minutos <= 240 and (valor_compra >= 150.00 or cadastro_app):
		return True
	return cadastro_app
