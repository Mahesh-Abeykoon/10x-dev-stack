import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

/**
 * ⚡ 10x Performance Config
 * Optimized for AI-generated apps (Bolt/Lovable style)
 */
export default defineConfig({
    plugins: [react()],
    build: {
        target: 'esnext', // Use modern JS for smaller bundles
        minify: 'esbuild', // Faster builds
        cssMinify: true,
        rollupOptions: {
            output: {
                manualChunks: {
                    'vendor': ['react', 'react-dom', 'framer-motion'], // Split large libs
                    'ui': ['lucide-react', 'clsx', 'tailwind-merge'] // Common UI libs
                }
            }
        }
    },
    server: {
        hmr: {
            overlay: false // Prevents overlay crashes during rapid AI edits
        }
    }
});
