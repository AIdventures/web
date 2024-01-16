/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			typography: {
				DEFAULT: {
					css: {
						strong: {
							color: 'white'
						},
						blockquote: {
							color: '#ccc'
						}
					}
				},
			},
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
				},
				green: {
					500: "#8dbfc9",
				},
				dungeon: {
					50: '#f4f6f7',
					100: '#e2e8eb',
					200: '#c9d3d8',
					300: '#a3b3bd',
					400: '#768c9a',
					500: '#5a7080',
					600: '#4e5e6c',
					700: '#434f5b',
					800: '#3c454e',
					900: '#363c43',
					950: '#1b1f24',
				},
				gold: {
					50: '#fcf8ea',
					100: '#f8eec9',
					200: '#f1da97',
					300: '#e8bc53',
					400: '#e1a52e',
					500: '#d18e21',
					600: '#b46d1a',
					700: '#904f18',
					800: '#783f1b',
					900: '#67361c',
					950: '#3b1b0d',
				}
			}
		},
	},
	plugins: [require("@tailwindcss/typography")],
}
