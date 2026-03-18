class FinanceTools:
    @staticmethod
    def calculate_tax(amount: float, tax_rate: float) -> float:
        if tax_rate < 0 or tax_rate > 100:
            print("La tasa de impuesto debe ser entre 0 y 100")
            return amount
        return amount + (amount * (tax_rate / 100))
    
    @staticmethod
    def is_eligible_for_discount(purchase_count : int, total_spent : float) -> bool:
        if (purchase_count > 10 and total_spent > 500) or total_spent > 2000:
            return True
        return False
