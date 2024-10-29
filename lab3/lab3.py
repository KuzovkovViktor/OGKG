import numpy as np
import matplotlib.pyplot as plt
import math

# Параметри
canvas_size = (960, 960)
center_point = (480, 480)
alpha_deg = 10 * (0 + 1)
alpha_rad = math.radians(alpha_deg)

# Обчислення матриці обертання
cos_a, sin_a = math.cos(alpha_rad), math.sin(alpha_rad)
rotation_matrix = np.array([
    [cos_a, -sin_a],
    [sin_a, cos_a]
])

# Завантаження точок з файлу
points = []
with open('C:\\Users\Viktor\\Documents\\GitHub\\OGKG\\lab3\\DS0.txt') as file:
    for line in file:
        x, y = map(int, line.split())
        points.append((x, y))

# Афінне перетворення точок
transformed_points = []
for x, y in points:
    # Перенесення точки до (0,0), обертання, перенесення назад
    vec = np.array([x - center_point[0], y - center_point[1]])
    rotated_vec = rotation_matrix @ vec
    new_point = rotated_vec + np.array(center_point)
    transformed_points.append(new_point)

# Перетворення списків точок для візуалізації
original_x, original_y = zip(*points)
transformed_x, transformed_y = zip(*transformed_points)

# Налаштування полотна
plt.figure(figsize=(10, 10))
plt.xlim(0, canvas_size[0])
plt.ylim(0, canvas_size[1])
plt.gca().set_aspect('equal', adjustable='box')

# Відображення результату
plt.scatter(transformed_x, transformed_y, color='blue', s=10)
plt.title(f'Обертання навколо точки {center_point} на кут {alpha_deg}°')
plt.savefig('transformed_image.png')
plt.show()
