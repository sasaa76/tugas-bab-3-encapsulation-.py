class Employee:
    def __init__(self, name=None, age=None, salary=None):
        self.__name = name
        self.__age = age
        self.__salary = salary
    
    # Metode Setter
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            print("Umur harus berupa bilangan bulat non-negatif")
    
    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary >= 0:
            self.__salary = salary
        else:
            print("Gaji harus berupa angka non-negatif")
    
    # Metode Setter
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_salary(self):
        return self.__salary


karyawan = Employee()

karyawan.set_name("Budi Santoso")
karyawan.set_age(30)
karyawan.set_salary(5000000)

print(f"Nama Karyawan: {karyawan.get_name()}")
print(f"Umur Karyawan: {karyawan.get_age()} tahun")
print(f"Gaji Karyawan: Rp {karyawan.get_salary():,}")

karyawan.set_salary(5500000)
print(f"Gaji Karyawan setelah kenaikan: Rp {karyawan.get_salary():,}")
