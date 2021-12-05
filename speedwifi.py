# import module
import os


# analyser les réseaux Wifi disponibles
os.system('cmd /c "netsh wlan montrer les réseaux"')

# saisir le nom du Wi-Fi
name_of_router = input('Entrez le nom/SSID du réseau Wifi auquel vous souhaitez vous connecter: ')

# se connecter au réseau wifi donné
os.system(f'''cmd /c "nom de connexion wlan netsh={name_of_router}"''')

print("Si vous n'êtes pas encore connecté, essayez à nouveau de vous connecter à un SSID précédemment connecté !")
##

import speedtest

#fonction qui obtient la vitesse de téléchargement en méga-octets par seconde
def get_metrics():
    st = speedtest.Speedtest()
    metrics = { "download" : round(st.download())/1e+6, "upload" : round(st.upload())/1e+6 }
    return metrics


#fonction qui trouve la vitesse de téléchargement moyenne en méga-octets par seconde
def looped_av(y):
    download_sum = 0
    upload_sum = 0
    for i in range(y):
        x = get_metrics()
        download_sum += x["download"]
        upload_sum += x["upload"]
        print(f'{i+1}. Dowload : {x["download"]}mb/s | Upload : {x["upload"]}mb/s')
    return {"avg_download" : download_sum/y, "avg_upload" : upload_sum/y}

#menu loop
while True:
    repeat = input('1, 2, 3 ou appuyez sur {ENTER} pour quitter\n>>>')
    if repeat == '1':
        #itération unique
        x = get_metrics()
        print(f'terminé, votre vitesse de téléchargement moyenne est {x["download"]}mb/s')
        print(f'terminé, votre vitesse de publier moyenne est{x["upload"]}mb/s')
    elif repeat == '2':
        #2 itérations et trouve la vitesse moyenne
        x = looped_av(2)
        print(f'terminé, votre vitesse de téléchargement moyenne est {x["avg_download"]}mb/s')
        print(f'terminé, votre vitesse de publier moyenne est {x["avg_upload"]}mb/s')
    elif repeat == '3':
        #découvre à quel point l'utilisateur veut que la moyenne soit précise, assez inutile je sais
        times_through = int(input('combien de fois voulez-vous que le test s exécute ?'\n>>>'))
        #trouve la vitesse de téléchargement moyenne
        x = looped_av(times_through)
        print(f'terminé, votre vitesse de téléchargement moyenne est {x["avg_download"]}mb/s')
        print(f'terminé, votre vitesse de publier moyenne est  {x["avg_upload"]}mb/s')
    else:
        #breaks from the loop
        break
