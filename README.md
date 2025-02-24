# Analyse et Visualisation de Données de Fitness  

## Description  

Ce projet consiste à analyser et visualiser un jeu de données de fitness contenant divers indicateurs de santé et d'activité physique. L'objectif est de découvrir des tendances et des insights liés à l'activité physique, aux calories brûlées, aux habitudes de sommeil et aux performances des entraînements. En utilisant `pandas` pour le traitement des données et `plotly` pour les visualisations interactives, le projet offre une vue complète des habitudes de fitness de l'utilisateur.  

---

## Fonctionnalités  

1. **Prétraitement des Données**  
   - Vérification des valeurs manquantes et affichage des lignes contenant des données manquantes.  
   - Conversion de la colonne `date` en format datetime pour l'analyse des séries temporelles.  
   - Renommage des colonnes pour une meilleure lisibilité.  
   - Création de nouvelles fonctionnalités, notamment :  
     - `weight_lbs` : Conversion du poids corporel de kilogrammes en livres.  
     - `day_of_week` : Extraction du jour de la semaine à partir de la colonne `date`.  
     - `weekend` : Indicateur booléen indiquant si la date tombe un week-end.  
     - `sleep_debt` : Différence entre les heures de sommeil enregistrées et les 7,5 heures recommandées.  
     - `cumulative_sleep_debt` : Somme cumulative de la dette de sommeil au fil du temps.  

2. **Exploration des Données**  
   - Statistiques descriptives pour comprendre la répartition des données numériques.  
   - Vérification des types de données de chaque colonne pour garantir leur cohérence.  

3. **Visualisation des Données**  
   - Histogramme de la fréquence des pas effectués.  
   - Graphique en ligne montrant l'évolution du nombre de pas au fil du temps, avec marquage des week-ends.  
   - Histogramme de la distribution des calories brûlées.  
   - Graphique en ligne montrant l'évolution des calories brûlées au fil du temps, avec marquage des week-ends.  
   - Graphique en ligne des variations de poids corporel au fil du temps.  
   - Graphique en ligne des heures de sommeil au fil du temps.  
   - Comparaison des heures de sommeil en semaine et le week-end à l'aide d'un boxplot.  
   - Moyenne des heures de sommeil par jour de la semaine avec un graphique en barres.  
   - Scatter plot montrant la relation entre le nombre de pas effectués et les calories brûlées.  
   - Boxplot comparant la durée des entraînements en fonction du type d'exercice.  

---

## Prérequis  

- Python 3.x  
- `pandas`  
- `plotly`  

Pour installer les dépendances :  
```bash  
pip install pandas plotly  

### Installation
1. Clonez le dépôt :

\`\`\`sh  
git clone https://github.com/votre-utilisateur/analyse-donnees-fitness.git  
cd analyse-donnees-fitness  
\`\`\`

2. Installez les dépendances :

\`\`\`sh  
pip install -r requirements.txt  
\`\`\`

3. Assurez-vous que le fichier fitness_data.csv se trouve dans le répertoire racine du projet.

### Utilisation

1. Exécutez le script :
\`\`\`sh  
python analyse_donnees_fitness.py  
\`\`\`

2. Le script traitera les données et affichera des visualisations interactives à l'aide de Plotly.

### Résultats
- Le script génère les visualisations suivantes :
    - Histogrammes pour la distribution des steps et des total_calories_burned.
    - Graphiques en ligne montrant l'évolution de steps, total_calories_burned, body_weight_kg et sleep_hours au fil du temps.
    - Boxplots et graphiques en barres pour comparer les données entre les jours de semaine et les week-ends, ainsi que les durées d'entraînement par type d'exercice.

### Conclusion
Ce projet offre un aperçu des tendances et des relations au sein du jeu de données de fitness, comme le lien entre les pas effectués et les calories brûlées, les habitudes de sommeil en semaine et le week-end, ainsi que les variations de poids au fil du temps.