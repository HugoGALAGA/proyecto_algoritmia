const mapGrid = document.getElementById('map-grid');
const selOrigen = document.getElementById('origen');
const selDestino = document.getElementById('destino');
const selIntermedio = document.getElementById('intermedio');
const selModo = document.getElementById('modo');
const statusDiv = document.getElementById('status');

const POI_LIST = {
    1: "Centro Técnico",
    2: "Colegio Anglo",
    3: "CONACMI",
    4: "PNC",
    5: "Parque J. Batres",
    6: "La Torre",
    7: "PATSY",
    8: "Palacio Nacional",
    9: "Plaza Constitución",
    10: "Pizza Hut",
    11: "Almacén el Cisne",
    12: "Mercado Central",
    13: "Sist. Penitenciario",
    14: "Hotel",
    15: "Parque Colón",
    16: "Santuario Guadalupe",
    17: "G&T"
};

let COORDENADAS = {
    "s-1": { t: 15.3, l: 4.8 },
    "s-2": { t: 15.0, l: 12.8 },
    "s-3": { t: 15.6, l: 21.9 },
    "s-4": { t: 15.1, l: 29.7 },
    "s-5": { t: 15.3, l: 38.2 },
    "s-6": { t: 15.1, l: 46.5 },
    "s-7": { t: 14.9, l: 51.2 },
    "s-8": { t: 15.1, l: 55.0 },
    "s-9": { t: 15.1, l: 62.2 },
    "s-10": { t: 15.1, l: 71.6 },
    "s-11": { t: 15.1, l: 80.1 },
    "s-12": { t: 14.7, l: 84.6 },
    "s-13": { t: 15.1, l: 88.4 },
    "s-14": { t: 14.9, l: 96.2 },
    "s-15": { t: 34.9, l: 4.9 },
    "s-16": { t: 34.9, l: 13.2 },
    "s-17": { t: 35.1, l: 21.2 },
    "s-18": { t: 34.5, l: 30.0 },
    "s-19": { t: 35.1, l: 37.8 },
    "s-20": { t: 35.5, l: 46.1 },
    "s-21": { t: 35.1, l: 50.5 },
    "s-22": { t: 35.1, l: 54.8 },
    "s-23": { t: 34.8, l: 61.7 },
    "s-24": { t: 35.1, l: 63.2 },
    "s-25": { t: 35.5, l: 71.8 },
    "s-26": { t: 35.2, l: 79.6 },
    "s-27": { t: 55.0, l: 4.7 },
    "s-28": { t: 54.6, l: 13.0 },
    "s-29": { t: 54.5, l: 21.4 },
    "s-30": { t: 54.5, l: 29.5 },
    "s-31": { t: 55.0, l: 38.0 },
    "s-32": { t: 54.6, l: 47.1 },
    "s-33": { t: 54.8, l: 71.3 },
    "s-34": { t: 54.8, l: 79.9 },
    "s-35": { t: 53.8, l: 84.3 },
    "s-36": { t: 54.6, l: 88.3 },
    "s-37": { t: 55.0, l: 96.9 },
    "s-38": { t: 75.0, l: 5.4 },
    "s-39": { t: 74.4, l: 13.1 },
    "s-40": { t: 75.0, l: 21.2 },
    "s-41": { t: 75.0, l: 29.8 },
    "s-42": { t: 75.0, l: 37.9 },
    "s-43": { t: 74.9, l: 46.5 },
    "s-44": { t: 75.0, l: 71.9 },
    "s-45": { t: 74.9, l: 80.5 },
    "s-46": { t: 75.1, l: 88.7 },
    "s-47": { t: 74.6, l: 96.9 },
    "s-48": { t: 95.0, l: 4.7 },
    "s-49": { t: 94.7, l: 13.6 },
    "s-50": { t: 94.8, l: 21.7 },
    "s-51": { t: 94.4, l: 30.0 },
    "s-52": { t: 94.2, l: 38.3 },
    "s-53": { t: 94.1, l: 45.9 },
    "s-54": { t: 94.1, l: 54.6 },
    "s-55": { t: 95.0, l: 62.7 },
    "s-56": { t: 94.2, l: 71.4 },
    "s-57": { t: 94.5, l: 79.4 },
    "s-58": { t: 94.0, l: 87.9 },
    "s-59": { t: 93.8, l: 96.2 },
    "p-1": { t: 22.5, l: 4.6 },
    "p-2": { t: 55.6, l: 8.3 },
    "p-3": { t: 25.2, l: 21.3 },
    "p-4": { t: 49.6, l: 29.5 },
    "p-5": { t: 16.6, l: 28.4 },
    "p-6": { t: 35.1, l: 40.8 },
    "p-7": { t: 29.9, l: 46.8 },
    "p-8": { t: 34.9, l: 52.5 },
    "p-9": { t: 55.6, l: 50.3 },
    "p-10": { t: 81.5, l: 54.8 },
    "p-11": { t: 34.6, l: 68.9 },
    "p-12": { t: 54.6, l: 67.3 },
    "p-13": { t: 54.5, l: 86.1 },
    "p-14": { t: 15.8, l: 91.5 },
    "p-15": { t: 83.9, l: 92.0 },
    "p-16": { t: 74.8, l: 16.9 },
    "p-17": { t: 74.6, l: 34.1 },
};

function getCoord(id, type) {
    const key = (type === 'street') ? `s-${id}` : `p-${id}`;
    return COORDENADAS[key] || { t: 50, l: 50 };
}

function init() {
    for (let i = 1; i <= 59; i++) {
        createNode(i, 'street');
    }

    for (const [id, nombre] of Object.entries(POI_LIST)) {
        createNode(id, 'poi', nombre);
        
        const label = `${id}. ${nombre}`;
        const opt = `<option value="${id}">${label}</option>`;
        
        selOrigen.innerHTML += opt;
        selDestino.innerHTML += opt;
        selIntermedio.innerHTML += opt;
    }
    
    if(selDestino.options.length > 1) selDestino.selectedIndex = 1;
}

function createNode(id, type, name = "") {
    const el = document.createElement('div');
    el.className = `node ${type}`;
    el.id = `node-${type === 'street' ? 's' : 'p'}-${id}`;
    el.innerText = (type === 'poi') ? id : '';
    el.dataset.logicId = id;
    if (name) el.dataset.name = name;
    
    const pos = getCoord(id, type);
    el.style.top = pos.t + '%';
    el.style.left = pos.l + '%';
    
    makeDraggable(el);
    mapGrid.appendChild(el);
}

function toggleIntermedio() {
    const modo = selModo.value;
    const group = document.getElementById('group-intermedio');
    const label = document.getElementById('label-intermedio');
    
    if (modo === 'simple') {
        group.style.display = 'none';
    } else {
        group.style.display = 'flex';
        label.innerText = (modo === 'parada') ? 'PARADA EN (C)' : 'EVITAR (C)';
    }
}

async function calcularRuta() {
    const idA = selOrigen.value;
    const idB = selDestino.value;
    const modo = selModo.value;
    const idC = selIntermedio.value;
    const pesado = document.getElementById('trafico-pesado').checked;
    const ligero = document.getElementById('trafico-ligero').checked;

    document.querySelectorAll('.node').forEach(el => {
        el.classList.remove('active', 'start', 'end', 'inter');
    });

    statusDiv.innerText = "Calculando...";

    try {
        const res = await fetch('/calcular', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ 
                origen: idA, 
                destino: idB, 
                modo: modo, 
                intermedio: idC,
                trafico_pesado: pesado,
                trafico_ligero: ligero
            })
        });
        const data = await res.json();

        if(data.success) {
            statusDiv.innerHTML = `Ruta OK<br>Tiempo: ${data.distancia} min`;
            animar(data.ruta, idA, idB, (modo !== 'simple' ? idC : null));
        } else {
            statusDiv.innerText = "Error: " + data.message;
        }
    } catch (error) {
        statusDiv.innerText = "Error de conexión.";
    }
}

function animar(ruta, idStart, idEnd, idInter) {
    ruta.forEach((paso, i) => {
        setTimeout(() => {
            let selector = "";
            if (typeof paso === 'number') {
                selector = `#node-s-${paso}`;
            } else {
                selector = `.node.poi[data-name="${paso}"]`;
            }
            const el = document.querySelector(selector);
            if(el) el.classList.add('active');
        }, i * 100);
    });

    setTimeout(() => {
        document.getElementById(`node-p-${idStart}`).classList.add('start');
        document.getElementById(`node-p-${idEnd}`).classList.add('end');
        if(idInter) {
            const el = document.getElementById(`node-p-${idInter}`);
            if(el) el.classList.add('inter');
        }
    }, 0);
}

let isEditMode = false;
function toggleEditMode() {
    isEditMode = !isEditMode;
    document.body.classList.toggle('edit-mode');
    const btn = document.getElementById('edit-btn');
    if(btn) btn.innerText = isEditMode ? "GUARDAR" : "Editar";
    if (!isEditMode) exportCoords();
}

function makeDraggable(el) {
    let isDragging = false;
    el.addEventListener('mousedown', (e) => {
        if (!isEditMode) return;
        isDragging = true;
        el.style.cursor = 'grabbing';
        e.preventDefault();
    });
    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const rect = mapGrid.getBoundingClientRect();
        let x = e.clientX - rect.left;
        let y = e.clientY - rect.top;
        el.style.left = ((x / rect.width) * 100).toFixed(1) + '%';
        el.style.top = ((y / rect.height) * 100).toFixed(1) + '%';
    });
    window.addEventListener('mouseup', () => { isDragging = false; });
}

function exportCoords() {
    console.log("let COORDENADAS = {");
    document.querySelectorAll('.node').forEach(el => {
        const key = el.id.replace('node-', '');
        console.log(`    "${key}": { t: ${parseFloat(el.style.top)}, l: ${parseFloat(el.style.left)} },`);
    });
    console.log("};");
}

init();