import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// Relative base so the app works under a GitHub Pages project subpath.
// https://vite.dev/config/
export default defineConfig({
  base: './',
  plugins: [svelte()],
  // Allow importing the repo's docs/*.md (one level above this web/ root) as ?raw.
  server: { port: 2137, strictPort: true, fs: { allow: ['..'] } },
})
