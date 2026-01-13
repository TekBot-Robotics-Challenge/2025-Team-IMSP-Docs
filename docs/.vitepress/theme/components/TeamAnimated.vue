<template>
  <!-- FontAwesome CDN pour les icônes -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <div class="team-page-animated">
    <h1 class="team-title">Découvrez notre équipe</h1>
    <p class="team-desc">Notre équipe est composée de 10 membres répartis en trois pôles distincts, chacun spécialisé dans un domaine précis : IT, Électronique et Mécanique.</p>

    <section v-for="pole in poles" :key="pole.name" class="team-pole">
      <h2 class="pole-title">
        <i v-if="pole.icon" :class="['fa-fw', pole.icon, 'fa-bounce']" style="margin-right: 0.5rem; color: #36c087;"></i>
        {{ pole.name }}
      </h2>
      <p class="pole-desc">{{ pole.desc }}</p>
      <div class="team-grid">
        <div v-for="member in pole.members" :key="member.name" class="team-card animate__animated animate__fadeInUp">
          <div class="team-img-wrapper">
            <img :src="member.img" :alt="member.name" class="team-img" />
          </div>
          <div class="team-info">
            <h3 class="team-name">{{ member.name }}</h3>
            <p class="team-role">{{ member.role }}</p>
            <div class="team-socials">
              <a v-if="member.linkedin" :href="member.linkedin" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
              <a v-if="member.github" :href="member.github" target="_blank" aria-label="GitHub"><i class="fab fa-github"></i></a>
              <a v-if="member.twitter" :href="member.twitter" target="_blank" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
              <a v-if="member.email" :href="'mailto:' + member.email" aria-label="Email"><i class="fas fa-envelope"></i></a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const poles = [
  {
    name: 'Pôle IT',
    icon: 'fas fa-laptop-code',
    desc: "Plongez dans l’univers des logiciels, des algorithmes et des systèmes intelligents qui assurent le contrôle du TekBot.",
    members: [
      { name: 'Sara Adjaho', img: '/2025-Team-IMSP-Docs/Sara.jpg', role: 'Master 2 Data Science', linkedin: 'https://www.linkedin.com/in/saraadjaho', github: 'https://github.com/saraadjaho', email: 'sara.adjaho@example.com' },
      { name: 'Claugitte Sossoumihen', img: '/2025-Team-IMSP-Docs/claugitte.jpg', role: 'Licence 3 Informatique', linkedin: 'https://www.linkedin.com/in/claugittesossoumihen', github: 'https://github.com/claugitte', email: 'claugitte.sossoumihen@example.com' },
      { name: 'Bénilde Bossa', img: '/2025-Team-IMSP-Docs/benilde.jpg', role: 'Licence 3 Informatique', linkedin: 'https://www.linkedin.com/in/benildebossa', github: 'https://github.com/benildebossa', email: 'benilde.bossa@example.com' },
      { name: 'Marie-Odette Atondé', img: '/2025-Team-IMSP-Docs/marie-odette.jpg', role: 'Master 1 Recherche Opérationnelle', linkedin: 'https://www.linkedin.com/in/marieodetteatonde', github: 'https://github.com/marieodetteatonde', email: 'marie.odette.atonde@example.com' },
      { name: 'Korede Degla', img: '/2025-Team-IMSP-Docs/korede.jpg', role: 'Licence 3 Informatique', linkedin: 'https://www.linkedin.com/in/korededegla', github: 'https://github.com/korededegla', email: 'korede.degla@example.com' },
      { name: 'Béryl Houéssou', img: '/2025-Team-IMSP-Docs/beryl.jpg', role: 'Master 2 Data Science', linkedin: 'https://www.linkedin.com/in/berylhouessou', github: 'https://github.com/berylhouessou', email: 'beryl.houessou@example.com' },
    ],
  },
  {
    name: 'Pôle Électronique',
    icon: 'fas fa-bolt',
    desc: 'Découvrez les capteurs, circuits et composants électroniques qui donnent vie au TekBot.',
    members: [
      { name: 'Donald Aitchedji', img: '/2025-Team-IMSP-Docs/donald.jpg', role: 'Licence 3 Informatiquen', linkedin: 'https://www.linkedin.com/in/donaldaitchedji', github: 'https://github.com/donaldaitchedji', email: 'donald.aitchedji@example.com' },
      { name: 'Siegfried Vissoh', img: '/2025-Team-IMSP-Docs/siegfried.jpg', role: 'Licence 3 Informatique', linkedin: 'https://www.linkedin.com/in/siegfriedvissoh', github: 'https://github.com/siegfriedvissoh', email: 'siegfried.vissoh@example.com' },
    ],
  },
  {
    name: 'Pôle Mécanique',
    icon: 'fas fa-cogs',
    desc: 'Explorez la conception physique, les matériaux et les techniques d’assemblage qui structurent le TekBot.',
    members: [
      { name: "Alex Gbé'nga Amigbatin", img: '/2025-Team-IMSP-Docs/Alex.jpg', role: 'Licence 3 Physique', linkedin: 'https://www.linkedin.com/in/alexamigbatin', github: 'https://github.com/alexamigbatin', email: 'alex.amigbatin@example.com' },
      { name: 'Luc Djeto', img: '/2025-Team-IMSP-Docs/luc.jpg', role: 'Licence 3 Physique', linkedin: 'https://www.linkedin.com/in/lucdjeto', github: 'https://github.com/lucdjeto', email: 'luc.djeto@example.com' },
    ],
  },
  // Ajoutez d'autres pôles ici si besoin
];
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css');
  /* Correction : bloc CSS orphelin supprimé */
@keyframes fadeInBg {
  from { opacity: 0; }
  to { opacity: 1; }
}
  .team-title {
    text-align: left;
    font-size: 2.8rem;
    margin-bottom: 0.5rem;
    letter-spacing: 1px;
    font-weight: 700;
  }
  .team-desc {
    text-align: left;
    font-size: 1.2rem;
    margin-bottom: 2.5rem;
    color: #bdbdbd;
  }
  .team-pole {
    margin-bottom: 2.5rem;
    background: none;
    box-shadow: none;
    border-radius: 0;
    padding: 0;
    border: none;
  }
  .pole-title {
    font-size: 2rem;
    margin-bottom: 0.2rem;
    text-align: left;
    color: #36c087;
    font-weight: 600;
  }
  .pole-desc {
    text-align: left;
    color: #bdbdbd;
    margin-bottom: 2rem;
  }
  .team-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5rem 2rem;
    margin-bottom: 1.5rem;
    background: none;
    box-shadow: none;
    border-radius: 0;
    padding: 0;
    justify-items: center;
  }
  .team-card {
    background: none;
    border-radius: 2rem;
    box-shadow: none;
    padding: 2.2rem 1.5rem 1.5rem 1.5rem;
    width: 260px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    transition: transform 0.3s, box-shadow 0.3s;
    position: relative;
    overflow: visible;
    border: none;
    animation-delay: 0.2s;
    text-align: left;
  }
.team-card:hover {
  transform: translateY(-10px) scale(1.04) rotate(-1deg);
  box-shadow: 0 12px 40px 0 rgba(54,192,135,0.18);
  border-color: #36c087;
}
  .team-img-wrapper {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    overflow: hidden;
    border: 5px solid #23234a;
    margin-bottom: 1.3rem;
    box-shadow: 0 4px 24px 0 rgba(54,192,135,0.14);
    background: #18182f;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: border-color 0.3s;
  }
.team-card:hover .team-img-wrapper {
  border-color: #36c087;
}
  .team-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
    filter: grayscale(10%) contrast(1.1);
    transition: filter 0.3s;
  }
.team-card:hover .team-img {
  filter: grayscale(0%) contrast(1.2) brightness(1.1);
}
  .team-info {
    text-align: left;
  }
  .team-name {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 0.2rem;
    color: #fff;
    text-align: left;
  }
  .team-role {
    font-size: 1rem;
    color: #36c087;
    margin-bottom: 0.7rem;
    text-align: left;
  }
  .team-socials {
    display: flex;
    justify-content: flex-start;
    gap: 0.7rem;
  }
.team-socials a {
  color: #bdbdbd;
  font-size: 1.2rem;
  transition: color 0.2s, transform 0.2s;
}
.team-socials a:hover {
  color: #36c087;
  transform: scale(1.2) rotate(-8deg);
}
@media (max-width: 1200px) {
  .team-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem 0;
  }
  .team-card {
    width: 90vw;
    max-width: 320px;
  }
}
@media (max-width: 600px) {
  .team-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem 1rem;
  }
  .team-card {
    width: 90vw;
    max-width: 320px;
  }
}
</style>
