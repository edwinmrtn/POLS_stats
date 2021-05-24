import requests
import json 
ratioPols = [0]*12
import csv
with open('dootmove.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        adressWallet = row[1]
        chain = row[2]
        test='0x0037dd60f7a4393587b6dce2c6dddd4508d38e32'
        r =requests.get('https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x83e6f1E41cdd28eAcEB20Cb649155049Fac3D5Aa&address='+adressWallet+'&tag=latest&apikey=BXZ97TIX629AHNSPDI3ICWFCRUTRJUMK2Q')
        jsonTab = r.json()
        
        nbrPols = int(jsonTab["result"])*0.000000000000000001


        if nbrPols < 250:
            ratioPols[0]=ratioPols[0]+1
        elif nbrPols < 270:
            ratioPols[1]=ratioPols[1]+1
        elif (nbrPols < 500):
            ratioPols[2]=ratioPols[2]+1
        elif (nbrPols < 750):
            ratioPols[3]=ratioPols[3]+1
        elif (nbrPols < 1000):
            ratioPols[4]=ratioPols[4]+1
        elif (nbrPols < 1500):
            ratioPols[5]=ratioPols[5]+1
        elif (nbrPols < 2000):
            ratioPols[6]=ratioPols[6]+1
        elif (nbrPols < 2500):
            ratioPols[7]=ratioPols[7]+1
        elif (nbrPols < 3000):
            ratioPols[8]=ratioPols[8]+1
        elif (nbrPols < 4000):
            ratioPols[9]=ratioPols[9]+1
        elif (nbrPols < 30000):
            ratioPols[10]=ratioPols[10]+1
        elif (nbrPols < 100000):
            ratioPols[11]=ratioPols[11]+1
        print(nbrPols)
        print(ratioPols)

