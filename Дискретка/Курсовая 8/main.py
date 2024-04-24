import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_hypergraph(n, m, incidence_matrix):
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.set_xlim(-1, n + 2)
    ax.set_ylim(-1, m + 2)

    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'lime', 'pink', 'brown']

    vertex_colors = {}

    def available_colors(vertex):
        adjacent_colors = set()
        for i in range(m):
            if incidence_matrix[vertex][i] == 1:
                for v in range(n):
                    if incidence_matrix[v][i] == 1 and v in vertex_colors:
                        adjacent_colors.add(vertex_colors[v])
        return set(colors) - adjacent_colors

    for vertex in range(n):
        available = available_colors(vertex)
        vertex_colors[vertex] = next(iter(available)) if available else colors[len(vertex_colors) % len(colors)]

    # Проходим по каждому гиперребру и раскрашиваем вершины
    for j in range(m):
        # Находим все вершины, соединенные с текущим гиперребром
        vertices = [i for i in range(n) if incidence_matrix[i][j] == 1]
        # Определяем размер гиперребра в зависимости от количества вершин
        width = len(vertices)
        height = 1
        # Координаты левого верхнего угла гиперребра
        left_x = vertices[0] + 1
        left_y = j + 1
        # Добавляем гиперребро в качестве прямоугольника
        rect = patches.Rectangle((left_x, left_y), width, height, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)

        # Добавляем вершины внутри гиперребра
        for i, vertex in enumerate(vertices):
            circle = plt.Circle((left_x + i + 0.5, left_y + 0.5), 0.2, fc=vertex_colors[vertex])
            ax.add_artist(circle)
            ax.text(left_x + i + 0.5, left_y + 0.5, f'{vertex + 1}', ha='center', va='center')

    ax.set_aspect('equal')
    ax.set_axis_off()
    plt.show()

def create_matrix_input_window(n, m):
    root = tk.Tk()
    root.title("Input Matrix")

    entries = [[tk.Entry(root, width=5) for j in range(m)] for i in range(n)]

    for i in range(n):
        label = tk.Label(root, text=f"U{i+1}")
        label.grid(row=i+1, column=0)
        for j in range(m):
            entries[i][j].grid(row=i+1, column=j+1)
    for j in range(m):
        label = tk.Label(root, text=f"E{j+1}")
        label.grid(row=0, column=j+1)

    def get_matrix():
        matrix = [[int(entries[i][j].get()) for j in range(m)] for i in range(n)]
        root.destroy()
        return matrix

    submit_button = tk.Button(root, text="Submit", command=lambda: root.quit())
    submit_button.grid(row=n+1, column=0, columnspan=m+1)

    root.mainloop()

    incidence_matrix = get_matrix()
    return incidence_matrix

def main():
    n = int(simpledialog.askstring("Input", "Введите количество вершин (n):"))
    m = int(simpledialog.askstring("Input", "Введите количество ребер (m):"))

    incidence_matrix = create_matrix_input_window(n, m)

    print("Матрица инцидентности:")
    for row in incidence_matrix:
        print(row)

    draw_hypergraph(n, m, incidence_matrix)

if __name__ == "__main__":
    main()