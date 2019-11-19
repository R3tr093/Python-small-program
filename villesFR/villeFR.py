import csv

from collections import namedtuple

Ville = namedtuple("Ville","nom lat lng nbhab surf dens")

print(" === > Lecture des villes françaises " )

lectcsv = csv.reader(open('villes_france.csv',encoding="utf-8"))

villes = []

nbVilles = 0

for items in lectcsv:
    nbVilles+= 1
    cp = items[8].split('-')
    dept = int(cp[0][:2])

    if not 1 <= dept <= 95:
    
        continue

    hab = int(items[16])


    if hab == 0:
        continue

    n = items[5]
    surf = float(items[18])
    lat = float(items[20])
    lng = float(items[19])

    v = Ville(n,lat,lng,hab,surf, hab / surf)
    villes.append(v)

print("Nombres des villes françaises concernées : ", len(villes), "sur", nbVilles)


print(" === > 10 Villes par densité croissantes " )

villes.sort(key=lambda x: x.dens)

from pprint import pprint 

pprint(villes[:10])

for v in villes:
    print("\n" + v.nom + " | densité : " + str(v.dens) + "\n")

input(" Appuyez sur enter ...")



print("\n  ==== BREAK === \n")


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np



carte = Basemap(projection='stere', lat_0=46.60611, lon_0=1.87528,resolution='l', llcrnrlon=-5, urcrnrlon=11, llcrnrlat=41, urcrnrlat=51)


carte.drawcoastlines(linewidth=0.25)
carte.drawcountries(linewidth=0.25)
carte.fillcontinents(color='#CAAF68', lake_color='#D3FFFF')
carte.drawmapboundary(fill_color='#D3FFFF')

carte.drawmeridians(np.arange(0, 360, 2), linewidth=0.1)
carte.drawparallels(np.arange(-90, 90, 2), linewidth=0.1)
plt.title('Prout !')

for v in villes[:200]:
  
    x, y = carte(v.lng, v.lat)
    carte.plot(x, y, marker='o', color='Red', markersize=3)


plt.show()    
