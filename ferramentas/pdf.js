// Gera PDF a partir do HTML com o Chromium do Playwright: node pdf.js <entrada.html> <saida.pdf>
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2], { waitUntil: 'networkidle' });
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, preferCSSPageSize: true,
    tagged: true, outline: true, displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8pt;width:100%;text-align:center;font-family:Liberation Serif,serif;color:#555"><span class="pageNumber"></span></div>' });
  await b.close();
})();
