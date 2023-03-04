/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
	  "./dist/index.html",
	  './components/**/*.{html,js}',
	  './pages/**/*.{html,js}',
  ],
  theme: {
    extend: {
		colors:{
			anime:'#ff6363',
			secondary:{
				100:'#E2E2D5',
				200:'#888883',
			}
		},
		fontFamily:{
			body:['Nunito']
		}
	},
  },
  plugins: [],
}
