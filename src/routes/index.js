const express = require('express');
const router = express.Router();
const scrapeController = require('../scrapers/scrapeController');

// Route pour la page principale
router.get('/', (req, res) => {
  res.render('index', { title: 'OrbitWatch', data: null });
});

// Exemple d'API pour récupérer des données via scraping
router.get('/scrape', async (req, res) => {
  try {
    const data = await scrapeController.scrapeData();
    res.render('index', { title: 'Résultats', data });
  } catch (error) {
    console.error(error);
    res.status(500).send('Erreur lors du scraping');
  }
});

module.exports = router;
