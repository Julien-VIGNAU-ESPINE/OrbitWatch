const express = require('express');
const path = require('path');
const routes = require('./routes'); // Importer les routes

const app = express();

// Définir le moteur de vue (EJS si besoin)
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '../views'));

// Servir les fichiers statiques
app.use(express.static(path.join(__dirname, '../public')));

// Utiliser les routes
app.use('/', routes);

module.exports = app;
