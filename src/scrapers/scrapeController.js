const axios = require('axios');
const cheerio = require('cheerio');

async function scrapeData() {
  const url = 'https://example.com'; // Remplace par l'URL cible

  const { data } = await axios.get(url);
  const $ = cheerio.load(data);

  // Exemple : extraire des titres
  const results = [];
  $('h2.title').each((index, element) => {
    results.push($(element).text());
  });

  return results;
}

module.exports = { scrapeData };
