nombre_usuario = input("Como te llamas?")
nombre_usuario_normalizado = nombre_usuario.strip().lower().replace(" ", ".")
nombre_empresa = input("Donde trabajas/estudias?")
extension_dominio = ".com.mx"
dominio_email_normalizado = nombre_empresa.strip().lower() + extension_dominio
Email = f"{nombre_usuario_normalizado}@{dominio_email_normalizado}"
print(Email)

