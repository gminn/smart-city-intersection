import matplotlib.pyplot as plt

pic = plt.imread('google_map.PNG')
BBox = (-83.699663, -83.697951, 42.300584, 42.301483)

fig, ax = plt.subplots(figsize=(6,6))

ax.imshow(pic, extent=[BBox[0],BBox[1],BBox[2],BBox[3]])
ax.set_aspect(2)

ax.set_title('Map of Mcity intersection')

ax.scatter(-80.6985069, 42.3010583, c = 'k')

fig.savefig('Mcity_map1.png')
fig.show()
print('end')
