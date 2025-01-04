var menuButton = document.getElementById('menu-button');
var menu = document.getElementById('menu-links');
var content = document.getElementById('main');
const year = document.getElementById('year');

// Get actual year
var today = new Date();
year.innerHTML = today.getFullYear();

function toggleMenu(event) {
    event.preventDefault();
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
}

function closeMenu() {
    if (menu.style.display === 'block') {
        menu.style.display = 'none'
    }
}

menuButton.addEventListener('click', toggleMenu) // close menu if click in menu button
content.addEventListener('click', closeMenu) // close menu if click in content

document.addEventListener("DOMContentLoaded", function () {

    // Detectar si es móvil
    const isMobile = window.matchMedia("(max-width: 808px)").matches;

    if (isMobile) {

        // Seleccionar todos los toggles del dropdown
        const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

        if (dropdownToggles.length === 0) {
            console.warn('No elements found with the class "dropdown-toggle". Check your HTML structure.');
        }

        dropdownToggles.forEach(toggle => {
            // Agregar un estado de clic
            let isSubmenuOpen = false;

            toggle.addEventListener('click', function (event) {
                const submenu = toggle.nextElementSibling;

                if (submenu) {
                    if (!isSubmenuOpen) {
                        // Primer clic: Desplegar el submenú
                        event.preventDefault();
                        event.stopPropagation();
                        submenu.style.display = 'block';
                        isSubmenuOpen = true;
                    } else {
                        // Segundo clic: Permitir navegación
                        submenu.style.display = 'none';
                        isSubmenuOpen = false;
                    }
                } else {
                    console.warn('No submenu found for this toggle:', toggle);
                }
            });
        });

        // Prevenir cualquier evento en enlaces de submenús
        const submenuLinks = document.querySelectorAll('.submenu a');
        submenuLinks.forEach(link => {
            link.addEventListener('click', function (event) {
                event.stopPropagation(); // Evitar propagación del clic al padre
            });
        });
    } else {
    }
});
