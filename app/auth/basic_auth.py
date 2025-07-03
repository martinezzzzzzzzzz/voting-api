from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    print("DEBUG - Username recibido:", credentials.username)
    print("DEBUG - Password recibido:", credentials.password)

    correct_username = "admin"
    correct_password = "secret"

    if not (
        secrets.compare_digest(str(credentials.username), correct_username)
        and secrets.compare_digest(str(credentials.password), correct_password)
    ):
        print("DEBUG - Credenciales inválidas")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    print("DEBUG - Autenticación exitosa")
    return credentials.username
