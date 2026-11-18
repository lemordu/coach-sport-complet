# Coach sport complet

Skill unique qui réunit :

- le calcul de **BMR / TDEE / macros** et des **plans de repas** ;
- un cycle de **force A/B/C** (avec substitutions genou / dos) ;
- du **renforcement et des étirements** par articulation (bas du dos, genoux, hanches, épaules, coudes, poignets, et un peu la nuque) ;
- des **progressions de callisthénie** (pompes, tractions, dips, équilibre, muscle-up, L-sit, back lever, drapeau, circuit débutants / surpoids).

Il est pensé pour un assistant IA (Cursor, Claude Code, Grok Bot ou tout outil qui charge un `SKILL.md`). Ce n’est **pas** un avis médical.

Les descriptions d’exercices sont des **reformulations structurées**, pas des transcriptions. Les vidéos, leurs images et leur texte restent la propriété de leurs auteurs. Les liens sources sont listés plus bas.

## Installation

Copier tout le dossier `coach-sport-skill/` (avec `SKILL.md`, `references/`, `scripts/`) sous le nom `coach-sport-complet`.

### Cursor

- Pour un projet : `.cursor/skills/coach-sport-complet/`
- Pour tous vos projets : `~/.cursor/skills/coach-sport-complet/`

Puis rouvrir le projet ou recharger les skills. Dans le chat, le skill apparaît typiquement via `/` ou `@`.

### Claude Code

Placer le dossier dans `~/.claude/skills/coach-sport-complet/` (ou le répertoire de skills indiqué par votre version de Claude Code). Relancer une session si besoin.

### Grok Bot

Importer le skill comme skill utilisateur (fichier `SKILL.md` + dossier `references/` et `scripts/`), puis l’invoquer avec `/` ou `@` selon l’interface. Le script `scripts/calc.py` doit rester au même niveau relatif que dans ce dépôt.

Le cœur du skill est le fichier `SKILL.md` (frontmatter `name` + `description`, puis les consignes). Les détails d’exercices sont dans `references/`. Le calcul reproductible est dans `scripts/calc.py` (Python 3, bibliothèque standard uniquement).

Exemple :

```bash
python3 scripts/calc.py --weight 75 --height 175 --age 30 --gender female --activity lightly_active --goal weight_loss
```

## Contenu

```
coach-sport-skill/
  SKILL.md
  README.md
  LICENSE
  CHANGELOG.md
  scripts/calc.py
  evals/
  references/
    nutrition.md
    training.md
    renforcement-*.md
    etirements.md
    callisthenie-*.md
```

## Sources / crédits

Les méthodes de renforcement, d’étirements et de callisthénie résumées ici s’appuient sur des vidéos publiques des chaînes suivantes. Merci à leurs autrices et auteurs. Allez voir les vidéos originales pour les démonstrations.

### Léa Holistic Training (@leaholistictraining)

- [Tu as mal au dos parce que tu ne sais pas te renforcer](https://youtu.be/UBVlMZQ__R4)
- [Tu renforces tes lombaires comme ça](https://youtu.be/pkA9m8Otkck)
- [Masterclass BACK EXTENSION](https://youtu.be/_wIp-TTDBgU)
- [Retrouve des lombaires SOLIDES et SANS DOULEUR](https://youtu.be/pElxPBRWt9g)
- [5 exercices de mobilité hanches & bas du dos](https://youtu.be/mdoh37svkcc)
- [Mobilité de hanche : 5 exercices, standards et régressions](https://youtu.be/JAlIbr4voDw)
- [Renforce tes genoux : 8 exercices sans équipement](https://youtu.be/hWWT_jYfwiM)
- [Tu renforces tes genoux comme ça](https://youtu.be/y3TzaRU1lbY)
- [Retrouve des genoux solides](https://youtu.be/rWqnoKwvE3A)
- [Retrouve des épaules SOLIDES](https://youtu.be/F5v_70ihItA)
- [Construis-toi des poignets SOLIDES](https://youtu.be/8J2al07rju4)
- [Douleurs aux coudes](https://youtu.be/k1-KuilmZ_o)
- [Poignets, coudes, nuque : les zones oubliées à renforcer en CrossFit](https://youtu.be/FWapc0egc_s)
- [Les étirements](https://youtu.be/6HCO4jhzruw)

### Brieuc Le Dantec (@brieucledantec7422)

- [S'améliorer en tractions](https://youtu.be/dhV4Ea8JpQs)
- [Apprendre les pompes](https://youtu.be/hAD-P3JUGao)
- [Tirer un maximum des barres parallèles](https://youtu.be/lCZrTqQnrFg)
- [Premiers équilibres / ATR](https://youtu.be/59ttse_W0gk)
- [Apprendre les pompes en équilibre](https://youtu.be/VbGoUoY8jhM)
- [Réussir les muscle-ups](https://youtu.be/a6jvpvQ9JZU)
- [Tenir le L](https://youtu.be/5FxjxP50Fc8)
- [L’échauffement en callisthénie](https://youtu.be/4BFOUs-gzAk)
- [Street workout : grands débutants et surpoids](https://youtu.be/A6r5MUIX_vE)
- [Tutorial Back Lever](https://youtu.be/FV-KzobUqko)
- [Tutorial Drapeau humain](https://youtu.be/ZsfSFTHL-F0)

Au moment de la constitution de cette base, la chaîne de Brieuc n’avait pas de tutoriel dédié au **front lever** ni à la **planche**.

La partie nutrition / cycle A/B/C est originale à ce skill (formules Mifflin-St Jeor, macros, canevas de force). Elle n’est pas tirée de ces chaînes.

## Licence

Le texte et le code originaux de ce dépôt sont sous licence **MIT** (voir `LICENSE`). Le contenu des vidéos YouTube reste la propriété de leurs créateurs.
