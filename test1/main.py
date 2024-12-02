import pandas as pd


# Exercitiul 1
agriculture_data = pd.read_csv('Agricultura.csv')

agriculture_data['CifraTotalaAfaceri'] = (agriculture_data['PlanteNepermanente'] + agriculture_data['PlanteInmultire']
                                          + agriculture_data['CrestereaAnimalelor'] + agriculture_data['FermeMixte']
                                          + agriculture_data['ActivitatiAuxiliare'])

output_data = agriculture_data[['Siruta', 'Localitate', 'CifraTotalaAfaceri']]
output_data.to_csv('Cerinta1.csv', index = False, header=['Siruta', 'Localitate', 'CifraAfaceri'])
print("Fisierul cerinta1.csv a fost generat cu succes")
print(agriculture_data.columns)

# Exercitiul 2

# gasirea activitatii cu cifra de afaceri cea mai mare pentru fiecare localitate
def max_activity(row):
    activities = ['PlanteNepermanente', 'PlanteInmultire', 'CrestereaAnimalelor', 'FermeMixte', 'ActivitatiAuxiliare']
    max_activity_name = max(activities, key=lambda activity: row[activity])
    return max_activity_name

agriculture_data['ActivitateMaxima'] = agriculture_data.apply(max_activity, axis=1) # axis=1 pentru a aplica functia pe fiecare rand

output_data = agriculture_data[['Siruta', 'Localitate', 'ActivitateMaxima']]

output_data.to_csv('Cerinta2.csv', index = False, header=['Siruta', 'Localitate', 'ActivitateMaxima'])

print("Fisierul cerinta2.csv a fost generat cu succes")

# Exercitiul 3

population_data = pd.read_csv('PopulatieLocalitati.csv')

merged_data = pd.merge(agriculture_data, population_data, on='Siruta')
activities = ['PlanteNepermanente', 'PlanteInmultire', 'CrestereaAnimalelor', 'FermeMixte', 'ActivitatiAuxiliare']
result = merged_data.groupby('Judet')[activities].sum() # sumarea cifrelor de afaceri pentru fiecare judet

result['Populatie'] = merged_data.groupby('Judet')['Populatie'].sum() # adaugarea populatiei pentru fiecare judet

for activity in activities:
    result[activity + '_PeLocuitor'] = result[activity] / result['Populatie'] # calcularea cifrei de afaceri pe locuitor pentru fiecare activitate

output_data = result[[acitivity + '_PeLocuitor' for acitivity in activities]].reset_index()
output_data.to_csv('Cerinta3.csv', index = False, header=['Judet'] + activities)

print("Fisierul cerinta3.csv a fost generat cu succes")

# Exercitiul 4

results = {}
for activity in activities:
    merged_data[f'{activity}_Ponderat'] = merged_data[activity] * merged_data['Populatie'] # calcularea cifrei de afaceri ponderate pentru fiecare activitate

grouped = merged_data.groupby('Judet')
for activity in activities:
    results[activity] = grouped[f'{activity}_Ponderat'].sum() / grouped['Populatie'].sum() # calcularea cifrei de afaceri pe locuitor pentru fiecare activitate

output_data = pd.DataFrame(results).reset_index()

output_data.to_csv('Cerinta4.csv', index = False, header=['Judet'] + activities)
print("Fisierul cerinta4.csv a fost generat cu succes")
