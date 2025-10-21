# IPC2_Proyecto3_201503846
Desarrollar una solución integral que implemente un API que brinde servicios utilizando el Protocolo HTTP bajo el concepto de programación orientada a objetos (POO) y el uso de bases de datos

Tecnologias Chapinas S.A consiste en crear configuraciones de infraestructura que agrupan recuros para una arquitectura de despliegue de aplicaciones, los clinetes de Tecnologias Chapinas S.A se registran ingresando su nombre, NIT, direccion fisica y correo electronico

una vez ingreado reciben en su correo un usuario y clave con la que pueden ingresar a una consola donde pueden crear, modifica y elminar instacias las instancias representan la configuracion que el usuario puede seleccionar en algunas categorias  que brinda Tecnologias Chapinas S.A

Cada categoría define “N” configuraciones, estas configuraciones agrupan recursos que
son integrados para brindar máquinas virtuales que puedan satisfacer los requerimientos
de carga de trabajo definidos en la categoría. Entre los recursos que una configuración
puede incluir se encuentran: núcleos, memoria RAM, almacenamiento secundario, sistema
operativo, base de datos, entre otros. Cada recurso que se puede incluir en una
configuración posee una dimensional que se utiliza como métrica para el recurso y un
costo por hora de este recurso, así, por ejemplo, para la memoria RAM su dimensional son
GiB (Gigabytes) y su costo por hora $ 0.75, mientras que para los núcleos su dimensional
es unidades y su costo por hora $.1.20.

# Mensaje de entrada para configurar los objetos definidos 
Para poder crear la información necesaria para brindar y cobrar por los servicios que
presta Tecnologías Chapinas, S.A. se utilizará un mensaje XML

Los valores y atributos antecedidos con el símbolo “$” se describen en el apartado “Reglas y consideraciones del formato para cada mensaje recibido”

```
<?xml version="1.0"?>
<archivoConfiguraciones>
    <listaRecursos>
        <recurso id="idRecurso">
        <nombre> nombreRecurso </nombre>
        <abreviatura> abreviaturaRecurso </abreviatura>
        <metrica> NombreMetrica </metrica>
        <tipo> $tipoRecurso </tipo>
        <valorXhora> valorNumerico </valorXhora>
    </recurso>
 ...
</listaRecursos>
<listaCategorias>
    <categoria id="idCateoria">
        <nombre> nombreCategoria </nombre>
        <descripcion> descripcionCategoria </descripcion>
        <cargaTrabajo> descripcionCargaTrabajo </cargaTrabajo>
    <listaConfiguraciones>
        <configuracion id="idConfiguracion">
            <nombre> nombreConfiguracion </nombre>
            <descripcion> descripcionConfiguracion </descripcion>
            <recursosConfiguracion>
            <recurso id="idRecurso"> cantidadRecurso </recurso>
            ...
            </recursosConfiguracion>
        </configuracion>
    ...
    </listaConfiguraciones>
    </categoria>
 ...
</listaCategorias>
<listaClientes>
    <cliente nit="$nitCliente">
    <nombre> nombreCliente </nombre>
    <usuario> nombreUsuario </usuario>
    <clave> claveUsuario </clave>
    <direccion> direccionCliente </direccion>
    <correoElectronico> eMailCliente </correoElectronico>
        <listaInstancias>
            <instancia id="idInstancia">
            <idConfiguracion> idConfiguracion </idConfiguracion>
            <nombre> nombreInstancia </nombre>
            <fechaInicio> descripcionFecha </fechaInicio>
            <estado> $estado </estado>
            <fechaFinal> $descripcionFecha </fechaFinal>
            </instancia>
            ...
        </listaInstancias>
    ...
    </cliente>
    ...
</listaClientes>
</archivoConfiguraciones>
```

# Mensaje de entrada para notificar el consumo de recursos
Una vez los recursos, clientes e instancias se encuentren definidos en la nube de
Tecnologías Chapinas, S.A., se reciben mensajes que notifican el tiempo utilizado por cada
instancia, de manera que sea posible establecer los montos a facturar a cada cliente,
dependiendo del tiempo que utilice sus instancias y el valor definido para cada recurso.

```
<?xml version="1.0"?>
<listadoConsumos>
    <consumo nitCliente="$nit" idInstancia="id">
        <tiempo> $tiempoConsumido </tiempo>
        <fechaHora> $descripcionFechaHora </fechaHora>
    </consumo>
    ...
</listadoConsumos>
```

## Reglas y consideraciones del formato para cada mensaje recibido
* Tipos de recursos ($tipoRecuso) pueden ser 2 hardware y software
* Fecha ($descripcionFecha) Todos los datos que sean de tipo fecha podrán
contener cualquier hilera, siempre y cuando contenga una secuencia de la forma
dd/mm/yyyy que represente una fecha válida, cualquier otra información será
descartada.
* Fechas y horas ($descripcionFechaHora): Todos los datos que sean de tipo fecha
y hora podrán contener cualquier hilera, siempre y cuando contenga una secuencia
de la forma dd/mm/yyyy hh24:mi
* Estado de la instancia ($estado): Toda instancia registrada por un cliente podrá
estar en estado “Vigente” o “Cancelada”. Toda instancia “Cancelada” deberá tener
una fecha final de la vigencia, de otra forma, la fecha de final de vigencia no tendrá
valor.
* Atributo NIT ($NIT): Debe ser un NIT válido, es decir, una sucesión de números del
0 al 9 seguidos por un guion y un dígito de validación (valor entre 0 y 9 o K). Ejs.
34300-4, 110339001-K, etc.
* Consumos ($tiempoConsumido): Todos los consumos se reportan en horas (tag
tiempo), este valor puede contener decimales, por ejemplo, si el recurso se utilizó por
1 hora y 45 minutos, se reportará un uso de 1.75 horas.

# Frontend
Para realizar el frontend deberá utilizarse el framework Django, el cual trabaja con el patrón MVT (Modelo-Vista-Template).

## Componentes:
* Enviar mensaje de configuración: Se desplegará una pantalla para gestionar el
envío del mensaje de entrada con extensión .xml con una o varias solicitudes de
creación de elementos del sistema. Deberá mostrar un mensaje indicando si el
mensaje fue enviado exitosamente y el resultado de este, por ejemplo, 3 nuevos
clientes creados, 7 nuevas instancias creadas, 2 nuevos recursos creados, 1 nueva
categoría creada.
* Enviar mensaje de consumo: Se desplegará una pantalla para gestionar el envío
del mensaje de entrada con extensión .xml con una o varias solicitudes de consumo
de recursos del sistema. Deberá mostrar un mensaje indicando si el mensaje fue
enviado exitosamente y el resultado de este, por ejemplo, 3 consumos procesados.
* Operaciones del sistema: En este apartado se debe de tener las siguientes opciones:
* *  Inicializar sistema: Al seleccionar esta opción se eliminarán todos los datos
en la base de datos para iniciar una prueba sin datos previos.
* * Consultar Datos: Al seleccionar esta opción se podrá chequear la estructura
de información que actualmente maneja el sistema, es decir, podrá ver las
categorías, recursos y configuraciones disponibles
* * Creación de nuevos datos: Al seleccionar esta opción se podrá crear nueva
información, es decir, podrá crear nuevas categorías, nuevos recursos, nuevas
configuraciones, nuevos clientes o registrar nuevas instancias, cancelar
instancias
* * Proceso de facturación: Al seleccionar esta opción se podrá elegir un rango
de fechas y se generará una factura para cada cliente por todos los recursos
consumidos no facturados previamente. La factura incluye la siguiente
información: Número de factura (debe ser único), NIT del cliente al que se le
emite la factura, fecha de la factura (último día incluido en el rango
seleccionado), monto a pagar
* *  Reportes en PDF: Deberá generar 2 reportes con las siguientes características:
* * * Detalle de factura: Este reporte permitirá seleccionar una factura y
presentará los datos de la factura y el detalle de lo que incluye la
factura. Debe ser posible ver el monto a pagar por cada instancia, los
tiempos en que fue consumida cada instancia y deberá mostrar el
detalle de recursos, así como el aporte de cada recurso al cobro de la
factura.
* * * Análisis de ventas: Este reporte permitirá analizar la información de
venta, permitiendo 2 opciones: a) Analizar las categorías y
configuraciones que más ingresos generan para la empresa en un
rango de fechas, b) Analizar los recursos que más ingresos generan
para la empresa en un rango de fechas.
* Ayuda: desplegará 2 opciones, una para visualizar información del estudiante y otra
para visualizar la documentación del programa.

# Backend
Este servicio consiste en una o varias APIs que brindarán servicios utilizando el protocolo
HTTP, su funcionalidad principal es procesar los datos recibidos del programa 1, luego de
procesar los datos es necesario que estos sean almacenados en uno o varios archivos xml
que representan la base de datos, este servicio también tiene la funcionalidad de devolver los
datos que fueron almacenados para que sean mostrados como respuesta a las solicitudes
realizadas por el “Programa 1 – Frontend”.

Para la realización de este servicio debe utilizarse el framework Flask. El estudiante deberá
definir por su propia cuenta los métodos que necesitará para la realización de este servicio.
Esto significa que debe implementar tantos métodos como necesite para consumir la API.

