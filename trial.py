AVO= 6.02e+23
PLANCK = 6.626e-34
LIGHT_SPEED = 3.0e+8

while True:
    wavelength = float(input("\nEnter wavelength: "))
    wavenumber = (1e+9)/wavelength
    print(wavenumber)
    energy = AVO * PLANCK * LIGHT_SPEED * wavenumber * 0.001
    print(f"\nLFSE: {energy}")
    print("\n")
