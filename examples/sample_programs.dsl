// Ejemplo básico
x = 10;
y = 5;
z = x + y;
print("Suma:");
print(z);

// Ejemplo de matriz
matriz = [[1, 2], [3, 4]];
print("Matriz:");
print(matriz);
print("Transpuesta:");
print(transpose(matriz));

// Ejemplo de ML
X = [[1], [2], [3], [4]];
y = [2, 4, 6, 8];
modelo = linear_regression(X, y);
print("Predicción para x=5:");
print(predict(modelo, [[5]]));

// Gráfica simple
datos = [1, 4, 2, 8, 5, 3];
print("Gráfica:");
plot(datos);