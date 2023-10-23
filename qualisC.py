import csv
from difflib import SequenceMatcher
 
# opening the CSV file
reader = csv.reader(open("artigosFull.csv", "r"), delimiter='$')
f = open("qualisFull.csv", "r");
qualis = csv.reader(f)
print("staring")
# displaying the contents of the CSV file
for lines in reader:
       for itp in lines:
         print(str(itp),end='');
           
       qac = ""
       qacfull = ""
       if( len(lines) == 2):
         itens = lines[1].split(".");
         if(len(itens) >3):
            for itt in itens:
                if(qac != ""):
                   print(" $ "+qac.strip())
                   print(" $ "+str(qacfull))
                   break

                ittl = str(itt)
                ittl = ittl.lower()
                ittl = ittl.strip()
                
                for q in qualis:
                    ql = str(q[1])
                    ql = ql.strip() 
                    ql = ql.lower()
                    ittl = str(itt)
                    ittl = ittl.lower()
                    ittl = ittl.strip()
                    s = SequenceMatcher(None, ittl, ql) 
                    if(s.ratio() > .8):
                       qac = q[3]
                       qacfull = q;
                    if(qac != ""):
                      try:
                         ittl = ittl.split(",")
                         for k in ittl:
                            k = str(k).strip()
                            k = k.lower()
                            s = SequenceMatcher(None, k, ql) 
                            if(s.ratio() > .8):
                               qac = q[3];
                               qacfull = q;
                               break
                      except:
                         a = "a"
                f.seek(0)   
