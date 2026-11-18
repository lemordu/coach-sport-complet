# Nutrition : profil, BMR / TDEE / macros, repas

Ne jamais inventer une mesure manquante. Si le poids, la taille, l’âge, le genre, le niveau d’activité ou l’objectif manque, demander **une information à la fois**. Les exemples chiffrés ci-dessous sont fictifs et servent uniquement à illustrer les formules.

## Profil (modèle)

```python
from pydantic import BaseModel, Field
from typing import Literal

class PhysicalProfile(BaseModel):
    weight_kg: float = Field(gt=30, lt=300)
    height_cm: float = Field(gt=120, lt=230)
    age: int = Field(ge=14, le=100)
    gender: Literal["male", "female"]
    activity: Literal["sedentary", "lightly_active", "moderately_active", "very_active"]
    goal: Literal["weight_loss", "muscle_gain", "maintenance"]
    restrictions: list[str] = []   # ex. végétarien, sans lactose, allergie arachide
    injuries: list[str] = []       # ex. genou, dos — zones, pas de dossier médical
```

Si l’environnement le permet et que la personne le souhaite, on peut mémoriser un fait de profil **générique** (poids, taille, âge, activité, objectif, restrictions, zones sensibles), puis le remplacer (oublier l’ancien, écrire le nouveau) plutôt que d’empiler les versions.

## Calcul BMR / TDEE / macros

Script : `python3 scripts/calc.py --weight KG --height CM --age ANS --gender male|female --activity … --goal …`

- **BMR** (Mifflin-St Jeor) : homme `10*kg + 6.25*cm - 5*âge + 5` ; femme `… − 161`.
- **TDEE** = BMR × activité : sedentary 1,2 ; lightly_active 1,375 ; moderately_active 1,55 ; very_active 1,725.
- **Cible** : perte de poids = TDEE − 500 ; prise de muscle = TDEE + 300 ; maintien = TDEE.
- Protéines ≈ 2 g/kg (4 kcal/g). Lipides ≈ 25 % des kcal (9 kcal/g). Glucides = le reste (4 kcal/g).
- Garde-fou : ne jamais descendre sous environ le BMR, ni sous **1500 kcal** (homme) / **1200 kcal** (femme). Si le déficit le ferait, plafonner et le dire clairement.
- Présenter BMR, TDEE, cible, puis P/L/G en grammes arrondis, et la formule en une ligne.

Exemple de vérification (fictif) : homme 35 ans, 82 kg, 180 cm, modérément actif, perte de poids → BMR 1775, TDEE 2751, cible 2251, P 164 g, L 63 g, G 258 g.

Recalculer si le poids change d’au moins 2 kg, ou si l’activité ou l’objectif change.

## Recettes et plans de repas

```python
class Recipe(BaseModel):
    name: str
    servings: int = 1
    ingredients: list[str]          # quantités en g/ml
    steps: list[str]
    kcal: int
    protein_g: int
    fat_g: int
    carbs_g: int
    tags: list[str] = []            # ex. sans_lactose, rapide, batch
```

- Respecter strictement les restrictions et allergies ; en cas de doute sur un ingrédient, l’exclure.
- Plan journalier : 3–5 repas, total à ±5 % des kcal cibles et ±10 g de protéines. Tableau : repas | kcal | P | L | G + total.
- Macros issues de valeurs typiques (CIQUAL / USDA) : ce sont des **estimations**.
- Sur demande : liste de courses par rayon, version batch cooking.

## Limites nutrition

Pas de diagnostic. Grossesse, trouble alimentaire, diabète, maladie rénale, moins de 18 ans : recommander un professionnel avant un déficit calorique.
