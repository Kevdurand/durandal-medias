# Voix off officielle Strikzy (fr-FR-Polyglot-1, vitesse 1.2) — R6 « Le débat : qui gagne le Major ? », 19/11/2026.
# À lancer dans Cloud Shell (projet strikzy-voix) : aucune clé, le jeton vient de la session gcloud de Kévin.
import json, base64, subprocess, urllib.request, os, zipfile
tok = subprocess.check_output(['gcloud', 'auth', 'print-access-token'], text=True).strip()
txt = ("Qui gagne le Major ? Les Falcons sont tenants du titre : trois à zéro contre Fouria, en finale à Cologne. "
       "Mais Fouria a pris sa revanche à Hong Kong, et enchaîne trois titres en un mois. "
       "Et Vitaliti ? Cinq titres d'affilée en début d'année, puis une sortie rapide à Hong Kong. "
       "Alors, ton favori ? Dis-le en commentaire.")
body = {'input': {'text': txt}, 'voice': {'languageCode': 'fr-FR', 'name': 'fr-FR-Polyglot-1'},
        'audioConfig': {'audioEncoding': 'LINEAR16', 'sampleRateHertz': 48000, 'speakingRate': 1.2}}
rq = urllib.request.Request('https://texttospeech.googleapis.com/v1/text:synthesize', data=json.dumps(body).encode(),
                            headers={'Authorization': 'Bearer ' + tok, 'x-goog-user-project': 'strikzy-voix', 'Content-Type': 'application/json'})
wav = base64.b64decode(json.load(urllib.request.urlopen(rq, timeout=90))['audioContent'])
out = os.path.expanduser('~/voix-R6.zip')
with zipfile.ZipFile(out, 'w') as z: z.writestr('R6_debat.wav', wav)
print('ok R6_debat — zip prêt :', out)
