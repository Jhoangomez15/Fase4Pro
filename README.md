
# Fase4Pro

## Fase 4 - Componente práctico - Prácticas simuladas

### Sistema Integral de Gestión de Clientes, Servicios y Reservas

**Empresa:** Software FJ

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación en Python para gestionar clientes, servicios y reservas de la empresa Software FJ.

El sistema permite registrar clientes, validar sus datos, administrar diferentes tipos de servicios y gestionar reservas mediante operaciones de confirmación, cancelación y procesamiento.

La aplicación utiliza programación orientada a objetos, herencia, encapsulamiento, abstracción y polimorfismo.

## 2. Objetivo

Desarrollar una aplicación funcional que permita gestionar clientes, servicios y reservas, aplicando los principios de programación orientada a objetos y el manejo de excepciones en Python.

## 3. Servicios disponibles

El sistema cuenta con tres servicios especializados:

- **Reserva de salas:** permite calcular el costo según las horas reservadas y aplicar el impuesto correspondiente.
- **Alquiler de equipos:** calcula el costo de acuerdo con los días de alquiler y los descuentos aplicables.
- **Asesoría especializada:** calcula el costo según el número de sesiones y el nivel de complejidad.

## 4. Conceptos de programación orientada a objetos aplicados

- **Abstracción:** se utilizan las clases abstractas `EntidadSistema` y `Servicio`.
- **Encapsulamiento:** se protegen los datos mediante atributos privados y propiedades.
- **Herencia:** los clientes y servicios especializados reutilizan las características de sus clases base.
- **Polimorfismo:** cada servicio implementa su propia versión de los métodos `calcular_costo()` y `describir()`.
- **Sobrecarga mediante parámetros opcionales:** se utilizan parámetros opcionales para permitir diferentes formas de calcular los costos, como descuentos, impuestos y niveles de complejidad.

## 5. Estructura del proyecto

- `entidad.py`: contiene la clase abstracta general del sistema.
- `cliente.py`: administra los datos y las validaciones de los clientes.
- `servicio.py`: contiene la clase abstracta base de los servicios.
- `reservasala.py`: implementa las reservas de salas.
- `alquiler.py`: implementa el alquiler de equipos.
- `Asesoria.py`: implementa las asesorías especializadas.
- `Reserva.py`: gestiona la creación, confirmación, cancelación y procesamiento de reservas.
- `excepciones.py`: contiene las excepciones personalizadas.
- `main.py`: ejecuta las operaciones de simulación del sistema.
- `registro_software_fj.log`: almacena los eventos y errores generados durante la ejecución.

## 6. Tecnologías utilizadas

- Lenguaje de programación Python.
- Programación orientada a objetos.
- Manejo de excepciones.
- Módulo `logging` para el registro de eventos y errores.
- Git y GitHub para el control de versiones.

## 7. Ejecución del proyecto

Para ejecutar la aplicación, se debe tener Python instalado y abrir una terminal en la carpeta del proyecto.

Ejecutar el siguiente comando:

```bash
py main.py
```

El programa realizará diez operaciones de simulación, incluyendo registros válidos, datos incorrectos, creación y procesamiento de reservas, cancelaciones y manejo de errores.

## 8. Manejo de errores

El sistema utiliza excepciones personalizadas para controlar situaciones relacionadas con clientes, servicios y reservas.

También registra los eventos y errores en el archivo `registro_software_fj.log`, permitiendo consultar lo ocurrido durante la ejecución.

## 9. Conclusión

El desarrollo de este proyecto permitió aplicar los conceptos de programación orientada a objetos en una situación práctica, integrando clases abstractas, herencia, encapsulamiento, polimorfismo y manejo de excepciones para construir un sistema organizado y funcional.
