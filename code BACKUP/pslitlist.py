lists = [[]]
test_list = ['-31115.00', '18719.80', '1497.60', '1497.60', '5400.00', '4000.00', '-1000.00', '500.00', '40.00', '460.00']
size = len(test_list)
idx_list = [idx for idx, val in
            enumerate(test_list) if float(val)<0]
print(idx_list)
  
res = [test_list[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))]
  
# print result
print("The list after splitting by a value : " + str(res))