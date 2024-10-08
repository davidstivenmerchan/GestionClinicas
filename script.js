document.getElementById("buscar-btn").addEventListener("click", function() {
    const numeroOrden = document.getElementById("numero-orden").value.trim();

    if (numeroOrden) {
        fetch('/buscar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ numero_orden: numeroOrden })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado-busqueda").textContent = data.message;
        });
    }
});

document.getElementById("form-medicamentos").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevenir el envío del formulario por defecto
    const nombreMedicamento = document.getElementById("nombre-medicamento").value;
    const cantidadMedicamento = document.getElementById("cantidad-medicamento").value;

    // Simulación de orden de medicamento
    const mensaje = `Ordenado ${cantidadMedicamento} de ${nombreMedicamento}.`;
    document.getElementById("resultado-medicamentos").textContent = mensaje;

    // Limpiar el formulario
    document.getElementById("form-medicamentos").reset();
});