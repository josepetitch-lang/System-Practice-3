const slides: NodeListOf<HTMLElement> = document.querySelectorAll('.slide');
const prevBtn: HTMLButtonElement | null = document.querySelector('.btn-prev');
const nextBtn: HTMLButtonElement | null = document.querySelector('.btn-next');

let currentSlide: number = 0;

const updateSlide = (index: number): void => {
    slides.forEach((slide: HTMLElement, i: number) => {
        slide.classList.toggle('active', i === index);
    });
};

export const cambiarSlide = (direccion: number): void => {
    currentSlide = (currentSlide + direccion + slides.length) % slides.length;
    updateSlide(currentSlide);
};


prevBtn?.addEventListener('click', () => cambiarSlide(-1));
nextBtn?.addEventListener('click', () => cambiarSlide(1));


document.addEventListener('keydown', (e: KeyboardEvent) => {
    if (e.key === 'ArrowRight') cambiarSlide(1);
    if (e.key === 'ArrowLeft') cambiarSlide(-1);
});


updateSlide(currentSlide);