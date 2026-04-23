class Employee:
    def __init__(self, name, anual_salary):
        self.name = name
        self.anual_salary = anual_salary

    @classmethod
    def from_string(cls, string_data: str) -> "Employee":
        name, salary_str = string_data.split("-")
        return cls(name, float(salary_str))

    @classmethod
    def from_monthly_salary(cls, name: str, monthly_salary: float) -> "Employee":
        return cls(name, monthly_salary * 12)
