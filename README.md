# projetoConfeitaria-backend

# ======= Entidades =====
# Cliente
# GET    /clientes/{ID}
# GET    /clientes?{atributo}={valor}
# POST   /clientes/
# PUT    /clientes/
# DELETE /clientes/{ID}
# ======================

# ======= Produto =======
# GET    /produtos/{ID}
# GET    /produtos?{atributo}={valor}
# POST   /produtos/
# PUT    /produtos/
# DELETE /produtos/{ID}
# =======================

# ======= Pedido =======
# GET    /pedidos/{ID}
# GET    /pedidos?{atributo}={valor}
# POST   /pedidos/
# PUT    /pedidos/
# DELETE /pedidos/{ID}
# ======================

# ======= Fichas Técnicas =======
# GET    /fichas_tecnicas/{ID}
# GET    /fichas_tecnicas?{atributo}={valor}
# POST   /fichas_tecnicas/
# PUT    /fichas_tecnicas/
# DELETE /fichas_tecnicas/{ID}
# ===============================

# ======= Ingredientes =======
# GET    /ingredientes/{ID}
# GET    /ingredientes?{atributo}={valor}
# POST   /ingredientes/
# PUT    /ingredientes/
# DELETE /ingredientes/{ID}
# ============================

# ======= FichasTécnicas-Ingredientes =======
# GET    /fichas_ingredientes/{ID?} Qual ID? BD terá um ID adicional pra isso?
# GET    /fichas_ingredientes?{atributo}={valor}
# POST   /fichas_ingredientes/
# PUT    /fichas_ingredientes/
# DELETE /fichas_ingredientes/{ID?} Qual ID? BD terá um ID adicional pra isso?
# ===========================================

# Considerações
# Endpoints GET podem ter retornos muito complexos.
# Exemplo: Cliente com informações de pessoa + endereços + telefones + preferencias
# Eventualmente podemos criar endpoints mais específicos para a mesma entidade.
# Exemplos:
# /cliente/{ID}/pessoal
# /cliente/{ID}/enderecos
# /cliente/{ID}/telefones
# /cliente/{ID}/preferencias
#
# Pode ser necessário versionar os endpoints
# API Versioning: https://www.freecodecamp.org/news/how-to-version-a-rest-api/
#
# Gerar documentação automaticamente parece ser o ideal
# https://swagger.io/blog/api-development/automatically-generating-swagger-specifications-wi/