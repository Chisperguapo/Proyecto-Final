function editField(field) {
    document.getElementById('edit-' + field).style.display = 'flex';
}

function closeEdit(field) {
    document.getElementById('edit-' + field).style.display = 'none';
}

// Función para manejar el clic en el botón de configuración
function changeColorOnClick(event){
    // Se define una lógica que va a tener como funcionalidad para desactivar cualquier otro click en el momento
    var button = document.querySelectorAll('.sidebar');
    button.forEach(function(button){
        button.classList.remove('active');
    });

    // Añadir la clase 'active' al botón que fue clickeado
    event.currentTarget.classList.add('active');
}

// Agregar el evento de clic a todos los botones en la barra lateral en settings.
document.querySelectorAll('.sidebar').forEach(function(button){
    button.addEventListener('click', changeColorOnClick);
});