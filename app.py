import matplotlib.pyplot as plt


sej = 350000
che = 660000
gon = 110000

year = range(0, 100)
list_sej = []
list_che = []
list_gon = []
for i in year:
    new_sej = sej * 0.92 + che * 0.01 + gon * 0.10 + 4800
    new_che = che * 0.98 + sej * 0.05 + gon * 0.05
    new_gon = che * 0.01 + sej * 0.03 + gon * 0.85
    sej_ratio = (new_sej / sej) * 100
    che_ratio = (new_che / che) * 100
    gon_ratio = (new_gon / gon) * 100
    sej = new_sej
    che = new_che
    gon = new_gon
    list_sej.append(sej)
    list_che.append(che)
    list_gon.append(gon)

#plt.plot(year, people, "bo")
#plt.show()


