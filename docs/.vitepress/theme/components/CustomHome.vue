<template>
  <div class="custom-home">
    <div class="hero-section">
      <!-- Navigation -->
      
      <nav class="custom-nav">
        <div class="logo animate__animated animate__fadeInDown">
          <img
            src="/logo.svg"
            alt="Logo"
            class="logo-img"
          />
          <span class="logo-text"
            ><span class="highlight-i">TEAM IMSP</span> Docs</span
          >
        </div>
        <ul class="nav-links animate__animated animate__fadeInDown animate__delay-1s" :class="{ active: menuOpen }">
          <li><a href="/2025-Team-IMSP-Docs/" @click="closeMenu">Home</a></li>
          <li><a href="/2025-Team-IMSP-Docs/team" @click="closeMenu">Team</a></li>
          <li class="mobile-github">
            <a
              href="https://github.com/beryl-07/TEAM-IMSP-TEKBOT-2025.git"
              target="_blank"
              @click="closeMenu"
            >
              GitHub
            </a>
          </li>
        </ul>
        <div class="nav-right">
          <a
            href="https://github.com/beryl-07/TEAM-IMSP-TEKBOT-2025.git"
            target="_blank"
            class="github-link desktop-github"
            title="GitHub"
          >
            <svg height="24" width="24" viewBox="0 0 16 16" fill="currentColor">
              <path
                d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"
              />
            </svg>
          </a>
          <button class="hamburger" @click="toggleMenu" :class="{ active: menuOpen }">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </nav>

      <!-- Hero Content -->
      <div class="hero-content">
        <div class="hero-left">
          <div class="hero-badge animate__animated animate__fadeIn">
            <span class="badge-icon"><i class="fas fa-trophy"></i></span>
            <span>TRC 2025 • FINALISTES</span>
          </div>
          <h3 class="hero-title animate__animated animate__fadeInLeft animate__delay-1s">IMSP TEAM<br><span class="highlight"><span class="nowrap">Tekbot Robotic</span><br><span class="nowrap">Challenge 2025</span></span></h3>
          <p class="hero-subtitle animate__animated animate__fadeInLeft animate__delay-1s">
            Développement d'un système robotique autonome pour la gestion intelligente des déchets urbains. 
            Une équipe de 10 étudiants passionnés de l'IMSP relève le défi de la résilience urbaine.
          </p>
          
          <div class="hero-stats animate__animated animate__fadeInUp animate__delay-1s">
            <div class="stat-badge">
              <div class="stat-number">10</div>
              <div class="stat-label">Membres</div>
            </div>
            <div class="stat-badge">
              <div class="stat-number">3</div>
              <div class="stat-label">Pôles</div>
            </div>
            <div class="stat-badge">
              <div class="stat-number">100%</div>
              <div class="stat-label">Innovation</div>
            </div>
          </div>

          <div class="hero-actions animate__animated animate__fadeInUp animate__delay-2s">
            <a href="/2025-Team-IMSP-Docs/test-it/test-one" class="btn-primary">
              <i class="fas fa-book-open"></i>
              <span>Documentation</span>
            </a>
            <a href="https://trc.tekbot.io/trc-2025/" class="btn-secondary">
              <i class="fas fa-arrow-right"></i>
              <span>En savoir plus</span>
            </a>
          </div>
        </div>

        <div class="hero-right">
          <div class="hero-image-wrapper animate__animated animate__fadeInRight animate__delay-1s">
            <div class="hero-image-bg"></div>
            <img
              src="/IMSP_TEAM.png"
              alt="IMSP Team"
              class="hero-image"
            />
            <div class="floating-badge animate__animated animate__bounceIn animate__delay-3s">
              <div class="icon"><i class="fas fa-robot"></i></div>
              <div class="badge-text">TRC<br/>2025</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- À propos du TRC Section -->
    <section class="about-trc-section">
      <div class="section-header animate__animated animate__fadeIn">
        <span class="section-tag"><i class="fas fa-bullseye"></i> LE CHALLENGE</span>
        <h2 class="section-title">À propos du TRC 2025</h2>
        <p class="section-desc">Porté par TEKBOT Robotics, le TRC 2025 nous pousse à créer des robots qui apportent des réponses concrètes aux besoins de nos villes</p>
      </div>

      <div class="trc-content">
        <div class="trc-card animate__animated animate__fadeInLeft">
          <div class="trc-icon"><i class="fas fa-globe"></i></div>
          <h3>Le Défi</h3>
          <p>Résilience Urbaine : Gestion Durable des Déchets. Un challenge qui répond aux besoins urgents de nos villes africaines.</p>
        </div>

        <div class="trc-card animate__animated animate__fadeInUp">
          <div class="trc-icon"><i class="fas fa-rocket"></i></div>
          <h3>Notre Mission</h3>
          <p>Développer un système robotique autonome capable de collecter, trier et gérer les déchets de manière intelligente et efficace.</p>
        </div>

        <div class="trc-card animate__animated animate__fadeInRight">
          <div class="trc-icon"><i class="fas fa-lightbulb"></i></div>
          <h3>L'Innovation</h3>
          <p>Navigation autonome, vision IA, manipulation précise : une synergie parfaite entre IT, Électronique et Mécanique.</p>
        </div>
      </div>

      <div class="trc-values">
        <h3 class="values-title">Nos Valeurs</h3>
        <div class="values-grid">
          <div class="value-item">
            <i class="fas fa-lightbulb"></i>
            <span>Innovation</span>
          </div>
          <div class="value-item">
            <i class="fas fa-users"></i>
            <span>Collaboration</span>
          </div>
          <div class="value-item">
            <i class="fas fa-trophy"></i>
            <span>Excellence</span>
          </div>
          <div class="value-item">
            <i class="fas fa-heart"></i>
            <span>Impact Social</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Roadmap Section -->
    <section class="roadmap-section">
      <div class="section-header animate__animated animate__fadeIn">
        <span class="section-tag"><i class="fas fa-route"></i> NOTRE PARCOURS</span>
        <h2 class="section-title">Feuille de Route</h2>
        <p class="section-desc">Du concept à la réalisation : les jalons de notre aventure TRC 2025</p>
      </div>

      <div class="timeline">
        <div class="timeline-item completed animate__animated animate__fadeInLeft">
          <div class="timeline-marker">
            <i class="fas fa-check"></i>
          </div>
          <div class="timeline-content">
            <div class="timeline-badge">PHASE 1 • TERMINÉ</div>
            <h3>Pré-sélection</h3>
            <p class="timeline-date">Juin 2025 à Juillet 2025</p>
            <p>10 tests techniques dans les 3 domaines : Électronique (gyroscope, boîte noire, afficheur), IT (POO, ROS2, pathfinding), Mécanique (CAO débutant à avancé)</p>
            <div class="timeline-stats">
              <span><i class="fas fa-tasks"></i> 10 Tests</span>
              <span><i class="fas fa-users"></i> 3 Pôles</span>
              <span><i class="fas fa-trophy"></i> Qualifiés</span>
            </div>
          </div>
        </div>

        <div class="timeline-item completed animate__animated animate__fadeInRight">
          <div class="timeline-marker">
            <i class="fas fa-check"></i>
          </div>
          <div class="timeline-content">
            <div class="timeline-badge">PHASE 2 • TERMINÉ</div>
            <h3>Développement & Finale</h3>
            <p class="timeline-date">Septembre 2025 - Janvier 2026</p>
            <p>Développement du système robotique complet pour EcoCity : navigation autonome ROS Master, collecte optimisée, tri IA avec DofBot, distribution ciblée</p>
            <div class="timeline-tech">
              <span class="tech-tag">ROS2</span>
              <span class="tech-tag">Vision IA</span>
              <span class="tech-tag">DofBot</span>
              <span class="tech-tag">Arduino</span>
            </div>
          </div>
        </div>

        <div class="timeline-item completed animate__animated animate__fadeInLeft">
          <div class="timeline-marker">
            <i class="fas fa-check"></i>
          </div>
          <div class="timeline-content">
            <div class="timeline-badge">PHASE 3 • TERMINÉ</div>
            <h3>Présentation Finale</h3>
            <p class="timeline-date">Samedi 17 Janvier 2026</p>
            <p>Grande finale : démonstration complète du système robotique, affrontement des deux meilleures équipes, présentation devant le jury</p>
            <div class="timeline-goal">
              <i class="fas fa-star"></i>
              <span>Objectif : Décrocher le titre de champions TRC 2025</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
      <div class="section-header animate__animated animate__fadeIn">
        <span class="section-tag"><i class="fas fa-circle-question"></i> QUESTIONS FRÉQUENTES</span>
        <h2 class="section-title">Tout ce qu'il faut savoir</h2>
        <p class="section-desc">Les réponses à vos questions sur notre projet et le TRC 2025</p>
      </div>

      <div class="faq-container">
        <div v-for="(faq, index) in faqs" :key="index" class="faq-item" @click="toggleFaq(index)">
          <div class="faq-question">
            <div class="faq-icon">
              <i :class="faq.icon"></i>
            </div>
            <h3>{{ faq.question }}</h3>
            <div class="faq-toggle" :class="{ active: openFaq === index }">
              <i class="fas fa-chevron-down"></i>
            </div>
          </div>
          <div class="faq-answer" :class="{ active: openFaq === index }">
            <p>{{ faq.answer }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Tests de Présélection Section -->
    <section class="preselection-section">
      <div class="section-header animate__animated animate__fadeIn">
        <span class="section-tag"><i class="fas fa-clipboard-check"></i> PHASE PRÉ-SÉLECTION</span>
        <h2 class="section-title">Tests de Présélection</h2>
        <p class="section-desc">4 semaines intensives où chaque pôle (IT, Électronique, Mécanique) développe ses compétences techniques fondamentales</p>
      </div>

      <div class="tests-grid">
        <!-- Test Semaine 1 -->
        <div class="test-card animate__animated animate__fadeInUp" style="animation-delay: 0.1s;">
          <div class="test-header">
            <div class="test-icon week"><i class="fas fa-code"></i></div>
            <div class="test-badge week">SEMAINE 1</div>
          </div>
          <h3 class="test-title">Fondamentaux</h3>
          <p class="test-description">
            Acquisition des bases : POO & UML, gyroscope MPU6050, et initiation CAO SolidWorks niveau débutant.
          </p>
          <div class="test-poles">
            <a href="/2025-Team-IMSP-Docs/test-it/test-one" class="pole-item it"><i class="fas fa-code"></i> IT : POO, UML, Arduino</a>
            <a href="/2025-Team-IMSP-Docs/test-electro/test-one" class="pole-item electro"><i class="fas fa-circle-dot"></i> Électro : Gyroscope MPU6050</a>
            <a href="/2025-Team-IMSP-Docs/test-meca/test-one" class="pole-item meca"><i class="fas fa-pen-ruler"></i> Méca : CAO débutant</a>
          </div>
          <a href="/2025-Team-IMSP-Docs/test-it/test-one" class="test-btn">
            <i class="fas fa-arrow-right"></i> Voir plus
          </a>
        </div>

        <!-- Test Semaine 2 -->
        <div class="test-card animate__animated animate__fadeInUp" style="animation-delay: 0.2s;">
          <div class="test-header">
            <div class="test-icon week"><i class="fas fa-satellite-dish"></i></div>
            <div class="test-badge week">SEMAINE 2</div>
          </div>
          <h3 class="test-title">Intégration Systèmes</h3>
          <p class="test-description">
            ROS2 avec capteurs/actionneurs, boîte noire embarquée, et progression CAO niveau intermédiaire.
          </p>
          <div class="test-poles">
            <a href="/2025-Team-IMSP-Docs/test-it/test-two" class="pole-item it"><i class="fas fa-network-wired"></i> IT : ROS2, Capteurs</a>
            <a href="/2025-Team-IMSP-Docs/test-electro/test-two" class="pole-item electro"><i class="fas fa-database"></i> Électro : Boîte noire</a>
            <a href="/2025-Team-IMSP-Docs/test-meca/test-two" class="pole-item meca"><i class="fas fa-box"></i> Méca : CAO intermédiaire</a>
          </div>
          <a href="/2025-Team-IMSP-Docs/test-it/test-two" class="test-btn">
            <i class="fas fa-arrow-right"></i> Voir plus
          </a>
        </div>

        <!-- Test Semaine 3 -->
        <div class="test-card animate__animated animate__fadeInUp" style="animation-delay: 0.3s;">
          <div class="test-header">
            <div class="test-icon week"><i class="fas fa-compass"></i></div>
            <div class="test-badge week">SEMAINE 3</div>
          </div>
          <h3 class="test-title">Navigation & Affichage</h3>
          <p class="test-description">
            Navigation autonome Gazebo, afficheur 7 segments, et CAO avancée avec modélisation complexe.
          </p>
          <div class="test-poles">
            <a href="/2025-Team-IMSP-Docs/test-it/test-three" class="pole-item it"><i class="fas fa-map-pin"></i> IT : Navigation, Gazebo</a>
            <a href="/2025-Team-IMSP-Docs/test-electro/test-three" class="pole-item electro"><i class="fas fa-table-cells"></i> Électro : Afficheur 7 seg</a>
            <a href="/2025-Team-IMSP-Docs/test-meca/test-three" class="pole-item meca"><i class="fas fa-cube"></i> Méca : CAO avancé</a>
          </div>
          <a href="/2025-Team-IMSP-Docs/test-it/test-three" class="test-btn">
            <i class="fas fa-arrow-right"></i> Voir plus
          </a>
        </div>

        <!-- Test Semaine 4 -->
        <div class="test-card animate__animated animate__fadeInUp" style="animation-delay: 0.4s;">
          <div class="test-header">
            <div class="test-icon week"><i class="fas fa-rocket"></i></div>
            <div class="test-badge week">SEMAINE 4</div>
          </div>
          <h3 class="test-title">Intégration Finale</h3>
          <p class="test-description">
            Synthèse et intégration de toutes les compétences acquises pour préparer le projet final du TRC 2025.
          </p>
          <div class="test-poles">
            <a href="/2025-Team-IMSP-Docs/test-final/it/it-part" class="pole-item it"><i class="fas fa-brain"></i> IT : Intégration ROS2</a>
            <a href="/2025-Team-IMSP-Docs/test-final/electro/electro-part" class="pole-item electro"><i class="fas fa-microchip"></i> Électro : Système complet</a>
            <a href="/2025-Team-IMSP-Docs/test-final/meca/meca-part" class="pole-item meca"><i class="fas fa-print"></i> Méca : Assemblage 3D</a>
          </div>
          <a href="/2025-Team-IMSP-Docs/test-final" class="test-btn">
            <i class="fas fa-arrow-right"></i> Voir plus
          </a>
        </div>
      </div>
    </section>

    <!-- Documentation Finale Section -->
    <section class="final-doc-section">
      <div class="section-container">
        <div class="section-header animate__animated animate__fadeIn">
          <span class="section-tag"><i class="fas fa-file-code"></i> PHASE FINALE</span>
          <h2 class="section-title">Documentation Finale</h2>
          <p class="section-desc">Les 3 composantes majeures de notre système robotique pour le TRC 2025</p>
        </div>

        <div class="final-doc-grid">
          <!-- Rosmaster X3 -->
          <div class="doc-category-card rosmaster animate__animated animate__fadeInUp" style="animation-delay: 0.1s;">
            <div class="doc-card-header">
              <div class="doc-icon-wrapper">
                <i class="fas fa-robot"></i>
              </div>
              <h3>Rosmaster X3</h3>
            </div>
            <p class="doc-description">Robot mobile omnidirectionnel équipé de ROS2 pour la navigation autonome et la détection intelligente</p>
            <div class="doc-features">
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Navigation ROS2 & SLAM</div>
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Vision IA embarquée</div>
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Détection des déchets</div>
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Communication ESP32</div>
            </div>
            <a href="/2025-Team-IMSP-Docs/finale/trc2025-finale/systeme-rosmaster-x3/systeme-rosmaster" class="doc-btn">
              <i class="fas fa-book-open"></i>
              <span>Accéder à la documentation</span>
            </a>
          </div>

          <!-- Convoyeur -->
          <div class="doc-category-card conveyor animate__animated animate__fadeInUp" style="animation-delay: 0.2s;">
            <div class="doc-card-header">
              <div class="doc-icon-wrapper">
                <i class="fas fa-arrows-left-right"></i>
              </div>
              <h3>Système Convoyeur</h3>
            </div>
            <p class="doc-description">Convoyeur intelligent pour le tri et l'acheminement automatique des déchets collectés</p>
            <div class="doc-features">
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Tri automatisé</div>
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Capteurs de détection</div>
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Contrôle motorisé</div>
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Synchronisation système</div>
            </div>
            <a href="/2025-Team-IMSP-Docs/finale/trc2025-finale/systeme-convoyeur/systeme-convoyeur" class="doc-btn">
              <i class="fas fa-book-open"></i>
              <span>Accéder à la documentation</span>
            </a>
          </div>

          <!-- DofBot Jetson Nano -->
          <div class="doc-category-card dofbot animate__animated animate__fadeInUp" style="animation-delay: 0.3s;">
            <div class="doc-card-header">
              <div class="doc-icon-wrapper">
                <i class="fas fa-microchip"></i>
              </div>
              <h3>DofBot Jetson Nano</h3>
            </div>
            <p class="doc-description">Bras robotique 5 DOF piloté par Jetson Nano pour la manipulation précise des objets</p>
            <div class="doc-features">
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Contrôle 5 axes</div>
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Vision caméra embarquée</div>
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Préhension adaptative</div>
              <div class="doc-feature"><i class="fas fa-circle-check"></i> Interface ROS2</div>
            </div>
            <a href="/2025-Team-IMSP-Docs/finale/trc2025-finale/dofbot-jetson-nano/dofbot-jetson-nano" class="doc-btn">
              <i class="fas fa-book-open"></i>
              <span>Accéder à la documentation</span>
            </a>
          </div>
        </div>

        <!-- Bannière d'information -->
        <div class="final-doc-banner animate__animated animate__fadeInUp" style="animation-delay: 0.4s;">
          <div class="banner-icon">
            <i class="fas fa-rocket"></i>
          </div>
          <div class="banner-content">
            <h4>Prêt pour la finale !</h4>
            <p>Notre système robotique intégré (Rosmaster X3 + Convoyeur + DofBot) est opérationnel et optimisé pour le TRC 2025. Consultez la documentation complète de chaque composante.</p>
          </div>
          <div class="banner-stats">
            <div class="stat">
              <i class="fas fa-bolt"></i>
              <span>100%</span>
              <small>Opérationnel</small>
            </div>
            <div class="stat">
              <i class="fas fa-calendar-days"></i>
              <span>17 Jan</span>
              <small>Finale TRC</small>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact/Footer Section -->
    <section class="footer-section">
      <div class="footer-content">
        <div class="footer-col">
          <div class="footer-logo">
            <img src="/2025-Team-IMSP-Docs/logo.svg" alt="IMSP Logo" class="footer-logo-img" />
            <h3>TEAM IMSP</h3>
          </div>
          <p class="footer-desc">
            Une équipe passionnée d'étudiants de l'IMSP, unis pour relever le défi du TRC 2025. 
            Notre mission : innover et repousser les limites de la robotique.
          </p>
          <div class="footer-social">
            <a href="https://github.com/beryl-07/TEAM-IMSP-TEKBOT-2025.git" target="_blank" title="GitHub">
              <i class="fab fa-github"></i>
            </a>
            <a href="https://www.linkedin.com" target="_blank" title="LinkedIn">
              <i class="fab fa-linkedin"></i>
            </a>
            <a href="mailto:team.imsp@example.com" title="Email">
              <i class="fas fa-envelope"></i>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Navigation</h4>
          <ul class="footer-links">
            <li><a href="/2025-Team-IMSP-Docs/">Accueil</a></li>
            <li><a href="/2025-Team-IMSP-Docs/team">Équipe</a></li>
            <li><a href="/2025-Team-IMSP-Docs/test-it/test-one">Documentation</a></li>
            <li><a href="https://trc.tekbot.io/trc-2025/" target="_blank">TRC 2025</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Ressources</h4>
          <ul class="footer-links">
            <li><a href="/2025-Team-IMSP-Docs/test-it/test-one">Test IT</a></li>
            <li><a href="/2025-Team-IMSP-Docs/test-electro/test-one">Test Électronique</a></li>
            <li><a href="/2025-Team-IMSP-Docs/test-meca/test-one">Test Mécanique</a></li>
            <li><a href="https://github.com/beryl-07/TEAM-IMSP-TEKBOT-2025.git" target="_blank">GitHub</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>TRC 2025</h4>
          <ul class="footer-links">
            <li><a href="https://trc.tekbot.io" target="_blank">Site Officiel</a></li>
            <li><a href="https://trc.tekbot.io/soutenir-trc/" target="_blank">Soutenir l'événement</a></li>
            <li><a href="https://www.linkedin.com/company/tekbot-robotics/" target="_blank">TEKBOT Robotics</a></li>
          </ul>
          <div class="footer-badge">
            <img src="https://trc.tekbot.io/wp-content/uploads/2025/01/Logo-1.svg" alt="TRC Logo" class="trc-logo" />
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2025 TEAM IMSP • IMSP - Université d'Abomey-Calavi • Tous droits réservés</p>
        <p class="footer-tagline">
          <i class="fas fa-rocket"></i> Innovation • 
          <i class="fas fa-handshake"></i> Collaboration • 
          <i class="fas fa-trophy"></i> Excellence
        </p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const menuOpen = ref(false)
const openFaq = ref(null)

// Load external resources
onMounted(() => {
  // Load Animate.css
  if (!document.querySelector('link[href*="animate.css"]')) {
    const animateLink = document.createElement('link')
    animateLink.rel = 'stylesheet'
    animateLink.href = 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'
    document.head.appendChild(animateLink)
  }
})

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

const closeMenu = () => {
  menuOpen.value = false
}

const toggleFaq = (index) => {
  openFaq.value = openFaq.value === index ? null : index
}

const faqs = [
  {
    icon: 'fas fa-robot',
    question: "Qu'est-ce que le TEKBOT Robotics Challenge (TRC) ?",
    answer: "Le TRC est une compétition internationale de robotique organisée au Bénin qui rassemble les meilleures équipes d'étudiants pour relever des défis techniques innovants. Le thème 2025 'Résilience Urbaine : Gestion Durable des Déchets' nous pousse à créer des solutions concrètes pour nos villes."
  },
  {
    icon: 'fas fa-users',
    question: "Qui compose l'équipe TEAM IMSP ?",
    answer: "Notre équipe est composée de 10 étudiants passionnés de l'IMSP (Institut de Mathématiques et de Sciences Physiques), répartis en 3 pôles : IT (6 membres), Électronique (2 membres) et Mécanique (2 membres). Chaque membre apporte son expertise unique au projet."
  },
  {
    icon: 'fas fa-microchip',
    question: "Quelles technologies utilisez-vous ?",
    answer: "Nous utilisons ROS2 pour la navigation autonome, des systèmes de vision IA pour la détection et le tri des déchets, le robot DofBot pour la manipulation, Arduino et ESP32 pour l'électronique embarquée, et SolidWorks pour la conception mécanique 3D."
  },
  {
    icon: 'fas fa-calendar-days',
    question: "Quand et où aura lieu la compétition ?",
    answer: "La grande finale du TRC 2025 aura lieu le 10 juillet 2025 au Bénin. Les deux meilleures équipes s'affronteront en démonstration live de leurs systèmes robotiques devant un jury d'experts."
  },
  {
    icon: 'fas fa-trophy',
    question: "Quels sont vos objectifs pour le TRC 2025 ?",
    answer: "Notre objectif principal est de décrocher le titre de champions du TRC 2025 en développant un système robotique performant, innovant et capable de gérer efficacement les déchets urbains. Nous visons l'excellence technique et la créativité."
  },
  {
    icon: 'fas fa-gear',
    question: "Comment le robot fonctionne-t-il ?",
    answer: "Notre robot navigue de manière autonome dans EcoCity, détecte et collecte les déchets grâce à la vision IA, les trie automatiquement selon leur type, et les distribue dans les zones de recyclage appropriées. Tout cela en 5 minutes chrono !"
  }
]
</script>

<style scoped>
/* Reset et styles de base */
.custom-home {
  overflow-x: hidden;
  width: 100%;
  position: relative;
}

.custom-home * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.hero-section {
  background: linear-gradient(135deg, #2c2d41 0%, #1a1b2e 100%);
  min-height: 100vh;
  padding: 0;
  margin-left: calc(-50vw + 50%);
  margin-right: calc(-50vw + 50%);
  margin-bottom: 0;
  margin-top: calc(-1 * var(--vp-nav-height));
  position: relative;
  overflow: hidden;
  width: 100vw;
  max-width: 100vw;
}

/* Décoration de fond */
.hero-section::before {
  content: "";
  position: absolute;
  top: 15%;
  left: 5%;
  width: 120px;
  height: 120px;
  background: rgba(139, 140, 234, 0.3);
  border-radius: 50%;
  z-index: 1;
}

.hero-section::after {
  content: "";
  position: absolute;
  top: 25%;
  left: 50%;
  width: 100px;
  height: 100px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  z-index: 1;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes pulse-glow {
  0%, 100% {
    box-shadow: 0 0 20px rgba(54, 192, 135, 0.3);
  }
  50% {
    box-shadow: 0 0 40px rgba(54, 192, 135, 0.6);
  }
}

@keyframes rotate-slow {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Navigation personnalisée */
.custom-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 5%;
  position: relative;
  z-index: 1000;
  max-width: 100%;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: clamp(1.2rem, 3vw, 2rem);
  font-weight: 700;
  color: white;
  z-index: 1001;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.05);
}

.logo-img {
  height: clamp(30px, 5vw, 40px);
  width: auto;
  transition: all 0.4s ease;
}

.logo:hover .logo-img {
  transform: rotate(360deg);
  filter: drop-shadow(0 0 10px rgba(54, 192, 135, 0.6));
}

.logo-text {
  font-size: clamp(1.2rem, 3vw, 2rem);
  font-weight: 700;
  color: white;
}

.highlight-i {
  color: #36c087;
}

.nav-links {
  display: flex;
  gap: 40px;
  list-style: none;
  margin-left: auto;
  margin-right: 40px;
  transition: all 0.3s ease;
}

.nav-links a {
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  font-weight: 500;
  font-size: 1rem;
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  position: relative;
  display: inline-block;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: #36c087;
  transition: width 0.3s ease;
}

.nav-links a:hover {
  color: #36c087;
  transform: translateY(-2px);
}

.nav-links a:hover::after {
  width: 100%;
}

.mobile-github {
  display: none;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.github-link {
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  text-decoration: none;
}

.github-link:hover {
  color: #36c087;
  background: rgba(168, 255, 53, 0.1);
  transform: scale(1.2) rotate(360deg);
  box-shadow: 0 0 20px rgba(54, 192, 135, 0.5);
}

.desktop-github {
  display: flex;
}

/* Hamburger Menu */
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 10px;
  z-index: 1001;
}

.hamburger span {
  width: 25px;
  height: 3px;
  background: white;
  transition: all 0.3s ease;
  border-radius: 3px;
}

.hamburger.active span:nth-child(1) {
  transform: rotate(45deg) translate(8px, 8px);
}

.hamburger.active span:nth-child(2) {
  opacity: 0;
}

.hamburger.active span:nth-child(3) {
  transform: rotate(-45deg) translate(7px, -7px);
}

.register-btn {
  padding: 12px 35px;
  border: 2px solid #36c087;
  border-radius: 50px;
  background: transparent;
  color: white;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  text-decoration: none;
  display: inline-block;
}

.register-btn:hover {
  background: #36c087;
  color: #1a1b2e;
}

/* Contenu Hero */
.hero-content {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 60px;
  align-items: center;
  padding: 40px 5%;
  position: relative;
  z-index: 2;
  max-width: 100%;
  margin-top: clamp(20px, 5vw, 60px);
}


.hero-left {
}

.hero-title {
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 800;
  color: white;
  line-height: 1.2;
  margin-bottom: clamp(20px, 4vw, 50px);
  text-transform: uppercase;
  letter-spacing: -1px;
}

.hero-title .highlight {
  color: #36c087;
  display: block;
}

.hero-title .nowrap {
  white-space: nowrap;
}

.hero-actions {
  display: flex;
  gap: 20px;
  margin-top: clamp(20px, 3vw, 40px);
  align-items: center;
  flex-wrap: wrap;
}

.btn-primary {
  padding: clamp(14px, 2vw, 18px) clamp(30px, 4vw, 45px);
  background: #36c087;
  color: #1a1b2e;
  border: none;
  border-radius: 50px;
  font-weight: 700;
  font-size: clamp(0.9rem, 1.5vw, 1.1rem);
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  text-align: center;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.btn-primary i {
  font-size: 1.2rem;
  transition: transform 0.3s ease;
  z-index: 2;
  position: relative;
}

.btn-primary span {
  z-index: 2;
  position: relative;
}

.btn-primary::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  transform: translate(-50%, -50%);
  transition: width 0.6s, height 0.6s;
}

.btn-primary:hover::before {
  width: 300px;
  height: 300px;
}

.btn-primary:hover {
  background: #2da871;
  transform: translateY(-5px) scale(1.05);
  box-shadow: 0 15px 40px rgba(54, 192, 135, 0.5);
}

.btn-primary:hover i {
  transform: translateY(-3px);
}

.btn-secondary {
  color: white;
  text-decoration: none;
  font-weight: 600;
  font-size: clamp(0.9rem, 1.5vw, 1.1rem);
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  position: relative;
}

.btn-secondary i {
  font-size: 1.1rem;
  transition: transform 0.3s ease;
}

.btn-secondary:hover {
  color: #36c087;
  gap: 15px;
}

.btn-secondary:hover i {
  transform: translateX(5px);
}

.btn-secondary::after {
  content: "→";
  font-size: 1.3rem;
  transition: transform 0.3s ease;
}

.btn-secondary:hover::after {
  transform: translateX(5px);
}

/* Section Hero droite */
.hero-right {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.hero-image-wrapper {
  position: relative;
  width: 100%;
  max-width: 860px;
  transition: transform 0.5s ease;
}

.hero-image-wrapper:hover {
  transform: scale(1.05);
}

.hero-image-bg {
  width: 100%;
  max-width: 800px;
  height: 0;
  padding-bottom: 100%;
  background: linear-gradient(
    135deg,
    rgba(139, 140, 234, 0.6) 0%,
    rgba(139, 140, 234, 0.2) 100%
  );
  border-radius: 50% 50% 40% 60% / 50% 50% 50% 50%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
  animation: pulse-glow 3s ease-in-out infinite;
}

.hero-image {
  position: relative;
  z-index: 2;
  width: 100%;
  height: auto;
  border-radius: 30px;
  transition: all 0.5s ease;
  filter: brightness(1);
}

.hero-image-wrapper:hover .hero-image {
  filter: brightness(1.1) contrast(1.05);
  box-shadow: 0 20px 60px rgba(54, 192, 135, 0.4);
}

.floating-badge {
  position: absolute;
  bottom: clamp(-10px, -2vw, -20px);
  right: clamp(-10px, -2vw, -20px);
  width: clamp(80px, 15vw, 120px);
  height: clamp(80px, 15vw, 120px);
  background: linear-gradient(135deg, #5B5BDCD4 0%, #4849b8 100%);
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: clamp(0.6rem, 1.2vw, 0.8rem);
  text-align: center;
  padding: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  z-index: 3;
  animation: rotate-slow 20s linear infinite, pulse-glow 2s ease-in-out infinite;
  transition: transform 0.3s ease;
  cursor: pointer;
}

.floating-badge:hover {
  transform: scale(1.15);
  animation-play-state: paused;
}

.floating-badge .icon {
  font-size: clamp(1.5rem, 3vw, 2rem);
  margin-bottom: 5px;
  color: var(--vp-c-brand-1);
}

.floating-badge .icon i {
  display: block;
}

/* Stats section */
.stats-section {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 80px;
  padding: 40px 80px 60px;
  align-items: center;
  position: relative;
  z-index: 2;
}

.rating-box {
  display: flex;
  align-items: center;
  gap: 20px;
}

.rating-icon {
  width: 80px;
  height: 80px;
  background: rgba(139, 140, 234, 0.3);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  color: #8b8cea;
}

.rating-info {
  color: white;
}

.rating-stars {
  color: #36c087;
  font-size: 1.2rem;
  margin-bottom: 5px;
}

.rating-score {
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 5px;
}

.rating-text {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.7);
}

.stats-grid {
  display: flex;
  justify-content: space-around;
  gap: 40px;
}

.stat-item {
  text-align: center;
  color: white;
}

.stat-number {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 8px;
  background: linear-gradient(135deg, #ffffff 0%, #36c087 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-label {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
}

/* Features Section */
.features-section {
  padding: clamp(40px, 8vw, 80px) 5%;
  background: white;
  max-width: 100%;
  overflow-x: hidden;
}

.features-title {
  text-align: center;
  font-size: clamp(1.8rem, 4vw, 2.5rem);
  font-weight: 700;
  color: #1a1b2e;
  margin-bottom: clamp(30px, 5vw, 50px);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
  gap: clamp(20px, 4vw, 40px);
}

.feature-card {
  background: #f8f9fa;
  border-radius: 20px;
  padding: clamp(25px, 4vw, 40px) clamp(20px, 3vw, 30px);
  text-align: left;
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 2px solid transparent;
  position: relative;
  overflow: hidden;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(54, 192, 135, 0.1), transparent);
  transition: left 0.6s ease;
}

.feature-card:hover::before {
  left: 100%;
}

.feature-card:hover {
  transform: translateY(-15px) scale(1.02);
  border-color: #36c087;
  box-shadow: 0 25px 50px rgba(54, 192, 135, 0.2);
}

.feature-icon {
  font-size: clamp(2rem, 5vw, 3rem);
  margin-bottom: 20px;
  display: inline-block;
  transition: all 0.4s ease;
}

.feature-card:hover .feature-icon {
  transform: scale(1.2) rotate(10deg);
  filter: drop-shadow(0 5px 15px rgba(54, 192, 135, 0.4));
}

.feature-title {
  font-size: clamp(1.2rem, 2.5vw, 1.5rem);
  font-weight: 700;
  color: #1a1b2e;
  margin-bottom: 15px;
}

.feature-description {
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: clamp(0.9rem, 1.5vw, 1rem);
}

.feature-link {
  color: #36c087;
  text-decoration: none;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  font-size: clamp(0.9rem, 1.5vw, 1rem);
}

.feature-link:hover {
  gap: 15px;
  transform: translateX(5px);
}

.feature-link::after {
  content: "→";
  transition: transform 0.3s ease;
}

.feature-link:hover::after {
  transform: translateX(5px) scale(1.2);
}

/* Responsive */
@media (max-width: 1024px) {
  .tests-grid {
    grid-template-columns: 1fr;
  }

  /* Sur mobile, la 4ème carte prend aussi toute la largeur normalement */
  .test-card:nth-child(4) {
    grid-column: 1;
    max-width: 100%;
  }

  .hero-content {
    grid-template-columns: 1fr;
    gap: 40px;
    padding: 30px 5%;
  }

  .hero-left {
    padding-right: 0;
    text-align: center;
  }

  .hero-title {
    font-size: clamp(2rem, 6vw, 3rem);
  }

  .hero-actions {
    justify-content: center;
  }

  .hero-right {
    order: -1;
  }

  .stats-section {
    grid-template-columns: 1fr;
    padding: 40px 5%;
    gap: 40px;
  }

  .rating-box {
    justify-content: center;
  }

  .stats-grid {
    justify-content: center;
  }

  .custom-nav {
    padding: 20px 5%;
  }

  .nav-links {
    gap: 30px;
    margin-right: 20px;
  }
}

@media (max-width: 768px) {
  .hero-section {
    min-height: auto;
    padding-bottom: 40px;
  }

  .hamburger {
    display: flex;
  }

  .desktop-github {
    display: none;
  }

  .mobile-github {
    display: block;
  }

  .nav-links {
    position: fixed;
    top: 0;
    right: -100%;
    height: 100vh;
    width: 70%;
    max-width: 300px;
    background: rgba(26, 27, 46, 0.98);
    backdrop-filter: blur(10px);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 30px;
    margin: 0;
    padding: 40px;
    transition: right 0.3s ease;
    box-shadow: -5px 0 15px rgba(0, 0, 0, 0.3);
  }

  .nav-links.active {
    right: 0;
  }

  .nav-links li {
    width: 100%;
    text-align: center;
  }

  .nav-links a {
    display: block;
    padding: 10px;
    font-size: 1.1rem;
    width: 100%;
  }

  .hero-content {
    padding: 20px 5%;
    gap: 30px;
    margin-top: 20px;
  }

  .hero-title {
    font-size: clamp(1.8rem, 8vw, 2.5rem);
    margin-bottom: 20px;
  }

  .hero-title .highlight {
    display: block;
  }

  .hero-actions {
    flex-direction: column;
    width: 100%;
    gap: 15px;
  }

  .btn-primary,
  .btn-secondary {
    width: 100%;
    justify-content: center;
  }

  .hero-right {
    padding: 10px;
  }

  .hero-image-wrapper {
    max-width: 350px;
  }

  .stats-grid {
    flex-direction: column;
    gap: 30px;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .feature-card {
    padding: 30px 20px;
  }

  .logo-text {
    font-size: clamp(1rem, 4vw, 1.5rem);
  }

  .logo-img {
    height: clamp(25px, 6vw, 35px);
  }
}

@media (max-width: 480px) {
  .hero-section::before {
    width: 80px;
    height: 80px;
  }

  .hero-section::after {
    width: 70px;
    height: 70px;
  }

  .custom-nav {
    padding: 15px 4%;
  }

  .hero-content {
    padding: 15px 4%;
  }

  .hero-title {
    font-size: clamp(1.5rem, 9vw, 2rem);
    line-height: 1.3;
  }

  .btn-primary {
    padding: 14px 30px;
    font-size: 0.95rem;
  }

  .btn-secondary {
    font-size: 0.95rem;
  }

  .features-section {
    padding: 40px 4%;
  }

  .feature-card {
    padding: 25px 15px;
  }

  .floating-badge {
    width: 70px;
    height: 70px;
    bottom: -5px;
    right: -5px;
  }

  .nav-links {
    width: 80%;
  }
}

@media (min-width: 1400px) {
  .hero-content {
    max-width: 1400px;
    margin-left: auto;
    margin-right: auto;
  }

  .features-section {
    max-width: 1400px;
    margin-left: auto;
    margin-right: auto;
  }
}

/* Hero Badges & Stats */
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: rgba(54, 192, 135, 0.1);
  border: 1px solid rgba(54, 192, 135, 0.3);
  border-radius: 50px;
  color: #36c087;
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: 1.5rem;
  animation: pulse-glow 2s ease-in-out infinite;
}

.badge-icon {
  font-size: 1.2rem;
  animation: float 3s ease-in-out infinite;
}

.badge-icon i {
  color: #ffd700;
}

.hero-subtitle {
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  margin-bottom: 2rem;
  max-width: 600px;
}

.hero-stats {
  display: flex;
  gap: 2rem;
  margin-bottom: 2rem;
}

.stat-badge {
  text-align: center;
}

.stat-badge .stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: #36c087;
  line-height: 1;
  margin-bottom: 0.3rem;
}

.stat-badge .stat-label {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.7);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.floating-badge .badge-text {
  font-size: 0.7rem;
  font-weight: 700;
  line-height: 1.2;
  margin-top: 5px;
}

/* Section Styles Communes */
.about-trc-section,
.roadmap-section,
.faq-section {
  padding: 80px 5%;
  max-width: 1400px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 60px;
}

.section-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 8px 20px;
  background: rgba(54, 192, 135, 0.1);
  border-radius: 50px;
  color: #36c087;
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: 1rem;
  letter-spacing: 1px;
}

.section-tag i {
  font-size: 1rem;
}

.section-title {
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 800;
  color: #1a1b2e;
  margin-bottom: 1rem;
}

.section-desc {
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: #666;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
}

/* À propos du TRC Section */
.trc-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  margin-bottom: 60px;
}

.trc-card {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  padding: 40px 30px;
  border-radius: 20px;
  border: 2px solid transparent;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative;
  overflow: hidden;
}

.trc-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, #36c087, #2da871);
  transform: scaleX(0);
  transition: transform 0.4s ease;
}

.trc-card:hover::before {
  transform: scaleX(1);
}

.trc-card:hover {
  transform: translateY(-10px);
  border-color: #36c087;
  box-shadow: 0 20px 60px rgba(54, 192, 135, 0.2);
}

.trc-icon {
  font-size: 3rem;
  margin-bottom: 1.5rem;
  animation: float 3s ease-in-out infinite;
}

.trc-icon i {
  display: block;
  background: linear-gradient(135deg, 
    var(--vp-c-brand-1) 0%, 
    #36c087 25%,
    #667eea 75%,
    var(--vp-c-brand-2) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  filter: drop-shadow(0 0 20px rgba(54, 192, 135, 0.3));
}

.trc-card h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1b2e;
  margin-bottom: 1rem;
}

.trc-card p {
  color: #666;
  line-height: 1.6;
  font-size: 1rem;
}

.trc-values {
  text-align: center;
  padding: 40px;
  background: linear-gradient(135deg, #2c2d41 0%, #1a1b2e 100%);
  border-radius: 20px;
  color: white;
}

.values-title {
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 2rem;
  color: #36c087;
}

.values-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 30px;
}

.value-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  transition: all 0.3s ease;
}

.value-item:hover {
  background: rgba(54, 192, 135, 0.1);
  transform: translateY(-5px);
}

.value-item i {
  font-size: 2rem;
  color: #36c087;
}

.value-item span {
  font-weight: 600;
  font-size: 1rem;
}

/* Roadmap/Timeline */
.timeline {
  position: relative;
  max-width: 900px;
  margin: 0 auto;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 30px;
  top: 0;
  bottom: 0;
  width: 3px;
  background: linear-gradient(180deg, #36c087 0%, #2da871 100%);
}

.timeline-item {
  position: relative;
  padding-left: 80px;
  margin-bottom: 60px;
}

.timeline-marker {
  position: absolute;
  left: 15px;
  top: 0;
  width: 40px;
  height: 40px;
  background: #fff;
  border: 4px solid #36c087;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
  transition: all 0.3s ease;
}

.timeline-marker i {
  color: #36c087;
  font-size: 1.2rem;
}

.timeline-item:hover .timeline-marker {
  transform: scale(1.2);
  box-shadow: 0 0 20px rgba(54, 192, 135, 0.5);
}

.timeline-item.completed .timeline-marker {
  background: #36c087;
  border-color: #36c087;
}

.timeline-item.completed .timeline-marker i {
  color: white;
}

.timeline-item.active .timeline-marker {
  animation: pulse-glow 2s ease-in-out infinite;
}

.timeline-item.upcoming .timeline-marker {
  background: #f8f9fa;
  border-color: #ddd;
}

.timeline-item.upcoming .timeline-marker i {
  color: #999;
}

.timeline-content {
  background: white;
  padding: 30px;
  border-radius: 15px;
  border: 2px solid #f0f0f0;
  transition: all 0.3s ease;
}

.timeline-item:hover .timeline-content {
  border-color: #36c087;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.timeline-badge {
  display: inline-block;
  padding: 6px 15px;
  background: #f0f0f0;
  border-radius: 50px;
  font-size: 0.8rem;
  font-weight: 700;
  color: #666;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.timeline-badge.current {
  background: rgba(54, 192, 135, 0.1);
  color: #36c087;
}

.timeline-content h3 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #1a1b2e;
  margin-bottom: 0.5rem;
}

.timeline-date {
  font-size: 0.95rem;
  color: #36c087;
  font-weight: 600;
  margin-bottom: 1rem;
}

.timeline-content > p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.timeline-stats,
.timeline-tech,
.timeline-goal {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-top: 1rem;
}

.timeline-stats span {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 8px 15px;
  background: rgba(54, 192, 135, 0.1);
  border-radius: 50px;
  font-size: 0.9rem;
  color: #36c087;
  font-weight: 600;
}

.timeline-stats i {
  font-size: 0.9rem;
}

.tech-tag {
  padding: 8px 15px;
  background: linear-gradient(135deg, #2c2d41 0%, #1a1b2e 100%);
  color: white;
  border-radius: 50px;
  font-size: 0.85rem;
  font-weight: 600;
}

.timeline-goal {
  padding: 15px 20px;
  background: linear-gradient(135deg, rgba(54, 192, 135, 0.1) 0%, rgba(54, 192, 135, 0.05) 100%);
  border-radius: 10px;
  border-left: 4px solid #36c087;
}

.timeline-goal i {
  color: #36c087;
  font-size: 1.2rem;
  margin-right: 10px;
}

.timeline-goal span {
  color: #1a1b2e;
  font-weight: 600;
}

/* FAQ Section */
.faq-container {
  max-width: 900px;
  margin: 0 auto;
}

.faq-item {
  background: white;
  border-radius: 15px;
  margin-bottom: 20px;
  border: 2px solid #f0f0f0;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
}

.faq-item:hover {
  border-color: #36c087;
  box-shadow: 0 5px 20px rgba(54, 192, 135, 0.1);
}

.faq-question {
  padding: 25px 30px;
  display: flex;
  align-items: center;
  gap: 20px;
  transition: all 0.3s ease;
}

.faq-icon {
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, rgba(54, 192, 135, 0.15), rgba(54, 192, 135, 0.08));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: all 0.3s ease;
}

.faq-item:hover .faq-icon {
  background: linear-gradient(135deg, rgba(54, 192, 135, 0.25), rgba(54, 192, 135, 0.15));
  transform: scale(1.1) rotate(5deg);
}

.faq-icon i {
  color: #36c087;
  font-size: 1.5rem;
  stroke-width: 2;
}

.faq-question h3 {
  flex: 1;
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1b2e;
}

.faq-toggle {
  width: 30px;
  height: 30px;
  background: rgba(54, 192, 135, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  flex-shrink: 0;
}

.faq-toggle i {
  color: #36c087;
  transition: transform 0.3s ease;
}

.faq-toggle.active i {
  transform: rotate(180deg);
}

.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease, padding 0.4s ease;
}

.faq-answer.active {
  max-height: 500px;
  padding: 0 30px 25px 100px;
}

.faq-answer p {
  color: #666;
  line-height: 1.7;
  font-size: 1rem;
}

/* Footer Section */
.footer-section {
  background: linear-gradient(135deg, #2c2d41 0%, #1a1b2e 100%);
  color: white;
  padding: 60px 5% 30px;
}

/* ============================================ */
/* Tests de Présélection Section */
/* ============================================ */
.preselection-section {
  padding: 5rem 2rem;
  background: linear-gradient(135deg, 
    #f5f7fa 0%, 
    #e8ecf1 25%,
    #dfe4ea 50%,
    #e8ecf1 75%,
    #f5f7fa 100%);
  position: relative;
}

.preselection-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 20%, rgba(102, 126, 234, 0.03) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(54, 192, 135, 0.03) 0%, transparent 50%);
  pointer-events: none;
}

.tests-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  max-width: 1400px;
  margin: 3rem auto 0;
}

/* La 4ème carte s'étale sur toute la ligne */
.test-card:nth-child(4) {
  grid-column: 1 / -1;
  max-width: 800px;
  margin: 0 auto;
  width: 100%;
}

.test-card {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 2px solid transparent;
  position: relative;
  overflow: hidden;
}

.test-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 5px;
  background: linear-gradient(90deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  transform: scaleX(0);
  transition: transform 0.4s ease;
}

.test-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
  border-color: var(--vp-c-brand-1);
}

.test-card:hover::before {
  transform: scaleX(1);
}

.test-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.test-icon {
  width: 70px;
  height: 70px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  color: white;
  transition: all 0.3s ease;
}

.test-icon.week {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.test-card:hover .test-icon {
  transform: rotate(360deg) scale(1.1);
}

.test-badge {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.test-badge.week {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.test-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: #1a1a2e;
}

.test-description {
  color: #666;
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.test-poles {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  margin-bottom: 1.5rem;
}

.pole-item {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02));
  padding: 0.7rem 1rem;
  border-radius: 10px;
  font-size: 0.9rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  border-left: 3px solid;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  text-decoration: none;
  cursor: pointer;
}

a.pole-item {
  display: flex;
  text-decoration: none;
}

.pole-item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 0;
  transition: width 0.3s ease;
  opacity: 0.1;
}

.pole-item:hover::before {
  width: 100%;
}

.pole-item i {
  font-size: 1.2rem;
  flex-shrink: 0;
  stroke-width: 2;
}

.pole-item.it {
  border-left-color: #667eea;
  color: #667eea;
}

.pole-item.it::before {
  background: linear-gradient(90deg, #667eea, transparent);
}

.pole-item.it:hover {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(102, 126, 234, 0.05));
  transform: translateX(5px);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
}

.pole-item.electro {
  border-left-color: #f59e0b;
  color: #d97706;
}

.pole-item.electro::before {
  background: linear-gradient(90deg, #f59e0b, transparent);
}

.pole-item.electro:hover {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(245, 158, 11, 0.05));
  transform: translateX(5px);
  box-shadow: 0 4px 15px rgba(245, 158, 11, 0.2);
}

.pole-item.meca {
  border-left-color: #0891b2;
  color: #0e7490;
}

.pole-item.meca::before {
  background: linear-gradient(90deg, #0891b2, transparent);
}

.pole-item.meca:hover {
  background: linear-gradient(135deg, rgba(8, 145, 178, 0.1), rgba(8, 145, 178, 0.05));
  transform: translateX(5px);
  box-shadow: 0 4px 15px rgba(8, 145, 178, 0.2);
}

.test-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 12px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.test-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.5s ease;
}

.test-btn:hover {
  transform: translateX(5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

.test-btn:hover::before {
  left: 100%;
}

.test-btn i {
  transition: transform 0.3s ease;
}

.test-btn:hover i {
  transform: translateX(5px);
}

/* ============================================ */
/* Documentation Finale Section */
/* ============================================ */
.final-doc-section {
  padding: 6rem 2rem;
  background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
  position: relative;
  overflow: hidden;
}

.final-doc-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 30%, rgba(54, 192, 135, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(102, 126, 234, 0.1) 0%, transparent 50%);
  pointer-events: none;
}

.final-doc-section .section-container {
  max-width: 1400px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.final-doc-section .section-header .section-tag,
.final-doc-section .section-title,
.final-doc-section .section-desc {
  color: white;
}

.final-doc-section .section-tag {
  background: linear-gradient(135deg, rgba(54, 192, 135, 0.2), rgba(102, 126, 234, 0.2));
  backdrop-filter: blur(10px);
  border: 1px solid rgba(54, 192, 135, 0.3);
}

.final-doc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2.5rem;
  margin: 4rem 0;
}

.doc-category-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
  border-radius: 24px;
  padding: 2.5rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative;
  overflow: hidden;
}

.doc-category-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.5s ease;
}

.doc-category-card.it::before {
  background: linear-gradient(90deg, #667eea, #764ba2);
}

.doc-category-card.rosmaster::before {
  background: linear-gradient(90deg, #667eea, #764ba2);
}

.doc-category-card.conveyor::before {
  background: linear-gradient(90deg, #f59e0b, #d97706);
}

.doc-category-card.dofbot::before {
  background: linear-gradient(90deg, #0891b2, #0e7490);
}

.doc-category-card.electro::before {
  background: linear-gradient(90deg, #f093fb, #f5576c);
}

.doc-category-card.meca::before {
  background: linear-gradient(90deg, #4facfe, #00f2fe);
}

.doc-category-card:hover {
  transform: translateY(-12px);
  border-color: rgba(54, 192, 135, 0.4);
  box-shadow: 
    0 20px 60px rgba(0, 0, 0, 0.4),
    0 0 40px rgba(54, 192, 135, 0.1);
}

.doc-category-card:hover::before {
  transform: scaleX(1);
}

.doc-card-header {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.doc-icon-wrapper {
  width: 70px;
  height: 70px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  position: relative;
  transition: all 0.4s ease;
}

.doc-category-card.it .doc-icon-wrapper {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.doc-category-card.rosmaster .doc-icon-wrapper {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.doc-category-card.conveyor .doc-icon-wrapper {
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
  box-shadow: 0 8px 25px rgba(245, 158, 11, 0.4);
}

.doc-category-card.dofbot .doc-icon-wrapper {
  background: linear-gradient(135deg, #0891b2 0%, #0e7490 100%);
  box-shadow: 0 8px 25px rgba(8, 145, 178, 0.4);
}

.doc-category-card.electro .doc-icon-wrapper {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  box-shadow: 0 8px 25px rgba(240, 147, 251, 0.4);
}

.doc-category-card.meca .doc-icon-wrapper {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  box-shadow: 0 8px 25px rgba(79, 172, 254, 0.4);
}

.doc-icon-wrapper i {
  color: white;
  font-size: 2rem;
}

.doc-category-card:hover .doc-icon-wrapper {
  transform: rotate(360deg) scale(1.1);
}

.doc-card-header h3 {
  font-size: 1.8rem;
  font-weight: 700;
  color: white;
  margin: 0;
}

.doc-description {
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.7;
  margin-bottom: 2rem;
  font-size: 1rem;
}

.doc-features {
  display: grid;
  gap: 0.8rem;
  margin-bottom: 2rem;
}

.doc-feature {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.95rem;
  padding: 0.6rem;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  border-left: 3px solid transparent;
  transition: all 0.3s ease;
}

.doc-category-card.it .doc-feature {
  border-left-color: #667eea;
}

.doc-category-card.rosmaster .doc-feature {
  border-left-color: #667eea;
}

.doc-category-card.conveyor .doc-feature {
  border-left-color: #f59e0b;
}

.doc-category-card.dofbot .doc-feature {
  border-left-color: #0891b2;
}

.doc-category-card.electro .doc-feature {
  border-left-color: #f093fb;
}

.doc-category-card.meca .doc-feature {
  border-left-color: #4facfe;
}

.doc-feature:hover {
  background: rgba(255, 255, 255, 0.06);
  transform: translateX(5px);
}

.doc-feature i {
  color: #36c087;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.doc-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, rgba(54, 192, 135, 0.2), rgba(54, 192, 135, 0.1));
  border: 1px solid rgba(54, 192, 135, 0.4);
  border-radius: 12px;
  color: white;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative;
  overflow: hidden;
}

.doc-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.6s ease;
}

.doc-btn:hover {
  background: linear-gradient(135deg, rgba(54, 192, 135, 0.3), rgba(54, 192, 135, 0.2));
  border-color: rgba(54, 192, 135, 0.6);
  transform: translateX(5px);
  box-shadow: 0 10px 30px rgba(54, 192, 135, 0.3);
}

.doc-btn:hover::before {
  left: 100%;
}

.doc-btn i {
  transition: transform 0.3s ease;
}

.doc-btn:hover i {
  transform: translateX(5px);
}

/* Bannière finale */
.final-doc-banner {
  margin-top: 4rem;
  padding: 2.5rem;
  background: linear-gradient(135deg, rgba(54, 192, 135, 0.1) 0%, rgba(102, 126, 234, 0.1) 100%);
  border-radius: 20px;
  border: 1px solid rgba(54, 192, 135, 0.2);
  backdrop-filter: blur(20px);
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 2rem;
  align-items: center;
}

.banner-icon {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #36c087, #667eea);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  color: white;
  animation: pulse-glow 2s ease-in-out infinite;
}

.banner-content h4 {
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
  margin: 0 0 0.5rem 0;
}

.banner-content p {
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
  margin: 0;
}

.banner-stats {
  display: flex;
  gap: 2rem;
}

.banner-stats .stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.3rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  min-width: 100px;
}

.banner-stats .stat i {
  font-size: 1.5rem;
  color: #36c087;
}

.banner-stats .stat span {
  font-size: 1.3rem;
  font-weight: 700;
  color: white;
}

.banner-stats .stat small {
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.6);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Responsive */
@media (max-width: 968px) {
  .final-doc-grid {
    grid-template-columns: 1fr;
  }

  .final-doc-banner {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .banner-stats {
    justify-content: center;
  }
}

/* Footer Section */
.footer-section {
  background: linear-gradient(135deg, #2c2d41 0%, #1a1b2e 100%);
  color: white;
  padding: 60px 5% 30px;
}

.footer-content {
  max-width: 1400px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
  margin-bottom: 40px;
}

.footer-col h3,
.footer-col h4 {
  color: #36c087;
  margin-bottom: 1.5rem;
  font-size: 1.3rem;
  font-weight: 700;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 1rem;
}

.footer-logo-img {
  height: 40px;
  width: auto;
}

.footer-desc {
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}

.footer-social {
  display: flex;
  gap: 15px;
}

.footer-social a {
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: all 0.3s ease;
  text-decoration: none;
}

.footer-social a:hover {
  background: #36c087;
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(54, 192, 135, 0.4);
}

.footer-social i {
  font-size: 1.1rem;
}

.footer-links {
  list-style: none;
}

.footer-links li {
  margin-bottom: 12px;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: all 0.3s ease;
  display: inline-block;
}

.footer-links a:hover {
  color: #36c087;
  transform: translateX(5px);
}

.footer-badge {
  margin-top: 20px;
}

.trc-logo {
  max-width: 150px;
  height: auto;
  filter: brightness(0) invert(1);
  opacity: 0.8;
  transition: opacity 0.3s ease;
}

.trc-logo:hover {
  opacity: 1;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 30px;
  text-align: center;
  max-width: 1400px;
  margin: 0 auto;
}

.footer-bottom p {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.9rem;
  margin-bottom: 10px;
}

.footer-tagline {
  color: #36c087 !important;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.footer-tagline i {
  width: 18px;
  height: 18px;
  stroke-width: 2.5;
}

/* Cacher le bouton return to top de VitePress */
.custom-home :deep(.VPBackdrop),
.custom-home :deep(.VPNavBarMenuGroup),
.custom-home :deep([class*="BackToTop"]),
.custom-home :deep([class*="back-to-top"]) {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
}
</style>

<style>
/* Cacher globalement le bouton return to top sur la page home */
body:has(.custom-home) .VPBackdrop,
body:has(.custom-home) [class*="BackToTop"],
body:has(.custom-home) [class*="back-to-top"],
body:has(.custom-home) .back-to-top,
body:has(.custom-home) .VPLocalNav,
body:has(.custom-home) .VPDocFooter,
.custom-home ~ * [class*="BackToTop"],
.custom-home ~ * [class*="back-to-top"] {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
}

/* Cacher spécifiquement pour la page avec custom-home */
.VPDoc:has(.custom-home) .VPBackdrop,
.VPDoc:has(.custom-home) [class*="BackToTop"],
.VPDoc:has(.custom-home) [class*="back-to-top"],
.Layout:has(.custom-home) .VPBackdrop,
.Layout:has(.custom-home) [class*="BackToTop"],
.Layout:has(.custom-home) [class*="back-to-top"] {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
}

/* Cibler tous les éléments potentiels */
.vp-doc:has(.custom-home) + * button,
.custom-home + * button[class*="top"],
body button[aria-label*="Return to top"],
body button[title*="Return to top"],
body a[aria-label*="Return to top"],
body a[title*="Return to top"] {
  display: none !important;
}
</style>
