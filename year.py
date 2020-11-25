import matplotlib.pyplot as plt
import csv


sej = 350000
che = 660000
gon = 110000

year = range(0, 10)
list_sej = [[]]
list_che = [[]]
list_gon = [[]]
main_list = [["Date", "Se-Jong", "Cheon-An", "Gong-Ju", "Sum", "Gap"]]
main_list.append(["2020-11-25", sej, che, gon, sej + che + gon, 0])
month = range(0, 100 * 12)
cur_month = 11
cur_year = 2020
for i in year:
    prev_sum = sej + che + gon
    new_sej = round(sej * 0.92 + che * 0.01 + gon * 0.10 + 4800)
    new_che = round(che * 0.98 + sej * 0.05 + gon * 0.05)
    new_gon = round(gon * 0.85 + che * 0.01 + sej * 0.03)
    new_sum = new_sej + new_che + new_gon
    sej_ratio = (new_sej / sej) * 100
    che_ratio = (new_che / che) * 100
    gon_ratio = (new_gon / gon) * 100
    sej = new_sej
    che = new_che
    gon = new_gon
    list_sej.append(["Se-Jong", i + 2020, sej])
    list_che.append(["Cheon-An", i + 2020, che])
    list_gon.append(["Gong-Ju", i + 2020, gon])
    cur_year += 1
    main_list.append([str(cur_year) + "-" + str(cur_month) +"-25", sej, che, gon, new_sum, new_sum - prev_sum])



f = open('output_year.csv', 'w', encoding='utf-8', newline='')
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
#plt.plot(year, main_list, "bo")
#plt.show()


