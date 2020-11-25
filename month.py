import matplotlib.pyplot as plt
import csv


sej = 350000
che = 660000
gon = 110000

year = range(0, 1000)
list_sej = [[]]
list_che = [[]]
list_gon = [[]]
main_list = [["Date", "Se-Jong", "Cheon-An", "Gong-Ju"]]
main_list.append(["2020-11-25", sej, che, gon])
month = range(0, 100 * 12)
cur_month = 11
cur_year = 2020
for i in month:
    #new_sej = round(sej * 0.92 + che * 0.01 + gon * 0.10 + 4800)
    new_sej = round((sej - sej * 0.05 * (1 / 12) - sej * 0.03 * (1 / 12))
            + che * 0.01 * (1 / 12) + gon * 0.10 * (1 / 12)) + 4800 / 12
    new_che = round((che - che * 0.01 * (1 / 12) - che * 0.01 * (1 / 12))
            + sej * 0.05 * (1 / 12) + gon * 0.05 * (1 / 12))
    new_gon = round((gon - gon * 0.10 * (1 / 12) - gon * 0.05 * (1 / 12))
            + che * 0.01 * (1 / 12) + sej * 0.03 * (1 / 12))
    sej_ratio = (new_sej / sej) * 100
    che_ratio = (new_che / che) * 100
    gon_ratio = (new_gon / gon) * 100
    sej = new_sej
    che = new_che
    gon = new_gon
    list_sej.append(["Se-Jong", i + 2020, sej])
    list_che.append(["Cheon-An", i + 2020, che])
    list_gon.append(["Gong-Ju", i + 2020, gon])
    main_list.append([str(cur_year) + "-" + str(cur_month) +"-25", sej, che, gon])
    cur_month += 1
    if (cur_month > 12):
        cur_month -= 12
        cur_year += 1



f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
for lst in main_list:
    wr.writerow(lst)
#for lst in list_sej:
    #wr.writerow(lst)
#for lst in list_che:
    #wr.writerow(lst)
#for lst in list_gon:
    #wr.writerow(lst)
f.close()
#plt.plot(year, people, "bo")
#plt.show()


