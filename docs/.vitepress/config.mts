import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/2025-Team-IMSP-Docs',
  title: "TEAM IMSP Docs",
  description: "IMSP TEAM Documentation for Tekbot Robotic Challenge 2025 about urban resilience",

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

    sidebar: [
      {
        text: 'Tests de Préselection',
        items: [
          {
            text: 'Tests Électronique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: '/test-electro/test-one.md' },
              { text: 'Test 2', link: '/test-electro/test-two.md' },
              { text: 'Test 3', link: '/test-electro/test-three.md' }
            ]
          },
          {
            text: 'Tests Informatique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: '/test-it/test-one.md' },
              {
                text: 'Test 2',
                link: '/test-it/test-two/index.md',
                items: [
                  { text: 'Installation de ROS2 Humble', link: '/test-it/test-two/installation-ros2-humble.md' },
                  { text: 'Creation de workspace', link: '/test-it/test-two/creation-workspace.md' },
                  { text: 'Creation de package', link: '/test-it/test-two/creation-package.md' }
                ]
              },
              {
                text: 'Test 3',
                link: '/test-it/test-three/index.md',
                items: [
                  { text: 'Gazebo', link: '/test-it/test-three/gazebo.md' },
                  { text: 'SLAM et slam_toolbox', link: '/test-it/test-three/slam_and_slam_toolbox.md' },
                  { text: 'RViz2', link: '/test-it/test-three/RViz2.md' },
                  { text: 'Nav2', link: '/test-it/test-three/Nav2.md' }
                ]
              }
            ]
          },
          {
            text: 'Tests Mécanique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: '/test-meca/test-one.md' },
              { text: 'Test 2', link: '/test-meca/test-two.md' },
              { text: 'Test 3', link: '/test-meca/test-three.md' }
            ]
          },
          {
            text: 'Test final',
            collapsed: true,
            items: [
              {
                text: 'Test final',
                link: '/test-final/index.md',
                items: [
                  { text: 'Partie IT', link: '/test-final/it/it-part.md' },
                  {
                    text: 'Partie Electro',
                    link: '/test-final/electro/electro-part.md',
                    collapsed: true,
                    items: [
                      { text: 'Photodiode', link: '/test-final/electro/subpages/photodiode.md' },
                      { text: 'Utilité de la photorésistance dans le projet', link: '/test-final/electro/subpages/resistance_utility.md' },
                      { text: 'S0/S1', link: '/test-final/electro/subpages/s0_s1.md' }
                    ]
                  },
                  {
                    text: 'Partie Mécanique',
                    link: '/test-final/meca/meca-part.md',
                    items: [
                      { text: 'Annexe', link: '/test-final/meca/annexe.md' },
                      { text: 'Convoyeur pièces', link: '/test-final/meca/convoyeur_pieces.md' }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },

      {
  text: 'TRC 2025: La finale',
  collapsed: true,
  items: [    
    {
      text: 'Généralités',
      link: '/finale/README.md'
    },

    {
      
      items: [
        {
          text: 'Dofbot Jetson Nano',
          link: '/finale/trc2025-finale/dofbot-jetson-nano/dofbot-jetson-nano.md'
        }
      ]
    },
      {
      
      items: [
        {
          text: 'Système Convoyeur',
          link: '/finale/trc2025-finale/systeme-convoyeur/systeme-convoyeur.md'
        }
      ]
    },

    {
      
      items: [
        {
          text: 'Système ROSMASTER X3',
          link: '/finale/trc2025-finale/systeme-rosmaster-x3/systeme-rosmaster.md'
        },

        {
          text: 'Solutions mécaniques',
          collapsed: true,
          items: [
            {
              text: 'Solution 1 : Pince mécanique articulée',
              link: '/finale/trc2025-finale/systeme-rosmaster-x3/Solution-1-Pince-mécanique-articule.md'
            },
            {
              text: 'Solution 2 : Pelle frontale + berne arrière',
              link: '/finale/trc2025-finale/systeme-rosmaster-x3/Solution-2-Pelle-frontale-avec-berne-arriere.md'
            },
            {
              text: 'Solution 3 : Collecte en masse par canalisation (choisie)',
              link: '/finale/trc2025-finale/systeme-rosmaster-x3/Solution-3-Système-de-collecte-en-masse-à-canalisation.md'
            }
          ]
        }
      ]
    }
  ]
},
      {
        text: 'Raccourcis',
        items: [
          { text: 'Accueil', link: '/index.md' },
          { text: 'Rosmaster X3', link: '/finale/trc2025-finale/systeme-rosmaster-x3/systeme-rosmaster.md',
                      },
          { text: 'Système Convoyeur', link: '/finale/trc2025-finale/systeme-convoyeur/systeme-convoyeur.md' },

          { text: 'DofBot Jetson Nano', link: '/finale/trc2025-finale/dofbot-jetson-nano/dofbot-jetson-nano.md' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/beryl-07/TEAM-IMSP-TEKBOT-2025.git' }
    ]
  }
})
