const puzzleContainer = document.getElementById('puzzle');

let tiles = [];
let emptyTileIndex = 15;

// Initialize puzzle
function initPuzzle() {
    tiles = Array.from({ length: 15 }, (_, i) => i + 1).concat(null);
    shuffleArray(tiles);
    renderPuzzle();
}

// Render the puzzle on the page
function renderPuzzle() {
    puzzleContainer.innerHTML = '';
    tiles.forEach((number, index) => {
        const tile = document.createElement('div');
        tile.classList.add('tile');
        if (number !== null) {
            tile.textContent = number;
            tile.addEventListener('click', () => moveTile(index));
        } else {
            tile.classList.add('empty');
        }
        puzzleContainer.appendChild(tile);
    });
}

// Shuffle the array
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// Move a tile
function moveTile(index) {
    const emptyIndex = tiles.indexOf(null);
    if (isAdjacent(index, emptyIndex)) {
        [tiles[index], tiles[emptyIndex]] = [tiles[emptyIndex], tiles[index]];
        renderPuzzle();
    }
}

// Check if two indexes are adjacent
function isAdjacent(index1, index2) {
    const row1 = Math.floor(index1 / 4);
    const col1 = index1 % 4;
    const row2 = Math.floor(index2 / 4);
    const col2 = index2 % 4;
    return (Math.abs(row1 - row2) === 1 && col1 === col2) || (Math.abs(col1 - col2) === 1 && row1 === row2);
}

initPuzzle();
