# Comandos de Git 

# Empezamos por "git init"
"""
git init 
"""
# Este comando inizializará nuestro directorio para hacerlo funcionar como un servidor/cliente de git.
#------------------------------------------------------------------------------------------------------

# Observar el repositorio con "git status"
"""
git status
"""
# Este comando nos va a permitir ver el estado del repositorio.
#------------------------------------------------------------------------------------------------------

# Preparar los cambios para el commit con "git add"
"""
git add
"""
# Este comando marca todos los archivos con cambios para empaquetarlos en un commit.
# Esto se llama "track", "tracear" o "traquear" los cambios.
#------------------------------------------------------------------------------------------------------

# Añadir un cambio con "git commit"
"""
git commit
"""
# Este comando empaqueta y almacena un cambio en la rama principal.
#------------------------------------------------------------------------------------------------------

# Ver el árbol de cambios con "git log"
"""
git log
"""
# Este comando nos permite ver por consola la lista de cambios en git
#------------------------------------------------------------------------------------------------------

# Abrir una rama con "git branch"
"""
git branch nueva-rama
"""
# Este comando crea una nueva rama en la que poder trabajar sin cambiar la rama principal.
#------------------------------------------------------------------------------------------------------

# Movernos a la nueva rama con "git checkout"
"""
git checkout nueva-rama
"""
# Este comando situa nuestra copia local en la nueva rama que hemos creado.
#------------------------------------------------------------------------------------------------------

# Mezclar ramas con "git merge"
"""
git checkout main

git merge nueva-rama
"""
# Primero nos movemos a la rama main.
# Luego nos traemos los cmabios de "nueva-rama" a la rama en la que estamos("main").
# FIN