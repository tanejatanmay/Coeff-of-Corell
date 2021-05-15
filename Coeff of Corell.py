ls1 = []
ls2 = []

while True:
    a1 = input("Enter the elements of your first list (Type END if you want to stop adding elements) : ")
    if a1 != "END":
        a1 = float(a1)
        ls1.append(a1)
    else:
        break

print("YOUR FIRST LIST IS:", ls1)


while True:
    a2 = input("Enter the elements of your second list (Type END if you want to stop adding elements) : ")
    if a2 != "END":
        a2 = float(a2)
        ls2.append(a2)
    else:
        break

print("YOUR SECOND LIST IS:", ls2)


if len(ls1) == len(ls2):
    def cor(ls1,ls2):
            mean_ls1 = sum(ls1) / len(ls1)
            mean_ls2 = sum(ls2) / len(ls2)

            num_XY = []
            den_ls1_sq = []
            den_ls2_sq = []
            X = []
            Y = []
            order = 0
            
            for x in ls1:
                t1 = x - mean_ls1
                v1 = t1 ** 2
                X.append(t1)
                den_ls1_sq.append(v1)
                

            for y in ls2:
                t2 = y - mean_ls2
                v2 = t2 ** 2
                Y.append(t2)
                den_ls2_sq.append(v2)
                

            while order < len(ls1):
                XY = X[order] * Y[order]
                num_XY.append(XY)
                order = order + 1


            sum_XY = sum(num_XY)
            sum_X2 = sum(den_ls1_sq)
            sum_Y2 = sum(den_ls2_sq)


            correl = (sum_XY) / ((sum_X2 * sum_Y2) ** 0.5)
            return(correl)
                
    print("The Coefficient of Correlation is:", cor(ls1,ls2))
else:
    print("The length of the two lists is not the same. Hence, Coefficient of Correlation cannot be calculated.")
