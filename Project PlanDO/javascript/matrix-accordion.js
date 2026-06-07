const PlanDOInfo = {
    nombre: "Sistema de concientización y auditoría básica de ciberseguridad para empresas venezolanas",
    descripcion: "Es un programa de consultoría preventiva de naturaleza tecno-estructural concebido exclusivamente para la realidad de las pequeñas y medianas empresas (PYMEs) en Venezuela. Su propósito fundamental es el diseño, estructuración y ejecución de un sistema de mitigación de riesgos digitales que actúa sobre el entorno operativo de la organización, identificando brechas en el manejo de datos para corregirlas mediante la formación directa del personal, transformando los hábitos diarios en un escudo activo para garantizar la continuidad del negocio.",
    mision: "Capacitar a las pequeñas organizaciones venezolanas en la identificación de riesgos digitales mediante auditorías de control básico y programas de concienciación humana, transformando la cultura interna de los trabajadores en un escudo activo contra ataques e incidentes informáticos.",
    vision: "Ser un modelo metodológico replicable de seguridad digital preventiva para el sector comercial de pequeña escala en Venezuela, demostrando que la protección de datos y la continuidad del negocio son alcanzables sin necesidad de altas inversiones en infraestructura tecnológica."
};


function renderInfoInstitucional() {
    
    const descContainer = document.getElementById('plan-descripcion-text');
    if (descContainer) {
        descContainer.textContent = PlanDOInfo.descripcion;
    }

   
    const misionContainer = document.getElementById('plan-mision-text');
    if (misionContainer) {
        misionContainer.innerHTML = `
            <div class="institutional-card mision-card">
                <h3><i class="fa-solid fa-bullseye"></i> Misión</h3>
                <p>"${PlanDOInfo.mision}"</p>
            </div>
        `;
    }

    
    const visionContainer = document.getElementById('plan-vision-text');
    if (visionContainer) {
        visionContainer.innerHTML = `
            <div class="institutional-card vision-card">
                <h3><i class="fa-solid fa-eye"></i> Visión</h3>
                <p>"${PlanDOInfo.vision}"</p>
            </div>
        `;
    }
}

function renderMethblocks() {
    const contenedor = document.getElementById('dynamic-blocks-container');
    if (!contenedor) return;

    if (typeof Methblock !== 'undefined') {
        contenedor.innerHTML = Methblock.map(b => `
            <div class="block-card">
                <div class="block-icon">
                    <i class="fa-solid ${b.icono || 'fa-shield-halved'}"></i>
                </div>
                <div class="block-body">
                    <span class="block-sub">${b.subtitulo}</span>
                    <h3>${b.titulo}</h3>
                    <p class="block-description">${b.descripcion}</p>
                </div>
            </div>
        `).join('');
    } else {
        console.warn("DynamicContent: 'Methblock' no está definido en main.js (todavía).");
    }
}


function renderCiberSecurityFails() {
    const contenedor = document.getElementById('fallas-container');
    if (!contenedor) return;

    if (typeof CiberSecurityfails !== 'undefined') {
        contenedor.innerHTML = CiberSecurityfails.map(f => `
            <div class="falla-card">
                <div class="falla-header">
                    <span class="falla-number">${f.numero}</span>
                    <h3>${f.titulo}</h3>
                </div>
                <p class="falla-text">${f.descripcion}</p>
            </div>
        `).join('');
    } else {
        console.warn("DynamicContent: 'CiberSecurityfails' no está definido en main.js todavía.");
    }
}

function renderStudyCases() {
    const contenedor = document.getElementById('casos-container');
    if (!contenedor) return;

    if (typeof StudyCases !== 'undefined') {
        contenedor.innerHTML = StudyCases.map(c => {
            
            const esNacional = c.categoria.toLowerCase().includes('nacional');
            const claseFiltro = esNacional ? 'nacional' : 'global';
            const iconoAmbito = esNacional ? 'fa-map-pin' : 'fa-earth-americas';

            return `
                <div class="caso-card ${claseFiltro}">
                    <div class="caso-badge-wrapper">
                        <span class="caso-ambito">
                            <i class="fa-solid ${iconoAmbito}"></i> ${c.categoria}
                        </span>
                    </div>
                    <h3>${c.titulo}</h3>
                    <p class="caso-details"><strong>Detalle:</strong> ${c.detalle}</p>
                    ${c.ocurrencia ? `<p class="caso-ocurrencia"><strong>Análisis:</strong> ${c.ocurrencia}</p>` : ''}
                </div>
            `;
        }).join('');
    } else {
        console.warn("DynamicContent: 'StudyCases' no está definido en main.js todavía.");
    }
}

function inicializarContenidoDinamico() {
    console.log("Plan DO: Renderizando contenidos informativos y de negocio...");
    renderInfoInstitucional();
    renderMethblocks();
    renderCiberSecurityFails();
    renderStudyCases();
}

document.addEventListener('DOMContentLoaded', inicializarContenidoDinamico)