function greedyColoring(adjacencyMatrix) {
    let numVertices = adjacencyMatrix.length;
    let colors = new Array(numVertices).fill(-1); // Инициализируем массив цветов
  
    // Цикл по всем вершинам
    for (let i = 0; i < numVertices; i++) {
      let availableColors = new Array(numVertices).fill(true); // Инициализируем доступные цвета
  
      // Проверяем цвета смежных вершин
      for (let j = 0; j < numVertices; j++) {
        if (adjacencyMatrix[i][j] === 1 && colors[j] !== -1) {
          availableColors[colors[j]] = false; // Помечаем цвет как недоступный
        }
      }
  
      // Находим первый доступный цвет
      for (let color = 0; color < numVertices; color++) {
        if (availableColors[color]) {
          colors[i] = color; // Присваиваем вершине цвет
          break;
        }
      }
    }
  
    return colors;
  }
  
  // Пример использования
  let adjacencyMatrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
  ];
  
  let colors = greedyColoring(adjacencyMatrix);
  console.log(colors); // Выводит: [0, 1, 2, 1]