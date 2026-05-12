import { defineConfig } from 'vitepress'

// Sidebar partagée : tests de présélection + test final + lien vers la finale
const realisationsSidebar = [
  {
    text: '⚡ Tests Électronique',
    collapsed: false,
    items: [
      { text: 'Test 1', link: '/test-electro/test-one' },
      { text: 'Test 2', link: '/test-electro/test-two' },
      { text: 'Test 3', link: '/test-electro/test-three' },
    ]
  },
  {
    text: '💻 Tests Informatique',
    collapsed: false,
    items: [
      { text: 'Test 1', link: '/test-it/test-one' },
      {
        text: 'Test 2',
        link: '/test-it/test-two/',
        collapsed: true,
        items: [
          { text: 'Installation de ROS2 Humble', link: '/test-it/test-two/installation-ros2-humble' },
          { text: 'Création de workspace', link: '/test-it/test-two/creation-workspace' },
          { text: 'Création de package', link: '/test-it/test-two/creation-package' },
        ]
      },
      {
        text: 'Test 3',
        link: '/test-it/test-three/',
        collapsed: true,
        items: [
          { text: 'Gazebo', link: '/test-it/test-three/gazebo' },
          { text: 'SLAM et slam_toolbox', link: '/test-it/test-three/slam_and_slam_toolbox' },
          { text: 'RViz2', link: '/test-it/test-three/RViz2' },
          { text: 'Nav2', link: '/test-it/test-three/Nav2' },
        ]
      },
    ]
  },
  {
    text: '⚙️ Tests Mécanique',
    collapsed: false,
    items: [
      { text: 'Test 1', link: '/test-meca/test-one' },
      { text: 'Test 2', link: '/test-meca/test-two' },
      { text: 'Test 3', link: '/test-meca/test-three' },
    ]
  },
  {
    text: '🏁 Test Final',
    collapsed: false,
    items: [
      {
        text: 'Partie IT',
        link: '/test-final/it/it-part'
      },
      {
        text: 'Partie Électronique',
        link: '/test-final/electro/electro-part',
        collapsed: true,
        items: [
          { text: 'Photodiode', link: '/test-final/electro/subpages/photodiode' },
          { text: 'Photorésistance', link: '/test-final/electro/subpages/resistance_utility' },
          { text: 'S0/S1', link: '/test-final/electro/subpages/s0_s1' },
        ]
      },
      {
        text: 'Partie Mécanique',
        link: '/test-final/meca/meca-part',
        collapsed: true,
        items: [
          { text: 'Annexe', link: '/test-final/meca/annexe' },
          { text: 'Convoyeur pièces', link: '/test-final/meca/convoyeur_pieces' },
        ]
      },
    ]
  },
  {
    text: '🏆 Grande Finale TRC 2025',
    collapsed: false,
    items: [
      { text: 'Vue d\'ensemble', link: '/finale/' },
      { text: 'Rosmaster X3', link: '/finale/rosmaster-x3' },
      { text: 'Système Convoyeur', link: '/finale/convoyeur' },
      { text: 'DofBot Jetson Nano', link: '/finale/dofbot-jetson-nano' },
    ]
  },
]

// Sidebar de la section Grande Finale
const finaleSidebar = [
  {
    text: '🏆 Grande Finale TRC 2025',
    items: [
      { text: 'Vue d\'ensemble', link: '/finale/' },
      {
        text: 'Rosmaster X3',
        link: '/finale/rosmaster-x3',
        collapsed: false,
        items: [
          { text: 'Solution 1 : Pince articulée', link: '/finale/solution-1' },
          { text: 'Solution 2 : Pelle frontale', link: '/finale/solution-2' },
          { text: 'Solution 3 : Canalisation arrière', link: '/finale/solution-3' },
        ]
      },
      { text: 'Système Convoyeur', link: '/finale/convoyeur' },
      { text: 'DofBot Jetson Nano', link: '/finale/dofbot-jetson-nano' },
    ]
  },
  {
    text: '← Tests de Présélection',
    collapsed: true,
    items: [
      { text: 'Tests Électronique', link: '/test-electro/test-one' },
      { text: 'Tests Informatique', link: '/test-it/test-one' },
      { text: 'Tests Mécanique', link: '/test-meca/test-one' },
      { text: 'Test Final', link: '/test-final/it/it-part' },
    ]
  },
]

export default defineConfig({
  base: '/2025-Team-IMSP-Docs',
  title: "TEAM IMSP Docs",
  description: "IMSP TEAM Documentation for Tekbot Robotic Challenge 2025 about urban resilience",
  ignoreDeadLinks: true,

  head: [
    ['link', { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css', crossorigin: 'anonymous' }],
  ],

  markdown: {
    math: true
  },

  themeConfig: {
    logo: "/logo.svg",

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Team', link: '/team' },
    ],

    sidebar: {
      '/test-electro/': realisationsSidebar,
      '/test-it/': realisationsSidebar,
      '/test-meca/': realisationsSidebar,
      '/test-final/': realisationsSidebar,
      '/finale/': finaleSidebar,
      '/trc2025-robotics/': [
        {
          text: 'TRC 2025 : La grande finale',
          items: [
            { text: 'Accueil', link: '/trc2025-robotics/' },
            { text: 'README', link: '/trc2025-robotics/README' },
            {
              text: 'Dofbot Jetson Nano',
              items: [
                { text: 'Présentation Dofbot', link: '/trc2025-robotics/trc2025-finale/dofbot-jetson-nano/dofbot-jetson-nano' },
              ]
            },
            {
              text: 'Système ROSMASTER X3',
              items: [
                { text: 'Système de collecte', link: '/trc2025-robotics/trc2025-finale/systeme-ramassage-x3/systeme-rosmaster' },
                {
                  text: 'Solutions mécaniques',
                  collapsed: true,
                  items: [
                    { text: 'Solution 1 : Pince articulée', link: '/trc2025-robotics/trc2025-finale/systeme-ramassage-x3/Solution-1-Pince-mécanique-articule' },
                    { text: 'Solution 2 : Pelle frontale', link: '/trc2025-robotics/trc2025-finale/systeme-ramassage-x3/Solution-2-Pelle-frontale-avec-berne-arriere' },
                    { text: 'Solution 3 : Canalisation (choisie)', link: '/trc2025-robotics/trc2025-finale/systeme-ramassage-x3/Solution-3-Système-de-collecte-en-masse-à-canalisation' },
                  ]
                }
              ]
            }
          ]
        }
      ],
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/beryl-07/TEAM-IMSP-TEKBOT-2025.git' }
    ]
  }
})
