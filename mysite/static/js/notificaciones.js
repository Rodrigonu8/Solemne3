//Titulo de la notificación
Push.create("MoBike DUOC", {
 
    //Texto del cuerpo de la notificación
    body: "Inscribete en MoBike y disfruta de nuestro excelente servicio.",
 
    icon: "../img/Isotipo.png", //Icono de la notificación
    timeout: 6000, //Tiempo de duración de la notificación



    onClick: function() {
        //Función que se cumple al realizar clic cobre la notificación
        window.location = "localhost:8000"; //Redirige a la siguiente web
        this.close(); //Cierra la notificación
    },
});
