import math

def mega_area(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2.0
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

def main():
    print("Vychislenie ploshchadi treugolnika po formule Gerona")
    a = float(input("Vvedite Vashu dlinu storony a: "))
    b = float(input("Vvedite Vashu dlinu storony b: "))
    c = float(input("Vvedite Vashu dlinu storony c: "))
    area = mega_area(a, b, c)
    print(f"Ploshchad treugolnika: {area:.5f}")

if __name__ == "__main__":
    main()