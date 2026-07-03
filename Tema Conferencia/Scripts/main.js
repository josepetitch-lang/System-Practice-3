// pq voy a añadir una imagen de kingdedede XDDDDDDDD

document.addEventListener('DOMContentLoaded', () => {
    console.log("Bienvenido a la Conferencia de la Comunicación xd")

    const actualizarSeccion = (titulo, imagenSrc) => {
        document.getElementById('titulo-principal').innerText = titulo;
        document.getElementById("img-principal").src = imagenSrc;
    }
})

window.onload = () => {
    const speaker = "José Guanipa";
    console.log(`Bienvenidos. El día de hoy nos acompaña ${speaker} para hablar sobre comunicación.`);

    const img = document.querySelector('.avatar-speaker');
   img.style.cursor = 'pointer';
   img.onclick = () => alert("Hola, soy José Guanipa, nosé que hacer con mi vida alaverga") //jajajajaj
}

document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;

    
    const showSlide = (index) => {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
    };

    
    document.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowRight' && currentSlide < slides.length - 1) {
            currentSlide++;
            showSlide(currentSlide);
        } else if (event.key === 'ArrowLeft' && currentSlide > 0) {
            currentSlide--;
            showSlide(currentSlide);
        }
    });


    showSlide(currentSlide);
    console.log("Presentación cargada. Usa las flechas para navegar.");
});

let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

const cambiarSlide = (direccion) => {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + direccion + slides.length) % slides.length;
    slides[currentSlide].classList.add('active');
};


document.addEventListener('keydown', (e) => {
    if(e.key === 'ArrowRight') cambiarSlide(1);
    if(e.key === 'ArrowLeft') cambiarSlide(-1);
});