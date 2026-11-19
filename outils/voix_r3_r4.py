# Voix off officielle Strikzy (fr-FR-Polyglot-1) — Reels R3 et R4, 19/11/2026.
# À lancer dans Cloud Shell (projet strikzy-voix) : aucune clé, le jeton vient de la session gcloud de Kévin.
import json, base64, subprocess, urllib.request, os, zipfile
tok = subprocess.check_output(['gcloud', 'auth', 'print-access-token'], text=True).strip()
textes = {
 'R3_fallen': "Dernier Major pour Falène. Après vingt-trois ans de carrière et deux Majors gagnés, la légende brésilienne s'arrête à la fin de l'année. Et il arrive en pleine forme : dimanche, Fouria a battu Spiritte trois à zéro, à Hong Kong. Troisième titre en un mois. Dernier arrêt : Singapour. Alors, il finit sur un titre ?",
 'R4_major': "Mardi, cinq heures du matin : le Major CS 2 commence. Trente-deux équipes, un seul titre, jusqu'au treize décembre. Côté français, Neïtiou ouvre le bal avec Féize, mardi à huit heures. Zywou et Apex entrent en jeu le deux décembre, avec Vitaliti. Alors, mets ton réveil.",
}
out = os.path.expanduser('~/voix-R3-R4.zip')
with zipfile.ZipFile(out, 'w') as z:
    for nom, txt in textes.items():
        for v in (1.1, 1.2):
            body = {'input': {'text': txt}, 'voice': {'languageCode': 'fr-FR', 'name': 'fr-FR-Polyglot-1'},
                    'audioConfig': {'audioEncoding': 'LINEAR16', 'sampleRateHertz': 48000, 'speakingRate': v}}
            rq = urllib.request.Request('https://texttospeech.googleapis.com/v1/text:synthesize', data=json.dumps(body).encode(),
                                        headers={'Authorization': 'Bearer ' + tok, 'x-goog-user-project': 'strikzy-voix', 'Content-Type': 'application/json'})
            z.writestr(f'{nom}_v{v}.wav', base64.b64decode(json.load(urllib.request.urlopen(rq))['audioContent']))
            print('ok', nom, v)
print('zip prêt :', out)
