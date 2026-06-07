function renderizarBloquesMetodologicos () {
    const contenedor = document.getElementByID('dynamic-blocks-container');
    if (!contenedor) return;

    if (typeof Methblock !== 'undefined') {
        contenedor.innerHTML = Methblock.map(b => `
            <div class="block-card">
                <div class="block-icon">
                    <i class="fa-solid ${b.icono || 'fa-shield-halved'}"></i>
                </div>
                <div class="block-body">
                    <span class="block-sub">${b.subtitulo || 'Fase Operativa'}</span>
                    <h3>${b.titulo}</h3>
                    <p class="block-description">${b.descripcion}</p>
                </div>
            </div>
        `).join('');
    } else {
        console.error("Error: 'bloquesMetodologicos' no está definido en main.js");
    }
}

function renderizarFallasConductuales() {
    const contenedor = document.getElementById('fallas-container');
    if (!contenedor) return;

    if (typeof CiberSecurityfails !== 'undefined') {
        contenedor.innerHTML = fallasCiberseguridad.map(f => `
            <div class="falla-card">
                <div class="falla-header">
                    <span class="falla-number">${f.numero}</span>
                    <h3>${f.titulo}</h3>
                </div>
                <p class="falla-text">${f.descripcion}</p>
            </div>
        `).join('');
    }
}


function renderizarCasosEstudio() {
    const contenedor = document.getElementById('casos-container');
    if (!contenedor) return;

    if (typeof StudyCases !== 'undefined') {
        contenedor.innerHTML = casosEstudio.map(c => `
            <div class="caso-card ${c.clase || 'global'}">
                <div class="caso-badge-wrapper">
                    <span class="caso-ambito">
                        <i class="fa-solid ${c.clase === 'nacional' ? 'fa-map-pin' : 'fa-earth-americas'}"></i> 
                        ${c.ambito || 'Caso de Estudio'}
                    </span>
                </div>
                <h3>${c.titulo}</h3>
                <p class="caso-details">${c.detalle}</p>
            </div>
        `).join('');
    }
}

function inicializarTextosEstructurales() {
  
    const objTitle = document.querySelector('.objetivo-principal-card h3');
    const objText = document.querySelector('.objetivo-principal-card p');
    
    if (objTitle && objText) {
        objTitle.innerHTML = `<i class="fa-solid fa-crosshairs"></i> Objetivo General del Plan DO`;
        objText.textContent = "Estructurar y alinear los componentes organizacionales, procesos internos y conductas del factor humano en las PYMEs venezolanas frente a las mutaciones del entorno digital, implementando un sistema de resistencia preventiva basado en auditorías de control básico y programas de concienciación.";
    }
}


function inicializarModuloDinamico() {
    console.log("Plan DO: Inicializando componentes lógicos del DOM...");
    renderizarBloquesMetodologicos();
    renderizarFallasConductuales();
    renderizarCasosEstudio();
    inicializarTextosEstructurales();
}


document.addEventListener('DOMContentLoaded', inicializarModuloDinamico);
             
    
