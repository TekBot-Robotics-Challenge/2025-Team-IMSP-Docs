<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
  <div class="team-container">
    <!-- Hero Simple -->
    <div class="team-hero">
      <h1 class="hero-title animate__animated animate__fadeInDown">Notre Équipe</h1>
      <p class="hero-subtitle animate__animated animate__fadeInUp">10 passionnés, 3 pôles, 1 objectif : décrocher le TRC 2025</p>
    </div>

    <!-- Sections des pôles -->
    <section v-for="(pole, poleIndex) in poles" :key="pole.name" class="pole-section">
      <div class="pole-header animate__animated animate__fadeInLeft">
        <div class="pole-icon" :class="pole.class">
          <i :class="pole.icon"></i>
        </div>
        <div class="pole-info">
          <h2 class="pole-title">{{ pole.name }}</h2>
          <p class="pole-desc">{{ pole.desc }}</p>
        </div>
      </div>
      
      <div class="members-grid">
        <div 
          v-for="(member, index) in pole.members" 
          :key="member.name" 
          class="member-card animate__animated animate__fadeInUp"
          :style="{ animationDelay: (index * 0.1) + 's' }"
        >
          <div class="member-photo-ring">
            <div class="member-avatar">
              <img :src="member.img" :alt="member.name" loading="lazy" />
            </div>
          </div>
          <div class="member-info">
            <h3 class="member-name">{{ member.name }}</h3>
            <p class="member-role">{{ member.role }}</p>
            <div class="member-links">
              <a v-if="member.linkedin" :href="member.linkedin" target="_blank" title="LinkedIn">
                <i class="fab fa-linkedin"></i>
              </a>
              <a v-if="member.github" :href="member.github" target="_blank" title="GitHub">
                <i class="fab fa-github"></i>
              </a>
              <a v-if="member.email" :href="'mailto:' + member.email" title="Email">
                <i class="fas fa-envelope"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Ancien Membre Section -->
    <section class="former-member-section">
      <div class="section-header">
        <i class="fas fa-user-clock section-icon"></i>
        <h2 class="section-title">Ancien membre</h2>
      </div>
      <p class="section-subtitle">Nous remercions nos anciens membres qui ont contribué au développement du TekBot.</p>
      
      <div class="former-member-card animate__animated animate__fadeInUp">
        <div class="member-photo-ring">
          <div class="member-avatar">
            <img src="/2025-Team-IMSP-Docs/Marus.jpg" alt="Marius HOUNKPETOHOU" loading="lazy" />
          </div>
        </div>
        <div class="member-info">
          <h3 class="member-name">Marius HOUNKPETOHOU</h3>
          <div class="member-links">
            <a href="https://www.linkedin.com/in/mariushounkpetohou" target="_blank" title="LinkedIn">
              <i class="fab fa-linkedin"></i>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer Section -->
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
        <p>&copy; 2026 TEAM IMSP • IMSP - Université d'Abomey-Calavi • Tous droits réservés</p>
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
const poles = [
  {
    name: 'Pôle IT',
    class: 'it',
    icon: 'fas fa-code',
    desc: "Navigation autonome, IA et systèmes intelligents",
    members: [
      { name: 'Sara ADJAHO', img: '/2025-Team-IMSP-Docs/Sara.jpg', role: 'Master 2 Data Science', linkedin: 'https://www.linkedin.com/in/saraadjaho', github: 'https://github.com/saraadjaho', email: 'sara.adjaho@example.com' },
      { name: 'Claugitte SOSSOUMIHEN', img: '/2025-Team-IMSP-Docs/claugitte.jpg', role: 'Licence 3 Informatique', linkedin: 'https://www.linkedin.com/in/claugittesossoumihen', github: 'https://github.com/claugitte', email: 'claugitte.sossoumihen@example.com' },
      { name: 'Bénilde BOSSA', img: '/2025-Team-IMSP-Docs/benilde.jpg', role: 'Licence 3 Informatique', linkedin: 'https://www.linkedin.com/in/benildebossa', github: 'https://github.com/benildebossa', email: 'benilde.bossa@example.com' },
      { name: 'Marie-Odette ATONDE', img: '/2025-Team-IMSP-Docs/marie-odette.jpg', role: 'Master 1 Recherche Opérationnelle', linkedin: 'https://www.linkedin.com/in/marieodetteatonde', github: 'https://github.com/marieodetteatonde', email: 'marie.odette.atonde@example.com' },
      { name: 'Korede DEGLA', img: '/2025-Team-IMSP-Docs/korede.jpg', role: 'Licence 3 Informatique', linkedin: 'https://www.linkedin.com/in/korededegla', github: 'https://github.com/korededegla', email: 'korede.degla@example.com' },
      { name: 'Béryl HOUESSOU', img: '/2025-Team-IMSP-Docs/beryl.jpg', role: 'Master 2 Data Science', linkedin: 'https://www.linkedin.com/in/berylhouessou', github: 'https://github.com/berylhouessou', email: 'beryl.houessou@example.com' },
    ],
  },
  {
    name: 'Pôle Électronique',
    class: 'electro',
    icon: 'fas fa-microchip',
    desc: 'Circuits, capteurs et électronique embarquée',
    members: [
      { name: 'Donald AITCHEDJI', img: '/2025-Team-IMSP-Docs/donald.jpg', role: 'Licence 3 Informatique', linkedin: 'https://www.linkedin.com/in/donaldaitchedji', github: 'https://github.com/donaldaitchedji', email: 'donald.aitchedji@example.com' },
      { name: 'Siegfried VISSOH', img: '/2025-Team-IMSP-Docs/siegfried.jpg', role: 'Licence 3 Informatique', linkedin: 'https://www.linkedin.com/in/siegfriedvissoh', github: 'https://github.com/siegfriedvissoh', email: 'siegfried.vissoh@example.com' },
    ],
  },
  {
    name: 'Pôle Mécanique',
    class: 'meca',
    icon: 'fas fa-cog',
    desc: 'Conception 3D, assemblage et structure mécanique',
    members: [
      { name: "Alex Gbé'nga AMIGBATIN", img: '/2025-Team-IMSP-Docs/Alex.jpg', role: 'Licence 3 Physique', linkedin: 'https://www.linkedin.com/in/alexamigbatin', github: 'https://github.com/alexamigbatin', email: 'alex.amigbatin@example.com' },
      { name: 'Luc DJETO', img: '/2025-Team-IMSP-Docs/luc.jpg', role: 'Licence 3 Physique', linkedin: 'https://www.linkedin.com/in/lucdjeto', github: 'https://github.com/lucdjeto', email: 'luc.djeto@example.com' },
    ],
  },
];
</script>

<style scoped>
.team-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 3rem 2rem;
}

/* Hero */
.team-hero {
  text-align: center;
  padding: 4rem 0 3rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 4rem;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--vp-c-brand-1);
  width: 100%;
  display: block;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: var(--vp-c-text-2);
  max-width: 600px;
  margin: 0 auto;
}

/* Pole Section */
.pole-section {
  margin-bottom: 5rem;
}

.pole-header {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 3rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid rgba(255, 255, 255, 0.05);
}

.pole-icon {
  width: 70px;
  height: 70px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  flex-shrink: 0;
}

.pole-icon.it {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(102, 126, 234, 0.05));
  color: #667eea;
}

.pole-icon.electro {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(245, 158, 11, 0.05));
  color: #f59e0b;
}

.pole-icon.meca {
  background: linear-gradient(135deg, rgba(8, 145, 178, 0.1), rgba(8, 145, 178, 0.05));
  color: #0891b2;
}

.pole-info {
  flex: 1;
}

.pole-title {
  font-size: 2rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
  color: var(--vp-c-text-1);
}

.pole-desc {
  font-size: 1.05rem;
  color: var(--vp-c-text-2);
  margin: 0;
}

/* Members Grid */
.members-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.member-card {
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 20px;
  padding: 2rem 1.5rem 1.5rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  transition: all 0.35s ease;
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.06);
  position: relative;
  overflow: hidden;
}

.member-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--vp-c-brand-1), #2ea574);
  opacity: 0;
  transition: opacity 0.3s;
}

.member-card:hover {
  transform: translateY(-6px);
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 12px 40px rgba(54, 192, 135, 0.15);
}

.member-card:hover::before {
  opacity: 1;
}

/* Photo ring styled like reference image */
.member-photo-ring {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(135deg, #36c087, #2ea574, #667eea);
  padding: 4px;
  margin-bottom: 1.2rem;
  flex-shrink: 0;
  transition: transform 0.3s, box-shadow 0.3s;
}

.member-card:hover .member-photo-ring {
  transform: scale(1.04);
  box-shadow: 0 0 0 6px rgba(54, 192, 135, 0.15);
}

.member-avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid var(--vp-c-bg);
  background: var(--vp-c-bg-soft);
}

.member-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
}

.member-info {
  width: 100%;
}

.member-name {
  font-size: 1.05rem;
  font-weight: 700;
  margin: 0 0 0.3rem 0;
  color: var(--vp-c-text-1);
  letter-spacing: -0.01em;
}

.member-role {
  font-size: 0.82rem;
  color: var(--vp-c-brand-1);
  font-weight: 600;
  margin: 0 0 1rem 0;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.member-links {
  display: flex;
  justify-content: center;
  gap: 0.6rem;
}

.member-links a {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-2);
  transition: all 0.25s;
  text-decoration: none;
  font-size: 0.95rem;
}

.member-links a:hover {
  background: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
  color: white;
  transform: translateY(-2px);
}

/* Footer Section */
.footer-section {
  background: linear-gradient(135deg, rgba(18, 18, 31, 0.95), rgba(35, 35, 74, 0.95));
  border-top: 1px solid rgba(54, 192, 135, 0.2);
  padding: 4rem 3rem 2rem;
  margin-top: 5rem;
  margin-left: calc(-50vw + 50%);
  margin-right: calc(-50vw + 50%);
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 3rem;
  max-width: 1400px;
  margin: 0 auto 3rem;
}

.footer-col {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin-bottom: 0.5rem;
}

.footer-logo-img {
  width: 40px;
  height: 40px;
}

.footer-logo h3 {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--vp-c-brand-1);
  margin: 0;
}

.footer-desc {
  color: #bdbdbd;
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.footer-social {
  display: flex;
  gap: 1rem;
}

.footer-social a {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 50%;
  color: #bdbdbd;
  transition: all 0.3s;
  font-size: 1.2rem;
}

.footer-social a:hover {
  background: var(--vp-c-brand-1);
  color: #fff;
  transform: translateY(-3px);
}

.footer-col h4 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #fff;
  margin-bottom: 0.5rem;
}

.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.footer-links li a {
  color: #bdbdbd;
  text-decoration: none;
  font-size: 0.95rem;
  transition: all 0.3s;
  display: inline-block;
}

.footer-links li a:hover {
  color: var(--vp-c-brand-1);
  transform: translateX(5px);
}

.footer-badge {
  margin-top: 1rem;
}

.trc-logo {
  width: 120px;
  height: auto;
}

.footer-bottom {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  color: #bdbdbd;
  font-size: 0.9rem;
}

.footer-bottom p {
  margin: 0.5rem 0;
}

.footer-tagline {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.footer-tagline i {
  color: var(--vp-c-brand-1);
  font-size: 1rem;
}

/* Former Member Section */
.former-member-section {
  margin: 5rem 0 4rem;
  text-align: center;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.section-icon {
  font-size: 2rem;
  color: var(--vp-c-brand-1);
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  margin: 0;
}

.section-subtitle {
  font-size: 1rem;
  color: var(--vp-c-text-2);
  margin-bottom: 3rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.former-member-card {
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 20px;
  padding: 2rem 1.5rem 1.5rem;
  max-width: 280px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: all 0.35s ease;
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.06);
}

.former-member-card:hover {
  transform: translateY(-6px);
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 12px 40px rgba(54, 192, 135, 0.15);
}

.former-member-card .member-photo-ring {
  width: 150px;
  height: 150px;
  margin-bottom: 1.2rem;
}

/* Responsive */
@media (max-width: 1200px) {
  .members-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
  }
}

@media (max-width: 1024px) {
  .footer-content {
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
  }
}

@media (max-width: 768px) {
  .team-container {
    padding: 2rem 1rem;
  }

  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .pole-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .pole-title {
    font-size: 1.5rem;
  }

  .members-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .footer-section {
    padding: 3rem 1.5rem 1.5rem;
    margin-left: -1rem;
    margin-right: -1rem;
  }

  .footer-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}
</style>
