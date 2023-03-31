# Docker Swarm Example

Este ejemplo demuestra cómo configurar un clúster de Docker Swarm con un nodo manager y un nodo worker para ejecutar un servicio web simple. El servicio web muestra un mensaje personalizado enviado desde el nodo worker en los registros del servicio en el nodo manager.

## Pasos realizados

1. Inicializamos Docker Swarm en el nodo manager y unimos el nodo worker al clúster.
2. Creamos una red overlay para permitir la comunicación entre los nodos.
3. Desarrollamos una aplicación web simple en Python utilizando Flask.
4. Creamos un Dockerfile para empaquetar la aplicación en una imagen de Docker.
5. Construimos la imagen de Docker en el nodo manager.
6. Creamos y desplegamos el servicio web en el clúster de Docker Swarm, asegurándonos de que se ejecute en el nodo worker.
7. Enviamos un mensaje personalizado al servicio web desde el nodo worker utilizando `curl`.
8. Verificamos los registros del servicio en el nodo manager para ver el mensaje enviado desde el nodo worker.

