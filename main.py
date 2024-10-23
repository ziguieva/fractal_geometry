import mandelbrot
import julia
import sierpinski_triangle
import koch_curve
import fractal_tree
import dragon_curve
import cantor_set
import visualisation

def menu():
    print("Choose a fractal to generate:")
    print("1. Mandelbrot Set")
    print("2. Julia Set")
    print("3. Sierpinski Triangle")
    print("4. Koch Curve")
    print("5. Fractal Tree")
    print("6. Dragon Curve")
    print("7. Cantor Set")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        data = mandelbrot.generate_mandelbrot()
    elif choice == '2':
        data = julia.generate_julia()
    elif choice == '3':
        data = sierpinski_triangle.generate_sierpinski()
    elif choice == '4':
        data = koch_curve.generate_koch()
    elif choice == '5':
        data = fractal_tree.generate_tree()
    elif choice == '6':
        data = dragon_curve.generate_dragon()
    elif choice == '7':
        data = cantor_set.generate_cantor()
    else:
        print("Invalid choice.")
        return

    visualisation.show_fractal(data)

if __name__ == "__main__":
    menu()
