function configurarNavegacion () {
    const navbar = document.querySelector('.navbar');

    window.addEventListener ('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });

    const enlacesMenu = document.querySelectorAll('.nav-menu a[href^="#"]');

    enlacesMenu.forEach(enlace => {
        enlace.addEventListener('click', function(e) {
            e.preventDefault();

            const idDestino = this.getAttribute('href');
            const elementDestiny = document.querySelector(idDestino);

            if(elementDestiny) {
                const highNavbar = navbar.offsetHeight;
                const Elementpos = elementDestiny.getBoundingClientRect().top;
                const PosAbsolute = Elementpos + window.pageYOffset - highNavbar;

                window.scrollTo({
                     top: PosAbsolute,
                     behavior: 'smooth' // animación de scroll suave, tipo ig o tiktok o yt o como veas caraverga
                });
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', configurarNavegacion)