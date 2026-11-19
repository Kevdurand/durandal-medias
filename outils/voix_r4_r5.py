# Voix off officielle Strikzy (fr-FR-Polyglot-1, vitesse 1.2) — R4 v3 (deux variantes) et R5, 19/11/2026.
# À lancer dans Cloud Shell (projet strikzy-voix) : aucune clé, le jeton vient de la session gcloud de Kévin.
import json, base64, subprocess, urllib.request, os, zipfile
tok = subprocess.check_output(['gcloud', 'auth', 'print-access-token'], text=True).strip()
textes = {
 'R4a_avec_francais': "Le Major CS 2 arrive ! Mardi, dès cinq heures du matin, le Stéïdje un commence. Trente-deux équipes, un seul titre, jusqu'au treize décembre. Côté français, Neïtiou ouvre le bal avec Féize, mardi à huit heures. Zywou et Apex entrent en jeu le deux décembre, avec Vitaliti. Alors, mets ton réveil.",
 'R4b_programme': "Le Major CS 2 arrive ! Mardi, dès cinq heures du matin, le Stéïdje un commence. Trente-deux équipes, un seul titre. Trois étapes, puis les playoffs, du dix au treize décembre, dans un stade à Singapour. Mardi matin, huit matchs d'entrée, deux par heure. Alors, mets ton réveil.",
 'R5_francais': "Trois Français au Major de Singapour. Neïtiou, avec Féize : son tout premier Major. Féize avait manqué Cologne, et revient sur la plus grande scène. Premier match mardi, huit heures. Et chez Vitaliti, Zywou et Apex. Cinq titres en début d'année, mais une sortie rapide à Hong Kong. Ils entrent en jeu le deux décembre. Bonne chance à eux trois. Alors, qui ira le plus loin ?",
}
out = os.path.expanduser('~/voix-R4-R5.zip')
with zipfile.ZipFile(out, 'w') as z:
    for nom, txt in textes.items():
        body = {'input': {'text': txt}, 'voice': {'languageCode': 'fr-FR', 'name': 'fr-FR-Polyglot-1'},
                'audioConfig': {'audioEncoding': 'LINEAR16', 'sampleRateHertz': 48000, 'speakingRate': 1.2}}
        rq = urllib.request.Request('https://texttospeech.googleapis.com/v1/text:synthesize', data=json.dumps(body).encode(),
                                    headers={'Authorization': 'Bearer ' + tok, 'x-goog-user-project': 'strikzy-voix', 'Content-Type': 'application/json'})
        z.writestr(f'{nom}.wav', base64.b64decode(json.load(urllib.request.urlopen(rq))['audioContent']))
        print('ok', nom)
print('zip prêt :', out)
