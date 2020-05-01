import subprocess
   
for i in range(1,36,2):
    print(i)
    subprocess.run(["lp", "-o fit-to-page", "splitted/page-{}.pdf".format(i)])

input("press return to continue wiht the other side")

for i in range(2,38,2):
    print(i)
    subprocess.run(["lp", "-o fit-to-page", "splitted/page-{}.pdf".format(i)])
    
