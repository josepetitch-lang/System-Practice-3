function enviarMensaje() {
    let input = document.getElementById("mensajeInput");
    let historial = document.getElementById("chat-historial");
    if(input.value.trim() !== "") {
        let msg = document.createElement("p");
        msg.innerHTML = `[${new Date().toLocaleTimeString()}] > Transmitiendo: ${input.value}`;
        historial.prepend(msg);
        input.value = "";
    }
}

let indice = 0;
const preguntas = [
    "¿Qué es el ruido en la comunicación?",
    "¿Cuál es el rol del EMISOR?",
    "¿Por qué es vital el FEEDBACK?",
    "¿Qué es el CANAL?",
    "¿Qué es la DECODIFICACIÓN?"
];

function iniciarTest() {
    let area = document.getElementById("pregunta-area");
    if (indice < preguntas.length) {
        area.innerText = "Pregunta " + (indice + 1) + ": " + preguntas[indice];
        indice++;
    } else {
        area.innerText = "Diagnóstico completado. Sistema estable.";
    }
}
function verificarRespuesta() {
    let respuesta = document.getElementById("respuestaInput").value;
    let preguntaActual = document.getElementById("pregunta-area").innerText;
    let historial = document.getElementById("chat-historial");

    if(respuesta.trim() !== "") {
        l
        let registro = document.createElement("p");
        registro.style.color = "#00ffff"; // Cambiamos color para diferenciar xd
        registro.innerHTML = `[SISTEMA] Respuesta recibida a "${preguntaActual.substring(0, 15)}...": ${respuesta}`;
        historial.prepend(registro);
        
        document.getElementById("respuestaInput").value = "";
    } else {
        alert("¡Error de transmisión! No se detectaron datos de respuesta.");
    }
}