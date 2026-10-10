"""Gera o .docx e o .pdf a partir do .md. Uso: python3 ferramentas/gerar.py
Requisitos: pip install pypandoc_binary pypdf; node com playwright (Chromium).
O modelo do .docx (A4, Times 12, entrelinha 1,5) é gerado por ferramentas/criar_referencia.py."""
import os, re, shutil, subprocess, tempfile, zipfile
import pypandoc
from pypdf import PdfReader, PdfWriter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "Da_lampada_ao_token_v2_CONSOLIDADO"
MD, DOCX, PDF = (os.path.join(RAIZ, BASE + ext) for ext in (".md", ".docx", ".pdf"))
AUTOR = "Ricardo Junqueira Malhão"
ORCID_URL = "https://orcid.org/0009-0002-9776-4906"
TITULO = "Da lâmpada ao token"
ASSUNTO = "Degradação de qualidade e incentivo econômico em mercados de inteligência artificial"
ENTRADA = "markdown+autolink_bare_uris"  # URLs das referências viram links clicáveis
CHAVES = ("obsolescência programada; assimetria de informação; enshittification; quantização; "
          "padrões obscuros; auditoria capturada; bajulação; modelos de linguagem; custo de inferência")


def gerar_docx():
    os.chdir(RAIZ)
    pypandoc.convert_file(MD, "docx", format=ENTRADA, outputfile=DOCX,
                          extra_args=["--reference-doc=" + os.path.join(RAIZ, "ferramentas", "referencia_abnt.docx")])
    # Pos-processamento: link clicavel no proprio icone (a:hlinkClick), texto alternativo e autor nos metadados
    tmp = DOCX + ".tmp"
    with zipfile.ZipFile(DOCX) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        rels = zin.read("word/_rels/document.xml.rels").decode()
        rid = re.search(r'Id="(rId\d+)"[^>]*Target="%s"' % re.escape(ORCID_URL), rels) or \
              re.search(r'Target="%s"[^>]*Id="(rId\d+)"' % re.escape(ORCID_URL), rels)
        rid = rid.group(1)
        link = '<a:hlinkClick xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" r:id="%s"/>' % rid
        for item in zin.infolist():
            dados = zin.read(item.filename)
            if item.filename == "word/document.xml":
                x = dados.decode()
                x = re.sub(r'(<wp:docPr descr="ORCID iD"[^>]*?)\s*/>', r'\1>%s</wp:docPr>' % link, x)
                x = re.sub(r'(<pic:cNvPr[^>]*?)descr="assets/orcid_id_icon\.png"([^>]*?)\s*/>',
                           r'\1descr="ORCID iD"\2>%s</pic:cNvPr>' % link, x)
                dados = x.encode()
            elif item.filename == "docProps/core.xml":
                x = dados.decode()
                x = re.sub(r"<dc:creator>.*?</dc:creator>|<dc:creator\s*/>", "<dc:creator>%s</dc:creator>" % AUTOR, x)
                dados = x.encode()
            zout.writestr(item, dados)
    os.replace(tmp, DOCX)


def gerar_pdf():
    with tempfile.TemporaryDirectory() as d:
        shutil.copytree(os.path.join(RAIZ, "assets"), os.path.join(d, "assets"))
        shutil.copy(os.path.join(RAIZ, "ferramentas", "estilo_pdf.css"), d)
        fonte = open(MD, encoding="utf-8").read().replace("assets/orcid_id_icon.png", "assets/orcid_id_icon.svg")
        open(os.path.join(d, "fonte.md"), "w", encoding="utf-8").write(fonte)
        os.chdir(d)
        pypandoc.convert_file("fonte.md", "html5", format=ENTRADA, outputfile="artigo.html", extra_args=[
            "--standalone", "--embed-resources", "--section-divs", "--css=estilo_pdf.css",
            "-M", "document-css=false", "-M", "pagetitle=" + TITULO])
        bruto = os.path.join(d, "bruto.pdf")
        subprocess.run(["node", os.path.join(RAIZ, "ferramentas", "pdf.js"), os.path.join(d, "artigo.html"), bruto], check=True)
        w = PdfWriter(clone_from=PdfReader(bruto))
        w.add_metadata({"/Title": TITULO, "/Author": AUTOR, "/Subject": ASSUNTO, "/Keywords": CHAVES})
        with open(PDF, "wb") as f:
            w.write(f)
    os.chdir(RAIZ)


if __name__ == "__main__":
    gerar_docx()
    gerar_pdf()
    print("ok:", DOCX, PDF)
