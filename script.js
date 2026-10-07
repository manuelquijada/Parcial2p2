document.getElementById("calcular").addEventListener("click", function () {

    const tipo = document.getElementById("tipo").value;
    const distancia = parseFloat(
        document.getElementById("distancia").value
    );

    const resultado = document.getElementById("resultado");

    if (isNaN(distancia) || distancia <= 0) {
        resultado.textContent = "Ingrese una distancia válida.";
        return;
    }

    let tarifaBase;
    let tarifa;

    if (tipo === "moto") {
        tarifaBase = 2.00;
        tarifa = tarifaBase + distancia * 0.35;
    } else {
        tarifaBase = 3.00;
        tarifa = tarifaBase + distancia * 0.60;
    }

    resultado.textContent =
        "Estimación del viaje: $" + tarifa.toFixed(2);
});