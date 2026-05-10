<template>
  <div>
    <nav class="navbar">
      <RouterLink to="/">Dashboard</RouterLink>
      <RouterLink to="/qa">AI 問答</RouterLink>
      <RouterLink to="/history">歷史紀錄</RouterLink>
    </nav>

    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>

<style>
.navbar {
  display: flex;
  gap: 20px;
  padding: 16px;
  border-bottom: 1px solid #ddd;
}

.navbar a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.main-content {
  padding: 24px;
}
</style>