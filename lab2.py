import matplotlib.pyplot as plt

plt.figure(figsize=(960/100, 540/100), dpi=100)

data = []
with open('C:/gnida/ogkg/DS0.txt', 'r') as file:
    for line in file:
        x, y = map(int, line.split())
        data.append((x, y))

x_coords, y_coords = zip(*data)

plt.scatter(x_coords, y_coords, color='blue', s=10)

plt.xlim(min(x_coords)-10, max(x_coords)+10)
plt.ylim(min(y_coords)-10, max(y_coords)+10)

plt.savefig('output.png')

plt.show()
