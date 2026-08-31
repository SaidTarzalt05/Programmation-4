from docx import Document
from pathlib import Path
import mistletoe


def convertir_paragraphe(paragraphe):
    texte_markdown = ""

    # Gestion du gras et de l'italique
    for run in paragraphe.runs:
        texte = run.text

        if run.bold and run.italic:
            texte_markdown += f"***{texte}***"

        elif run.bold:
            texte_markdown += f"**{texte}**"

        elif run.italic:
            texte_markdown += f"*{texte}*"

        else:
            texte_markdown += texte

    return texte_markdown


def convertir_en_markdown(chemin):
    document = Document(chemin)

    markdown = ""

    for paragraphe in document.paragraphs:
        texte = convertir_paragraphe(paragraphe).strip()

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

    return markdown


# Chemins
dossier_script = Path(__file__).parent

fichier_word = dossier_script / "test.docx"
fichier_markdown = dossier_script / "output.md"
fichier_html = dossier_script / "output.html"


# Word vers Markdown
markdown = convertir_en_markdown(fichier_word)


# Sauvegarder le Markdown
with open(fichier_markdown, "w", encoding="utf-8") as fichier:
    fichier.write(markdown)


# Markdown vers HTML avec Mistletoe
html = mistletoe.markdown(markdown)


# Créer le fichier HTML
with open(fichier_html, "w", encoding="utf-8") as fichier:
    fichier.write(html)


print("Conversion terminée.")
print("Markdown :", fichier_markdown)
print("HTML :", fichier_html)