import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from 'tailwindcss'

export default defineConfig({
  plugins: [
    react(),           // React plugin
  ],
  css: {
    postcss: {
      plugins: [tailwindcss()],  // Tailwind CSS plugin
    },
  },
  server: {
    host: '0.0.0.0',  // Listen on all network interfaces
  },
})
