#defining the funtions
def km_to_m(a):
    return a * 1000

def c_to_f(a):
    return a * (9/5) + 32

def h_to_m(a):
    return a * 60
#creating loop for options
while True:
    print("\n" + "="*40)
    print("     🌟 SIMPLE UNIT CONVERTER 🌟\n                 ~Kanchan Maji")
    print("="*40)
    print("1. Kilometers ➝ Meters")
    print("2. Celsius ➝ Fahrenheit")
    print("3. Hours ➝ Minutes")
    print("4. Exit")
    print("="*40)

    option = int(input("👉 Choose an option(1-4): "))

    if option == 1:
        n = km_to_m(int(input("\n📥 Enter the value in Km: ")))
        print(f"✅ Result: {n} meters")

    elif option == 2:
        n = c_to_f(int(input("\n📥 Enter the value in °C: ")))
        print(f"✅ Result: {n} °F")

    elif option == 3:
        n = h_to_m(int(input("\n📥 Enter the value in Hours: ")))
        print(f"✅ Result: {n} minutes")

    elif option == 4:
        print("\n👋 Thanks for using the Converter. Goodbye!")
        print("="*40)
        break

    else:
        print("\n❌ Invalid Option! Please try again.")