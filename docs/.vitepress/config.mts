import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/2025-Team-IMSP-Docs',
  title: "TEAM IMSP Docs",
  description: "IMSP TEAM Documentation for Tekbot Robotic Challenge 2025 about urban resilience",
  themeConfig: {
    logo: "/logo.svg",
    nav: [
      { text: 'Home', link: '/' },
      { text: 'About', link: '/coming-soon' },
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
              { text: 'Test 2', link: '/test-electro/test-two.md'},
              { text: 'Test 3', link: '/test-electro/test-three.md'}
            ]
          },
          {
            text: 'Tests Informatique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: '/test-it/test-one.md' },
              { text: 'Test 2', link: '/test-it/test-two/index.md',
                items: [
                  {
                    text: 'Installation de ROS2 Humble',
                    link: '/test-it/test-two/installation-ros2-humble.md'
                  },
                  {
                    text: 'Creation de workspace',
                    link: '/test-it/test-two/creation-workspace.md'
                  },
                  {
                    text: 'Creation de package',
                    link: '/test-it/test-two/creation-package.md'
                  },
                ]
              },
              { text: 'Test 3', link: '/test-it/test-three/index.md',
                items: [
                  {
                    text: 'Gazebo',
                    link: '/test-it/test-three/gazebo.md'
                  },
                  {
                    text: 'SLAM et slam_toolbox',
                    link: '/test-it/test-three/slam_and_slam_toolbox.md'
                  },
                  {
                    text: 'RViz2',
                    link: '/test-it/test-three/RViz2.md'
                  },
                  {
                    text: 'Nav2',
                    link: '/test-it/test-three/Nav2.md'
                  }
                ]
              }
            ]
          },
           {
            text: 'Tests Mécanique',
            collapsed: true,
            items: [
              { text: 'Test 1', link: '/test-meca/test-one.md' },
              { text: 'Test 2', link: '/test-meca/test-two.md',},
              { text: 'Test 3', link: '/test-meca/test-three.md' }
            ]
          },
          {
            text: 'Test final',
            collapsed: true,
            items: [
              { text: 'Test final', link: '/test-final/index.md' },
            ]
          }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/beryl-07/TEAM-IMSP-TEKBOT-2025.git' }
    ]
  }
})
