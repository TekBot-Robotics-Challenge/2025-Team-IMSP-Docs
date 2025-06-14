import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/2025-Team-IMSP-Docs',
  title: "TEAM IMSP Docs",
  description: "IMSP TEAM Documentation for Tekbot Robotic Challenge 2025 about urban resilience",
  themeConfig: {
    logo: "/logo.svg",
    nav: [
      { text: 'Home', link: '/' },
      { text: 'About', link: '/coming-soon' }
    ],

    sidebar: [
      {
        text: 'Tests de Préselection',
        items: [
          {
            text: 'Tests Électronique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: 'test-electro/test-one-elec' },
            ]
          },
          {
            text: 'Tests Informatique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: 'test-it/test-one-it' },
            ]
          },
           {
            text: 'Tests Mécanique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: 'test-meca/test-one-meca' },
            ]
          },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/beryl-07/TEAM-IMSP-TEKBOT-2025.git' }
    ]
  }
})
