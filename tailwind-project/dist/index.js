const burger = document.querySelector('#burger');
const menue = document.querySelector('#menue');

burger.addEventListener('click', () => {
	if ( menue.classList.contains('hidden')) {
		menue.classList.remove('hidden');
	} else {
		menue.classList.add('hidden');
	}
})
