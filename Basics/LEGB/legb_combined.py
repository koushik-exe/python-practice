# LEGB Combined - All 4 levels in one code

city = "Coimbatore"        # G - Global

def company():
    company_name = "GenZ"  # E - Enclosing

    def employee():
        employee_name = "Koushik"   # L - Local
        print(f"{employee_name} works in {company_name} in {city}")
        # print() is B - Built in

    employee()

company()