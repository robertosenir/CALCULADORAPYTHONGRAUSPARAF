def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

temp = float(input("Digite a temperatura: "))
escala = input("Digite a escala original (C/F): ").strip().upper()

if escala == "C":
    print(f"{temp}°C = {celsius_para_fahrenheit(temp):.2f}°F")
elif escala == "F":
    print(f"{temp}°F = {fahrenheit_para_celsius(temp):.2f}°C")
else:
    print("Escala inválida.")

