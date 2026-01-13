<template>
  <!-- Animate.css CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
  <div class="custom-home">
    <div class="hero-section">
      <!-- Navigation -->
      
      <nav class="custom-nav">
        <div class="logo animate__animated animate__fadeInDown">
          <img
            src="/2025-Team-IMSP-Docs/logo.svg"
            alt="Logo"
            class="logo-img"
          />
          <span class="logo-text"
            ><span class="highlight-i">TEAM IMSP</span> Docs</span
          >
        </div>
        <ul class="nav-links animate__animated animate__fadeInDown animate__delay-1s" :class="{ active: menuOpen }">
          <li><a href="/2025-Team-IMSP-Docs/" @click="closeMenu">Home</a></li>
          <li><a href="/2025-Team-IMSP-Docs/coming-soon" @click="closeMenu">About</a></li>
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
          <h3 class="hero-title animate__animated animate__fadeInLeft animate__delay-1s">IMSP TEAM <span class="highlight">Tekbot Robotic Challenge 2025</span></h3>

          <div class="hero-actions animate__animated animate__fadeInUp animate__delay-2s">
            <a href="/2025-Team-IMSP-Docs/test-it/test-one" class="btn-primary"
              >Documentation</a
            >
            <a href="https://trc.tekbot.io/trc-2025/" class="btn-secondary"
              >Learn More</a
            >
          </div>
        </div>

        <div class="hero-right">
          <div class="hero-image-wrapper animate__animated animate__fadeInRight animate__delay-1s">
            <div class="hero-image-bg"></div>
            <img
              src="/2025-Team-IMSP-Docs/IMSP_TEAM.png"
              alt="IMSP Team"
              class="hero-image"
            />
            <div class="floating-badge animate__animated animate__bounceIn animate__delay-3s">
              <div class="icon">
                
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Features Section -->
    <div class="features-section">
      <div class="features-grid">
        <div class="feature-card animate__animated animate__fadeInUp" style="animation-delay: 0.2s;">
          <div class="feature-icon">📚</div>
          <h3 class="feature-title">Test One</h3>
          <p class="feature-description">
            The first week allowed us to acquire basic knowledge of
            object-oriented programming (OOP), the UML language, Arduino
            programming, and mechanical part design using SolidWorks.
          </p>
          <a href="/2025-Team-IMSP-Docs/test-it/test-one" class="feature-link"
            >Learn more</a
          >
        </div>

        <div class="feature-card animate__animated animate__fadeInUp" style="animation-delay: 0.4s;">
          <div class="feature-icon">🔧</div>
          <h3 class="feature-title">Test Two</h3>
          <p class="feature-description">
            This test focuses on the integration of various sensors and
            actuators with the ROS2 framework, enabling the robot to perceive
            its environment and respond to changes effectively.
          </p>
          <a href="/2025-Team-IMSP-Docs/test-it/test-two" class="feature-link"
            >Learn more</a
          >
        </div>

        <div class="feature-card animate__animated animate__fadeInUp" style="animation-delay: 0.6s;">
          <div class="feature-icon">🛠️</div>
          <h3 class="feature-title">Test Three</h3>
          <p class="feature-description">
            This test consists of developing an autonomous navigation system for
            the TekBot mobile robot in a simulated environment using ROS2 and
            Gazebo.
          </p>
          <a href="/2025-Team-IMSP-Docs/test-it/test-three" class="feature-link"
            >Learn more</a
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const menuOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

const closeMenu = () => {
  menuOpen.value = false
}
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
  grid-template-columns: 1fr 1fr;
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
  display: inline;
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
  display: inline-block;
  text-align: center;
  position: relative;
  overflow: hidden;
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

.btn-secondary:hover {
  color: #36c087;
  gap: 15px;
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
  max-width: 500px;
  transition: transform 0.5s ease;
}

.hero-image-wrapper:hover {
  transform: scale(1.05);
}

.hero-image-bg {
  width: 100%;
  max-width: 450px;
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
