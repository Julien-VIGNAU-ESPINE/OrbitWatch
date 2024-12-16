const express = require('express');
const app = require('./src/app'); // Point d'entrée principal du projet

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Serveur lancé sur http://localhost:${PORT}`);
});
