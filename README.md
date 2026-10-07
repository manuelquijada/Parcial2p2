# Parcial2p2
Sistema de estimación de tarifas de transporte desarrollado con Python, HTML, CSS y JavaScript.

## Descripción

Este proyecto implementa un sistema de estimación de tarifas para servicios de transporte utilizando Programación Orientada a Objetos en Python y una interfaz web desarrollada con HTML, CSS y JavaScript.

## Parte Python

El sistema utiliza una clase padre llamada `ServicioTransporte`, de la cual heredan las clases:

- `Motocicleta`
- `Automovil`

Cada clase implementa el método `calcular_tarifa()` de forma polimórfica.

### Cálculo de tarifas

- Motocicleta: tarifa base + distancia × 0.35
- Automóvil: tarifa base + distancia × 0.60

Se crean al menos cuatro servicios de diferentes tipos y se procesan desde una misma colección, demostrando el uso de herencia y polimorfismo.

## Parte Frontend

La interfaz web permite:

- Seleccionar entre Motocicleta y Automóvil.
- Ingresar la distancia del viaje.
- Presionar el botón "Calcular estimación".
- Mostrar la tarifa estimada del viaje.

HTML se utiliza para la estructura de la página, CSS para el diseño visual y JavaScript para realizar el cálculo de la estimación en el navegador.

## Flujo de una aplicación web real

El flujo conceptual del sistema es:

**Usuario → Frontend → Backend → Respuesta → Frontend**

### Usuario
El usuario selecciona el tipo de transporte e ingresa la distancia del viaje.

### Frontend
El frontend recopila la información ingresada. En una aplicación real enviaría al backend datos como:

- Tipo de transporte.
- Distancia del viaje.

### Backend
El backend recibiría los datos y aplicaría la lógica de negocio correspondiente para calcular la tarifa.

### Respuesta
El backend devolvería información como:

- Tipo de transporte.
- Distancia.
- Tarifa calculada.

### Frontend
Finalmente, el frontend recibiría la respuesta y mostraría al usuario el costo estimado del viaje.

En este proyecto la comunicación entre el frontend y Python es conceptual, por lo que no se implementa una conexión real entre ambos.

## Estructura del proyecto

Parcial2p2/
- python/
  - modelos.py
  - main.py
- frontend/
  - index.html
  - styles.css
  - script.js
- README.md
