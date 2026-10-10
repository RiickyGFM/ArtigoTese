"""Cria ferramentas/referencia_abnt.docx a partir do modelo padrão do pandoc.
Ajustes: papel A4, margens 3 cm (sup./esq.) e 2 cm (inf./dir.), Times New Roman 12,
entrelinha 1,5, texto justificado, títulos em preto e número de página no rodapé.
Uso: python3 ferramentas/criar_referencia.py"""
import os, re, subprocess, tempfile, zipfile
import pypandoc

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "ferramentas", "referencia_abnt.docx")
FONTE = '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman" />'
RODAPE = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
    '<w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
    '<w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
    '<w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
    '<w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r>'
    '<w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:t>1</w:t></w:r>'
    '<w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r>'
    '</w:p></w:ftr>'
)


def estilo(s, sid, f):
    m = re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % sid, s, re.S)
    if not m:
        raise SystemExit("estilo ausente: " + sid)
    return s[:m.start()] + f(m.group(0)) + s[m.end():]


def rpr(bloco, novo):
    """Troca o rPr do estilo por um novo (fonte explícita, sem cor de tema)."""
    bloco = re.sub(r"<w:rPr>.*?</w:rPr>", "", bloco, flags=re.S)
    return bloco.replace("</w:style>", "<w:rPr>%s%s</w:rPr></w:style>" % (FONTE, novo))


def ppr(bloco, novo):
    bloco = re.sub(r"<w:pPr>.*?</w:pPr>", "", bloco, flags=re.S)
    return re.sub(r"(<w:qFormat ?/>|<w:name [^>]*/>)", r"\1<w:pPr>%s</w:pPr>" % novo, bloco, count=1)


def main():
    pandoc = pypandoc.get_pandoc_path()
    with tempfile.TemporaryDirectory() as d:
        base = os.path.join(d, "base.docx")
        subprocess.run([pandoc, "-o", base, "--print-default-data-file", "reference.docx"], check=True)
        zin = zipfile.ZipFile(base)
        arquivos = {n: zin.read(n) for n in zin.namelist()}

    s = arquivos["word/styles.xml"].decode()
    s = re.sub(r"<w:rPrDefault>.*?</w:rPrDefault>",
               "<w:rPrDefault><w:rPr>%s<w:sz w:val=\"24\" /><w:szCs w:val=\"24\" />"
               "<w:lang w:val=\"pt-BR\" w:eastAsia=\"pt-BR\" w:bidi=\"ar-SA\" /></w:rPr></w:rPrDefault>" % FONTE, s, flags=re.S)
    s = re.sub(r"<w:pPrDefault>.*?</w:pPrDefault>",
               "<w:pPrDefault><w:pPr><w:spacing w:after=\"120\" w:line=\"360\" w:lineRule=\"auto\" /></w:pPr></w:pPrDefault>", s, flags=re.S)
    s = estilo(s, "BodyText", lambda b: ppr(b, '<w:spacing w:before="0" w:after="120" /><w:jc w:val="both" />'))
    s = estilo(s, "Compact", lambda b: ppr(b, '<w:spacing w:before="0" w:after="60" /><w:jc w:val="left" />'))
    s = estilo(s, "Title", lambda b: rpr(b, '<w:b /><w:sz w:val="32" /><w:szCs w:val="32" />'))
    s = estilo(s, "Subtitle", lambda b: rpr(b, '<w:b w:val="0" /><w:i /><w:sz w:val="26" /><w:szCs w:val="26" />'))
    s = estilo(s, "Author", lambda b: rpr(b, '<w:b w:val="0" /><w:sz w:val="24" /><w:szCs w:val="24" />'))
    s = estilo(s, "Heading1", lambda b: rpr(b, '<w:b /><w:sz w:val="28" /><w:szCs w:val="28" />'))
    s = estilo(s, "Heading2", lambda b: rpr(b, '<w:b /><w:sz w:val="24" /><w:szCs w:val="24" />'))
    s = estilo(s, "Heading3", lambda b: rpr(b, '<w:b /><w:i /><w:sz w:val="24" /><w:szCs w:val="24" />'))
    # Referências (ABNT NBR 6023): alinhadas à esquerda, espaço simples, uma linha em branco entre elas
    s = s.replace("</w:styles>",
                  '<w:style w:type="paragraph" w:customStyle="1" w:styleId="Referencia">'
                  '<w:name w:val="Referencia" /><w:basedOn w:val="Normal" /><w:qFormat />'
                  '<w:pPr><w:spacing w:before="0" w:after="240" w:line="240" w:lineRule="auto" /><w:jc w:val="left" /></w:pPr>'
                  '</w:style></w:styles>')
    arquivos["word/styles.xml"] = s.encode()

    doc = arquivos["word/document.xml"].decode()
    sect = ('<w:sectPr><w:footerReference w:type="default" r:id="rIdRodape1" />'
            '<w:footnotePr><w:numRestart w:val="eachSect" /></w:footnotePr>'
            '<w:pgSz w:w="11906" w:h="16838" />'
            '<w:pgMar w:top="1701" w:right="1134" w:bottom="1134" w:left="1701" w:header="709" w:footer="567" w:gutter="0" />'
            '</w:sectPr>')
    doc = re.sub(r"<w:sectPr>.*?</w:sectPr>", sect, doc, flags=re.S)
    if 'xmlns:r=' not in doc[:2000]:
        doc = doc.replace("<w:document ", '<w:document xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" ', 1)
    arquivos["word/document.xml"] = doc.encode()

    rels = arquivos["word/_rels/document.xml.rels"].decode()
    rels = rels.replace("</Relationships>",
                        '<Relationship Id="rIdRodape1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>')
    arquivos["word/_rels/document.xml.rels"] = rels.encode()
    tipos = arquivos["[Content_Types].xml"].decode()
    tipos = tipos.replace("</Types>",
                          '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>')
    arquivos["[Content_Types].xml"] = tipos.encode()
    arquivos["word/footer1.xml"] = RODAPE.encode()

    with zipfile.ZipFile(SAIDA, "w", zipfile.ZIP_DEFLATED) as z:
        for nome, dados in arquivos.items():
            z.writestr(nome, dados)
    print("ok:", SAIDA)


if __name__ == "__main__":
    main()
