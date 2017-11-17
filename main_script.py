from persistence_diagram import *


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
    for i in range(35):
        y = high * random.random()
        x = y * random.random()
        diag1.add_point([x, y])

    diag2 = diag1.create_close_diagram(distance = 0.5)
    display_2_diagrams(diag1, diag2)
