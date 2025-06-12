import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "TEAM IMSP Docs",
  description: "IMSP TEAM Documentation for Tekbot Robotic Challenge 2025 about urban resilience",
  themeConfig: {
    logo: "/logo.svg",
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Tests de Préselection',
        items: [
          {
            text: 'Tests Électronique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: 'test-electro/test-01' },
            ]
          },
          {
            text: 'Tests Informatique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: 'test-it/test-01/test_01' },
            ]
          },
          //  {
          //   text: 'Tests Mécanique',
          //   collapsed: true,
          //   items: [
          //     { text: 'Test 1', link: 'test-meca/test-01/' },
          //   ]
          // },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/beryl-07/TEAM-IMSP-TEKBOT-2025.git' }
    ]
  }
})
