import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('/home/sparlex/Projects/WEB/Map_of_city_events/venv/Include/activity_map/media', import.meta.url))
    }
  }
})
