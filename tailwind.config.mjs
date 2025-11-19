/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				bg: 'var(--color-bg)',
				primary: 'var(--color-text)',
			},
            fontFamily: {
                serif: ['Georgia', 'Cambria', 'Times New Roman', 'serif'],
                sans: ['Inter', 'system-ui', 'sans-serif'] // Use for UI elements
            }
		},
	},
	plugins: [
        require('@tailwindcss/typography'), // Ensure you install: npm install -D @tailwindcss/typography
    ],
}