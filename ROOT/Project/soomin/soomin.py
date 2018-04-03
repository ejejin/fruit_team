
f = open("soomin_tree_cut_soomin_f_total_hist.txt", "r")

EN = 0
for line in f:
    _, _, fbin, entry = line.split()
    fbin = float(fbin)
    fbin = int(fbin)+1
    EN = EN + fbin*float(entry)

print(EN)


