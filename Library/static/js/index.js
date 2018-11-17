const menuIcon = document.getElementById('open-menu');
const navBar = document.querySelector('nav.mobile');


menuIcon.addEventListener('click', toggleMenu);

function toggleMenu() {
    if (navBar.classList.contains('open')) {
        navBar.classList.remove('open');
        menuIcon.firstChild.classList.add('fa-bars');
        menuIcon.firstChild.classList.remove('fa-times');
    } else {
        navBar.classList.add("open");
        menuIcon.firstChild.classList.add('fa-times');
        menuIcon.firstChild.classList.remove('fa-bars');
    }
}