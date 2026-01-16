<template>
  <div class="finale-intro">
    <div class="intro-content">
      <div class="intro-text">
        <p>Bienvenue à ECOCITY, ville fictive aux défis bien réels. Dans le cadre de la finale du TRC2025, notre équipe comme toutes les autres a eu pour objectif de transformer la gestion des déchets de cette métropole grâce à l'intelligence artificielle et la robotique avancée. Le défi ? Nettoyer 10 quartiers encombrés de déchets ménagers, dangereux et recyclables, en alliant rapidité d'exécution et précision de tri.</p>
        
        <p>Notre réponse technologique repose sur une collaboration parfaite entre mobilité et manipulation. Au cœur de notre dispositif : le Rosmaster X3, notre unité mobile chargée de la "reconnaissance et récupération". Après une phase d'analyse de données via des QR Codes pour cartographier la pollution, il opère de manière autonome, traitant en priorité les zones critiques saturées de déchets dangereux grâce à un système de ramassage conçu par nos soins.</p>
        
        <p>Mais la collecte n'est que la première étape. Une fois les déchets acheminés à la station centrale, notre unité de tri, le bras robotique Dofbot, prend le relais. Couplé à un convoyeur personnalisé et un système de vision par ordinateur, il assure la ségrégation des matériaux pour garantir un recyclage optimal.</p>
        
        <p>Ce rapport présente comment notre équipe a relevé ce défi technique, transformant des composants électroniques et des lignes de code en une solution concrète pour l'environnement.</p>
      </div>
      <div class="intro-image">
        <img src="/2025-Team-IMSP-Docs/finale/assets/rosmaster.webp" alt="Rosmaster X3" />
      </div>
    </div>
  </div>

  <h2 class="architecture-title">Architecture du système</h2>

  <div class="architecture-grid">
    <a href="/2025-Team-IMSP-Docs/finale/dofbot-jetson-nano" class="arch-card">
      <img src="/2025-Team-IMSP-Docs/finale/assets/JetsonDOFBOT-Yahboom_800x.webp" alt="DOFBOT JETSON NANO" />
      <span class="arch-link">DOFBOT JETSON NANO</span>
    </a>
    
    <a href="/2025-Team-IMSP-Docs/finale/rosmaster-x3" class="arch-card">
      <img src="/2025-Team-IMSP-Docs/finale/assets/WhatsApp_Image_2026-01-11_at_7.25.23_PM.jpeg" alt="SYSTEME ROSMASTER X3" />
      <span class="arch-link">SYSTEME ROSMASTER X3</span>
    </a>
    
    <a href="/2025-Team-IMSP-Docs/finale/convoyeur" class="arch-card">
      <img src="/2025-Team-IMSP-Docs/finale/assets/13c5eeda-cbfa-4074-9289-348db2985a0d.png" alt="SYSTÈME CONVOYEUR" />
      <span class="arch-link">SYSTÈME CONVOYEUR</span>
    </a>
  </div>
</template>

<style scoped>
.finale-intro {
  margin: 2rem 0 3rem;
}

.intro-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: start;
}

.intro-text p {
  margin-bottom: 1.5rem;
  line-height: 1.8;
  text-align: justify;
  color: var(--vp-c-text-1);
}

.intro-image {
  position: sticky;
  top: 2rem;
}

.intro-image img {
  width: 100%;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.architecture-title {
  font-size: 2rem;
  font-weight: 700;
  margin: 3rem 0 2rem;
  color: var(--vp-c-text-1);
}

.architecture-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin: 2rem 0;
}

.arch-card {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
  text-decoration: none;
  display: block;
}

.arch-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 24px rgba(54, 192, 135, 0.2);
  border-color: rgba(54, 192, 135, 0.5);
}

.arch-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.arch-link {
  display: block;
  font-weight: 600;
  font-size: 1.1rem;
  color: var(--vp-c-brand-1);
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: all 0.3s;
}

.arch-card:hover .arch-link {
  background: rgba(54, 192, 135, 0.1);
}

@media (max-width: 768px) {
  .intro-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .intro-image {
    position: relative;
    top: 0;
  }
  
  .architecture-grid {
    grid-template-columns: 1fr;
  }
}
</style>
