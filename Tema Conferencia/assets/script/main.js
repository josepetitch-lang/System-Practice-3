import projectData from './work.js';
import { randomTips, showWelcomeMessage } from './extra.js';

const initConference = () => {
    console.log("Cargando sistema...");
    showWelcomeMessage("José Guanipa");
    console.log(projectData.getSummary());
    
    const tip = randomTips[Math.floor(Math.random() * randomTips.length)];
    console.log("Dato rápido:", tip);
};

initConference();