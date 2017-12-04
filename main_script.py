from persistence_diagram import *
from discrete_function import *
import random


def display_2_diagrams(diag1, diag2):
    x1, y1, x2, y2 = [[], [], [], []]
    for p in diag2.points:
        x1.append(p[0])
        y1.append(p[1])
    for p in diag1.points:
        x2.append(p[0])
        y2.append(p[1])

    y_max = max(np.max(y1), np.max(y2)) + 1
    line = np.arange(0, y_max, 0.1)

    plt.plot(x1, y1, 'rs', x2, y2, 'bs', line, line, 'g')
    plt.axis([0, y_max, 0, y_max])
    plt.show()


if __name__ == "__main__":
    high = 10
    diag1 = Persistence_diagram(high = high)
    n_points = 5
    for exp in range(10):
        for i in range(n_points):
            y = high * random.random()
            x = y * random.random()
            diag1.add_point([x, y])

        kernel_vals = []
        ds = []
        distances = [0, 0.1, 0.2, 0.3, 0.4, .5, .6, .7, .9, 1.2, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6]
        for d in distances:
            d = np.abs(d+random.random())
            ds.append(d)
            diag2 = diag1.create_close_diagram(distance = d)
            # display_2_diagrams(diag1, diag2)

            sigma = .2
            val = 2*np.sqrt(np.pi)* sigma * diag1.kernel_value(diag2, sigma=sigma)
            norm1 = 2*np.sqrt(np.pi)* sigma * diag1.kernel_value(diag1, sigma=sigma)
            norm2 = 2*np.sqrt(np.pi)* sigma * diag2.kernel_value(diag2, sigma=sigma)
            kernel_vals.append(norm1 + norm2 - 2*val)
        plt.plot(ds, kernel_vals, 'b.')
    plt.show()
