# Prestadores_SuperIntendencia_Simulacion

## Descripción del Proyecto

Este proyecto, desarrollado en Python, simula un frontend para interactuar con la API de validación de prestadores de salud utilizada por el sistema PsicoAgendaAPP. Su objetivo principal es proporcionar una interfaz web que permita a los usuarios buscar y verificar la validez de un prestador de servicios de salud, particularmente psicólogos, consultando una base de datos que simula los registros de la superintendencia de salud.

## Características Principales

- **Interfaz de Usuario**: Incluye una interfaz web en HTML que permite a los usuarios buscar profesionales de la salud mediante su RUT. La página muestra una lista de profesionales y permite la búsqueda específica de un profesional utilizando su número de identificación.

- **Validación de RUT**: Valida el RUT ingresado por el usuario para asegurarse de que sea correcto antes de realizar la consulta en la base de datos, utilizando un algoritmo de verificación para comparar el dígito verificador proporcionado con el calculado.

- **Integración con la API**: Se conecta con la API desarrollada previamente para consultar los datos de los profesionales registrados. Muestra los detalles relevantes, incluyendo los antecedentes, si se encuentra un profesional con el RUT proporcionado.

- **Manejo de Errores**: Diseñado para manejar varios tipos de errores, como la ausencia del RUT, un formato de RUT incorrecto, o cuando un profesional no es encontrado en la base de datos.

- **Simulación de Entidad Reguladora**: Simula el comportamiento de una entidad reguladora, proporcionando un entorno de pruebas para la verificación de profesionales de la salud.

## Ejemplo de Uso

Un usuario puede ingresar el RUT de un psicólogo en la barra de búsqueda de la página web. Si el RUT es válido, el sistema consulta la base de datos y muestra los detalles del profesional, incluyendo su nombre completo, RUT, y los antecedentes asociados. Si el RUT no es válido o no se encuentra registrado, se muestra un mensaje de error adecuado.
