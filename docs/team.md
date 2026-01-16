---
layout: page
sidebar: false
---

<script setup>

import TeamAnimated from './.vitepress/theme/components/TeamAnimated.vue'
</script>

<TeamAnimated />

<style>
/* Cacher la sidebar sur la page team */
.VPSidebar {
  display: none !important;
}

.VPContent.has-sidebar {
  padding-left: 0 !important;
}

/* S'assurer que le contenu prend toute la largeur */
.VPDoc.has-sidebar .container,
.VPDoc.has-sidebar .content {
  max-width: 100% !important;
  padding: 0 !important;
}
</style>