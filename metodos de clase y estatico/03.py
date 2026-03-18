class ReportUtils:

    @staticmethod
    def format_username(username: str) -> str:
        clean_name = username.strip().title()
        return clean_name if clean_name else "Guest"
    
    @staticmethod
    def mask_email(email: str) -> str:
        if "@" not in email:
            return email
        
        user, domain = email.split("@")
        return f"{user[:3]}***@{domain}"

