import subprocess
   
for i in range(1,63,2):
    print(i)
    subprocess.run(["lp", "/Users/fuat/Desktop/esad/coding/PrintingOnBothSideWithMyPrinter/splitted/page-{}.pdf".format(i)])

input("press return to continue wiht the other side")

for i in range(2,62,2):
    print(i)
    subprocess.run(["lp", "/Users/fuat/Desktop/esad/coding/PrintingOnBothSideWithMyPrinter/splitted/page-{}.pdf".format(i)])
    
