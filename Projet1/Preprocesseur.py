from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.text.run import Run
from docx.oxml.ns import qn
from pathlib import Path
import mistletoe


# --------------------------------------------------
# Conversion du gras, italique et images
# --------------------------------------------------

def convertir_run(run_element, paragraphe, dossier_images):
    run = Run(run_element, paragraphe)
    texte = run.text

    # Gras + italique
    if run.bold and run.italic:
        texte = f"***{texte}***"

    # Gras
    elif run.bold:
        texte = f"**{texte}**"

    # Italique
    elif run.italic:
        texte = f"*{texte}*"

    resultat = texte

    # Recherche d'images dans le run
    for element in run_element.iter():
        if element.tag == qn("a:blip"):

            relation_id = element.get(qn("r:embed"))

            if relation_id:
                relation = paragraphe.part.rels[relation_id]

                image = relation.target_part

                nom_image = Path(image.partname).name
                chemin_image = dossier_images / nom_image

                # Sauvegarde de l'image
                with open(chemin_image, "wb") as fichier:
                    fichier.write(image.blob)

                # Syntaxe Markdown pour une image
                resultat += f"\n\n![{nom_image}](images/{nom_image})\n\n"

    return resultat


# --------------------------------------------------
# Conversion d'un paragraphe
# --------------------------------------------------

def convertir_paragraphe(paragraphe, dossier_images):
    texte_markdown = ""

    # On parcourt les éléments XML pour détecter
    # les textes normaux ET les hyperliens
    for element in paragraphe._p:

        # Texte normal
        if element.tag == qn("w:r"):

            texte_markdown += convertir_run(
                element,
                paragraphe,
                dossier_images
            )

        # Hyperlien
        elif element.tag == qn("w:hyperlink"):

            relation_id = element.get(qn("r:id"))

            texte_lien = ""

            # Récupérer le texte du lien
            for run_element in element.findall(qn("w:r")):

                texte_lien += convertir_run(
                    run_element,
                    paragraphe,
                    dossier_images
                )

            # Récupérer l'adresse URL
            if relation_id:

                relation = paragraphe.part.rels[relation_id]
                url = relation.target_ref

                texte_markdown += f"[{texte_lien}]({url})"

            else:
                texte_markdown += texte_lien

    return texte_markdown


# --------------------------------------------------
# Conversion d'un tableau Word
# --------------------------------------------------

def convertir_tableau(tableau, dossier_images):
    html = "\n<table>\n"

    for ligne in tableau.rows:

        html += "  <tr>\n"

        for cellule in ligne.cells:

            contenu = ""

            for paragraphe in cellule.paragraphs:

                texte = convertir_paragraphe(
                    paragraphe,
                    dossier_images
                ).strip()

                if texte:
                    contenu += texte + " "

            html += f"    <td>{contenu.strip()}</td>\n"

        html += "  </tr>\n"

    html += "</table>\n\n"

    return html


# --------------------------------------------------
# Conversion Word vers Markdown
# --------------------------------------------------

def convertir_en_markdown(chemin, dossier_images):

    document = Document(chemin)

    markdown = ""

    # Permet de garder l'ordre des paragraphes
    # et des tableaux dans le document
    for element in document.element.body.iterchildren():

        # ------------------------------------------
        # PARAGRAPHE
        # ------------------------------------------

        if element.tag == qn("w:p"):

            paragraphe = Paragraph(element, document)

            texte = convertir_paragraphe(
                paragraphe,
                dossier_images
            ).strip()

            if texte == "":
                continue

            style = paragraphe.style.name

            # Titres
            if style == "Heading 1":
                markdown += "# " + texte + "\n\n"

            elif style == "Heading 2":
                markdown += "## " + texte + "\n\n"

            elif style == "Heading 3":
                markdown += "### " + texte + "\n\n"

            # Liste à puces
            elif style == "List Bullet":
                markdown += "- " + texte + "\n"

            # Liste numérotée
            elif style == "List Number":
                markdown += "1. " + texte + "\n"

            # Paragraphe normal
            else:
                markdown += texte + "\n\n"

        # ------------------------------------------
        # TABLEAU
        # ------------------------------------------

        elif element.tag == qn("w:tbl"):

            tableau = Table(element, document)

            markdown += convertir_tableau(
                tableau,
                dossier_images
            )

    return markdown


# --------------------------------------------------
# CHEMINS
# --------------------------------------------------

dossier_script = Path(__file__).parent

fichier_word = dossier_script / "test.docx"

fichier_markdown = dossier_script / "output.md"

fichier_html = dossier_script / "output.html"

dossier_images = dossier_script / "images"


# Créer le dossier images s'il n'existe pas
dossier_images.mkdir(exist_ok=True)


# --------------------------------------------------
# WORD VERS MARKDOWN
# --------------------------------------------------

markdown = convertir_en_markdown(
    fichier_word,
    dossier_images
)


# Sauvegarder le Markdown
with open(
    fichier_markdown,
    "w",
    encoding="utf-8"
) as fichier:

    fichier.write(markdown)


# --------------------------------------------------
# MARKDOWN VERS HTML AVEC MISTLETOE
# --------------------------------------------------

contenu_html = mistletoe.markdown(markdown)


# Créer une vraie page HTML
html = f"""<!DOCTYPE html>

<html lang="fr">

<head>

    <meta charset="UTF-8">

    <title>Document converti</title>

</head>

<body>

{contenu_html}

</body>

</html>
"""


# Sauvegarder le HTML
with open(
    fichier_html,
    "w",
    encoding="utf-8"
) as fichier:

    fichier.write(html)


print("Conversion terminée.")

print("Markdown :", fichier_markdown)

print("HTML :", fichier_html)

print("Images :", dossier_images)