from bs4 import BeautifulSoup
import csv
from difflib import SequenceMatcher
import codecs
import sys
import os
import pathlib



files = [f for f in pathlib.Path().glob("xmls/*.xml")]
fqualis = open("batual.csv", "r");
qualis = csv.reader(fqualis)

sep = "$" 
for pesq in files:
	with open(pesq.resolve(), 'r',encoding="latin-1") as f:
	    data = f.read()
 
	Bs_data = BeautifulSoup(data, "xml")
 
	artigosg = Bs_data.find_all('ARTIGOS-PUBLICADOS')

	artigos = Bs_data.find_all('ARTIGO-PUBLICADO')
        
	nome = str(pesq)
	nome = nome.replace("xmls/","").replace(".xml","")
	for t in artigos:
		dadosB = t.find_all("DADOS-BASICOS-DO-ARTIGO");
		ano = dadosB[0].get("ANO-DO-ARTIGO")
		ano = int(ano)
		if(ano >= 2019):
			print(nome,end=sep)
			print(t, end=sep) 
			issn = t.find_all("DETALHAMENTO-DO-ARTIGO")
			issn = issn[0].get("ISSN")
			issn = issn[:4] + '-' + issn[4:]
			issnf = 0
			for q in qualis:
				ql = str(q[0]).strip().lower()
				s = SequenceMatcher(None, issn, ql)
				if(ql == issn):
					print(q[3],end=sep)
					issnf = 1
					break;
			print()
			fqualis.seek(0) 
			

 
