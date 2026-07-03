const quizData = [
    { pregunta: "¿Qué es la comunicación asertiva?", respuesta: "Defender tus derechos respetando al otro." },
    { pregunta: "¿Cuál es el ruido en una comunicación?", respuesta: "Cualquier interferencia que distorsiona el mensaje." }
];

export const iniciarSimulador = (): void => {
    quizData.forEach((item, index) => {
        const respuesta = prompt(`Pregunta ${index + 1}: ${item.pregunta}`);
        if (respuesta && respuesta.toLowerCase().includes("distorsión")) {
            alert("¡Correcto! Entiendes la base de la comunicación.");
        } else {
            alert("Intenta de nuevo, recuerda la teoría del marco teórico.");
        }
    });
};

const preguntas = [
    { 
        pregunta: "Alguien te interrumpe constantemente, ¿qué haces?", 
        opciones: ["Me callo", "Lo interrumpo yo también", "Le digo: 'Me gustaría terminar mi idea'"],
        correcta: 2 
    },
    { 
        pregunta: "¿Qué es el ruido en un canal de comunicación?", 
        opciones: ["Música alta", "Cualquier interferencia que distorsiona el mensaje", "Hablar bajito"],
        correcta: 1 
    }
];

let indicePregunta = 0;

const renderizarPregunta = (): void => {
    const contenedorPregunta = document.getElementById('pregunta')!;
    const contenedorOpciones = document.getElementById('opciones')!;
    
    const pActual = preguntas[indicePregunta];
    contenedorPregunta.innerText = pActual.pregunta;
    contenedorOpciones.innerHTML = '';
    
    pActual.opciones.forEach((opc, i) => {
        const btn = document.createElement('button');
        btn.innerText = opc;
        btn.onclick = () => verificarRespuesta(i);
        contenedorOpciones.appendChild(btn);
    });
};

const verificarRespuesta = (seleccion: number): void => {
    if (seleccion === preguntas[indicePregunta].correcta) {
        alert("¡Correcto! Eso es comunicación asertiva.");
    } else {
        alert("Incorrecto. Intenta considerar la postura del receptor.");
    }
    
    if (indicePregunta < preguntas.length - 1) {
        indicePregunta++;
        renderizarPregunta();
    } else {
        alert("¡Simulador completado!");
    }
};

const btnSiguiente = document.querySelector('.btn-next') as HTMLButtonElement;

btnSiguiente?.addEventListener('click', () => {
    console.log("¡Conectado! El botón funciona.");
});

const container = document.getElementById('quiz-container')!;
const pTexto = document.getElementById('pregunta-texto')!;
const optContainer = document.getElementById('opciones-container')!;

const pregunta = container.dataset.pregunta;
const opciones = container.dataset.opciones?.split(',');
const correcta = parseInt(container.dataset.correcta || "0");

pTexto.innerText = pregunta || "";

opciones?.forEach((opc, i) => {
    const btn = document.createElement('button');
    btn.innerText = opc;
    btn.onclick = () => alert(i === correcta ? "¡Correcto!" : "Intenta de nuevo");
    optContainer.appendChild(btn);
});