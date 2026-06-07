const Methblock = [ {
    id: 1,
    titulo: "Bloque 1: Diagnóstico Operativo",
    subtitulo: "Auditoría Básica",
    icono: "fa-clipboard-check",
    descripcion: "Levantamiento de formación inicial para evaluar los hábitos de los trabajadores"
}, 
{ id: 2,
  titulo: "Bloque 2: Diseño Estructural y Capacitación",
  subtitulo: "Cursos de Concienciación",
  icono: "fa-graduation-cap",
  descripcion: "Talleres prácticos  para reconocer y repeler amenazas comunes como la ingeniería social, el phising, el ransomware, malware, secuestro de cuentas, hackeo, o ser Robtop Games XD"
}, {
    id: 3,
    titulo: "Bloque 3: Gestión del Cambio Organizacional",
    subtitulo: "Convivencia Digital",
    icono: "fa-users-gear",
    descripcion: "Creación y entrega de manuales básicos de convivencia digital que sirvan como norma interna"
}, {
    id: 4,
    titulo: "Bloque 4: Validación y Métricas de Control",
    subtitulo: "Control e Impacto",
    icono: "fa-chart-line",
    descripcion: "Ejecución de pruebas prácticas y evaluaciones post-capacitación para comprobar la modificación de condcutas de riesgo en el entorno laboral real-"
}
]

const CiberSecurityfails = [
    {
        numero: "1",
        titulo: "Seguridad por Oscuridad",
        descripcion: "Creer que un sistema es seguro solamente a que 'nadie lo entiende' o porque la empresa es 'muy pequeña como para fijarse en ella' "
    },
    {
        numero: "2",
        titulo: "Brecha Conductual",
        descripcion: "Tener sistemas tecnológicos costosos pero el eslabón débil es el personal. Si un empleado anota la contraseña en un Post-it, la guarda como texto plano dentro de una tabla (ROBTOP) o cae en un mensaje de phising, adios a la infraestructura."
    },
    {
        numero: "3",
        titulo: "Almacenamiento y Tránsito Inseguro",
        descripcion: "Guardar datos críticos (como contraseñas, registros, cédulas) en texto plano (sin encriptarlas o hashearlas) o usar canales abiertos  para transferir información confidencial."
    }
]

const StudyCases = [
     {
        categoria: "Nacional (Venezuela)",
        titulo: "Secuestro de Whatsapp Business por 'Doble Factor' ausente o mal puesto",
        detalle: "Caso común en tiendas de ropa o bodegones que centralizan su atención al cliente en Whastapp Business",
        ocurrencia: "Falta de Concienciación, el personal operativo recibe una llamada o mensaje falso y termina siendo perjudicial para la empresa y el cliente, quedando expuestos, ya que el estafador (via SMS) toma control de la situación"
    }, 
    {
        categoria: "Nacional (Venezuela)",
        titulo: "Extracción de datos en puntos de venta y registro",
        detalle: "Algunas empresas adoptan la práctica de anotar manulamente en libretas o en archivos Excel los datos de los clientes (CI, TEL, RIF, HUELLA)",
        ocurrencia: "Representa una pérdida de control bestial: Guardar bitácoras financieras en texto plano o papel equivale a que si la liberta se pierde, expones todos los datos de los clientes XD"

    },
    {   
        categoria: "Global",
        titulo: "El hackeo a Capcom (2020)",
        detalle: "La empresa creadora de Resident Evil (El creador del juego: Shinji Mikami) sufrió un ataque de ransomware masivo donde se robaron cerca de 1TB de datos confidenciales",
        ocurrencia: "Los hackers ingresaron aprovechando un dispositivo de red VPN viejo y obsoleto que Capcom mantenía activo"
    }, 
    {   
        categoria: "Global",
        titulo: "Rockstar Games y el GTA VI (2022)",
        detalle: "Un hacker logró acceder a los servidores internos y filtró más de 90 videos del desarrollo de GTA VI",
        ocurrencia: "El atacante no rompió un muro de código inexpugnable mediante fuerza bruta; por via Slack, engañó a un empleado de la empresa haciéndose pasar por el equipo de soporte técnico para que le diera sus credenciales de acceso XDDDDDD"
    }
];

function renderContent() {
   const blocksContainer = document.getElementBYId('dynamic-blocks-container');
   if (blocksContainer) {
    blocksContainer.innerHTML = Methblock.map(bloque => `
            <div class="block-card">
                <div class="block-icon"><i class="fa-solid ${bloque.icono}"></i></div>
                <div class="block-body">
                    <span>${bloque.subtitulo}</span>
                    <h3>${bloque.titulo}</h3>
                    <p>${bloque.descripcion}</p>
                </div>
            </div>
        `).join('');
    }

    
    const fallasContainer = document.getElementById('fallas-container');
    if (fallasContainer) {
        fallasContainer.innerHTML = CiberSecurityfails.map(falla => `
            <div class="falla-card">
                <div class="falla-badge">${falla.numero}</div>
                <h3>${falla.titulo}</h3>
                <p>${falla.descripcion}</p>
            </div>
        `).join('');
    }

    
    const casosContainer = document.getElementById('casos-container');
    if (casosContainer) {
        casosContainer.innerHTML = StudyCases.map(caso => `
            <div class="caso-card ${caso.categoria.includes('Global') ? 'global' : 'nacional'}">
                <div class="caso-tag">${caso.categoria}</div>
                <h3>${caso.titulo}</h3>
                <p>${caso.detalle}</p>
            </div>
        `).join('');
    }
}

document.addEventListener('DOMContentLoaded', renderContent);
   