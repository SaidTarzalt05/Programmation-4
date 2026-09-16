\# Doc2MD — Préprocesseur Word vers Markdown



\## 1. Présentation du projet



Doc2MD est un programme développé en Python qui permet de convertir un document Word (`.docx`) en Markdown (`.md`).



Le programme utilise ensuite la bibliothèque Mistletoe pour transformer le Markdown en HTML (`.html`), afin de pouvoir afficher le résultat dans un navigateur web comme Google Chrome.



Le préprocesseur fonctionne indépendamment de Mistletoe et ne modifie pas son code source.



\## 2. Fonctionnalités



Le programme permet de :



\- Lire un document Word au format `.docx`.

\- Extraire le texte du document.

\- Reconnaître les titres et les paragraphes.

\- Convertir les titres en Markdown.

\- Conserver le texte en gras et en italique.

\- Convertir les listes à puces.

\- Convertir les listes numérotées.

\- Convertir les hyperliens.

\- Convertir les tableaux Word en HTML intégré au Markdown.

\- Extraire les images dans un dossier.

\- Générer un fichier Markdown (`output.md`).

\- Générer un fichier HTML (`output.html`) avec Mistletoe.



\## 3. Prérequis



Pour utiliser le programme, il faut avoir :



\- Python 3 installé sur l'ordinateur.

\- La bibliothèque `python-docx`.

\- La bibliothèque `mistletoe`.



\## 4. Installation des bibliothèques



Ouvrir un terminal dans Visual Studio Code ou une invite de commandes Windows.



Installer les bibliothèques nécessaires avec les commandes suivantes :



```bash

python -m pip install python-docx

python -m pip install mistletoe

```



Si plusieurs versions de Python sont installées, il faut utiliser la même version pour installer les bibliothèques et exécuter le programme.



Pour vérifier que les bibliothèques sont correctement installées :



```bash

python -c "from docx import Document; import mistletoe; print('Installation réussie')"

```



\## 5. Structure du projet



Les fichiers doivent être organisés de cette façon :



```text

Projet1/

│

├── Preprocesseur.py

├── test.docx

├── output.md

├── output.html

└── images/

```



Description des fichiers :



\- `Preprocesseur.py` : programme principal de conversion.

\- `test.docx` : document Word à convertir.

\- `output.md` : fichier Markdown généré.

\- `output.html` : fichier HTML généré.

\- `images/` : dossier contenant les images extraites du document Word.



Les fichiers `output.md`, `output.html` et le dossier `images/` sont créés automatiquement lors de l'exécution du programme.



\## 6. Utilisation



\### Étape 1 — Préparer le document Word



Placer le document Word à convertir dans le même dossier que `Preprocesseur.py`.



Le document doit être nommé :



`test.docx`



\### Étape 2 — Exécuter le programme



Ouvrir un terminal et se placer dans le dossier contenant le programme.



Exécuter la commande :



```bash

python Preprocesseur.py

```



\### Étape 3 — Vérifier les résultats



Après l'exécution, le programme affiche :



```text

Conversion terminée.

Markdown : .../output.md

HTML : .../output.html

Images : .../images

```



Le fichier `output.md` contient le document converti en Markdown.



Le fichier `output.html` contient le résultat de la conversion effectuée par Mistletoe.



\### Étape 4 — Ouvrir le fichier HTML



Pour visualiser le résultat :



1\. Ouvrir le dossier du projet.

2\. Faire un clic droit sur `output.html`.

3\. Sélectionner « Ouvrir avec ».

4\. Choisir Google Chrome.



Le document converti sera affiché dans le navigateur.



\## 7. Fonctionnement du programme



Le processus de conversion est le suivant :



```text

Document Word (.docx)

&#x20;       

&#x20;       v

Préprocesseur Python

&#x20;       

&#x20;       v

Extraction du texte et de la structure

&#x20;       

&#x20;       v

Conversion en Markdown

&#x20;       

&#x20;       v

Fichier output.md

&#x20;       

&#x20;       v

Mistletoe

&#x20;       

&#x20;       v

Fichier output.html

&#x20;       

&#x20;       v

Google Chrome

```



\## 8. Limites connues



\- Le programme prend actuellement en charge les documents `.docx`.

\- Les titres sont reconnus à partir des styles `Heading 1`, `Heading 2` et `Heading 3`.

\- Les listes sont reconnues à partir des styles `List Bullet` et `List Number`.

\- Certains styles personnalisés de Word peuvent ne pas être reconnus.

\- Les tableaux sont convertis en HTML intégré au Markdown.

\- Les images intégrées sont extraites, mais certains types d'images ou de mises en page complexes peuvent ne pas être pris en charge.

\- La mise en forme du document Word original n'est pas entièrement reproduite.



\## 9. Problèmes fréquents



\### Erreur : No module named 'docx'



Cette erreur signifie que la bibliothèque `python-docx` n'est pas installée dans l'environnement Python utilisé.



Solution :



```bash

python -m pip install python-docx

```



\### Erreur : No module named 'mistletoe'



Solution :



```bash

python -m pip install mistletoe

```



\### Erreur : Package not found at 'test.docx'



Vérifier que le fichier `test.docx` existe et se trouve dans le même dossier que `Preprocesseur.py`.



\### Les listes ne sont pas reconnues



Vérifier que les listes utilisent les styles de liste de Word et qu'elles ne sont pas simplement écrites avec des tirets ou des chiffres.



\## 10. Auteur



\*\*Said Tarzalt\*\*



Cégep de Sherbrooke



Cours : 243-524-SH — Programmation 4

