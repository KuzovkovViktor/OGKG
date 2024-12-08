import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from skimage.measure import label, regionprops

# Зчитування датасету з файлу
def read_dataset(file_path):
    points = np.loadtxt(file_path, dtype=int)
    print(f"Завантажено {len(points)} точок.")
    return points

# Побудова зв'язаних областей
def find_connected_components(points):
    grid_size = (np.max(points[:, 1]) + 1, np.max(points[:, 0]) + 1)
    grid = np.zeros(grid_size, dtype=int)
    grid[points[:, 1], points[:, 0]] = 1

    labeled_grid = label(grid)
    regions = regionprops(labeled_grid)
    print(f"Знайдено {len(regions)} зв'язаних областей.")
    
    # Демонстрація областей
    plt.figure(figsize=(10, 6))
    plt.imshow(labeled_grid, cmap="tab20")
    plt.title("Зв'язані області")
    plt.colorbar()
    plt.show()
    
    return regions

# Обчислення центрів ваги
def calculate_centroids(regions):
    centroids = []
    for region in regions:
        centroids.append(region.centroid[::-1])  # x, y
    centroids = np.array(centroids)
    print(f"Обчислено центри ваги: {centroids}")
    return centroids

# Побудова діаграми Вороного
def plot_voronoi(centroids, points, output_file):
    plt.figure(figsize=(960 / 96, 540 / 96), dpi=96)
    
    # Побудова діаграми Вороного
    vor = Voronoi(centroids)
    voronoi_plot_2d(vor, show_vertices=False, line_colors='blue', line_width=1.5, point_size=0)
    
    # Нанесення точок центроїдів
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=20, label='Centroids')
    
    # Нанесення точок датасету
    plt.scatter(points[:, 0], points[:, 1], c='black', alpha=0.1, s=1, label='Dataset points')
    
    # Легенда
    plt.legend()
    plt.axis('equal')
    plt.title("Діаграма Вороного")
    plt.show()
    
    # Збереження зображення
    plt.savefig(output_file)
    print(f"Діаграма Вороного збережена у файл {output_file}")

# Основна програма
def main():
    input_file = "C:\gnida\ogkg\DS0.txt"
    output_file = "output.png"
    
    # Зчитування і обробка датасету
    points = read_dataset(input_file)
    regions = find_connected_components(points)
    centroids = calculate_centroids(regions)
    
    # Побудова і збереження графіки
    plot_voronoi(centroids, points, output_file)

if __name__ == "__main__":
    main()
