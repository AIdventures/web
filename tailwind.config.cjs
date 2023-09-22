/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			fontFamily: {
				sans: ["Source Sans Pro", ...defaultTheme.fontFamily.sans],
			},
			colors: {
				lila: {
					500: "#c8befd",
					900: "#5534F9",
				},
				pink: {
					500: "#f3c4cd",
				}
			}
		},
	},
	plugins: [require("@tailwindcss/typography")],
}
