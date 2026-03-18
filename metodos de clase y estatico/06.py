class DatabaseConnection:
    host = "localhost"

    def __init__(self,user: str, password: str):
        self.user = user
        self.password = password
    
    @classmethod
    def set_host(cls, new_host: str) -> None:
        cls.host = new_host
    
    @classmethod
    def create_production_connection(cls,user: str) -> 'DatabaseConnection':
        cls.set_host("192.168.1.100")
        return cls(user, "holaaa")
    
    def get_connection_info(self) -> str:
        return f"Conectando a {self.host} con usuario {self.user}"