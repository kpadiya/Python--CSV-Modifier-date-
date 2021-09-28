import csv
import os
import shutil
import subprocess
from datetime import date

###RECHERCHE LE FICHIER CSV
for filename in os.listdir('/home/elastic/Licence'):
        if filename.endswith('.csv'):
                print('')

### OUVERTURE LE FICHIER CSV
text=open('/home/elastic/Licence/'+filename,'r')
with open('/home/elastic/Licence/'+filename,'r') as csv_file:
        csv_reader=csv.reader(csv_file)
        for line in csv_reader:
                print('')
        text = ''.join([i for i in text])
today = date.today()

### LA DATE SYSTEME DANS LE FICHIER
text = text.replace('No,','No,'+ today.strftime("%Y-%m-%d"))
text = text.replace('GB,','GB,'+ today.strftime("%Y-%m-%d"))
x=open('/home/elastic/csv/Terrena_VM-'+ today.strftime("%Y-%m-%d")+'.csv','w')
x.writelines(text)
print('Transformation of CSV file completed')
x.close()

###INSERTION DES DONNEES DANS ELASTIC
return_code = subprocess.call("/home/elastic/integration_elastic.sh")

###ARCHIVAGE DU FICHIER TRANSFORME
shutil.copyfile('/home/elastic/Licence/'+filename,'/home/elastic/Terrena_backup/'+filename)

###SUPPRESSION DU FICHIER DANS /Licence ET /csv
os.remove('/home/elastic/Licence/'+filename)
os.remove('/home/elastic/csv/Terrena_VM-'+ today.strftime("%Y-%m-%d")+'.csv')
