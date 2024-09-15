from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def instructores(request):
    data = [
        {
            'Nombre': 'Linus Torvalds',
            'Especialidad': 'Sistemas Operativos y Software de Código Abierto',
            'Descripcion': 'Linus Torvalds es el creador del sistema operativo Linux, uno de los pilares del software de código abierto. Su trabajo en el desarrollo del núcleo Linux ha tenido un impacto significativo en la informática moderna, incluyendo servidores, dispositivos móviles y supercomputadoras. Torvalds sigue siendo una figura clave en la comunidad de código abierto y en el desarrollo de sistemas operativos.',
            'imagen': 'images/linus.jpg',
            'imagen2': 'images/linus2.jpg'
        },
        {
            'Nombre': 'Grace Hopper',
            'Especialidad': 'Lenguajes de Programación y Compiladores',
            'Descripcion': 'Grace Hopper fue una pionera en el desarrollo de lenguajes de programación y compiladores. Es conocida por su trabajo en el desarrollo del lenguaje COBOL y por la creación de uno de los primeros compiladores. Hopper tuvo un impacto duradero en la informática, facilitando la creación de programas complejos y accesibles para la programación empresarial.',
            'imagen': 'images/grace.jpg',
            'imagen2': 'images/grace2.jpg'
        },
        {
            'Nombre': 'Donald Knuth',
            'Especialidad': 'Lenguajes de Programación y Compiladores',
            'Descripcion': 'Donald Knuth es conocido por su trabajo en el análisis de algoritmos y la creación de la serie de libros "The Art of Computer Programming". Sus contribuciones han influido profundamente en el campo de la informática y el desarrollo de algoritmos.',
            'imagen': 'images/donald.jpg',
            'imagen2': 'images/donald2.jpg'
        }
    ]
    return render(request, 'info.html', {'titulo': 'Instructores', 'info': data, 'color': '#3399ff'})

def cursos(request):
    data = [
        {
            'Nombre': 'Desarrollo Web con Django',
            'Duracion': '8 semanas',
            'Reseña': 'Este curso te introduce al framework Django, cubriendo desde los fundamentos básicos hasta técnicas avanzadas para el desarrollo de aplicaciones web robustas y escalables. Aprenderás a trabajar con modelos, vistas y plantillas, así como a implementar autenticación de usuarios y formularios. Al finalizar, serás capaz de construir aplicaciones web completas y funcionales utilizando las mejores prácticas del desarrollo en Django.',
            'imagen': 'images/django.jpg',
            'imagen2': 'images/django2.jpg'
        },
        {
            'Nombre': 'Introducción a Python para Ciencia de Datos',
            'Duracion': '6 semanas',
            'Reseña': 'Este curso está diseñado para principiantes en el campo de la ciencia de datos. Aprenderás los fundamentos de Python, cómo manejar datos utilizando bibliotecas como Pandas y NumPy, y cómo visualizar datos con Matplotlib y Seaborn. El curso cubre técnicas esenciales de análisis y manipulación de datos.',
            'imagen': 'images/datos.jpg',
            'imagen2': 'images/datos.jpg'
        },
        {
            'Nombre': 'Diseño de Interfaces de Usuario con React',
            'Duracion': '10 semanas',
            'Reseña': 'En este curso, exploramos el desarrollo de interfaces de usuario modernas utilizando React. Desde la creación de componentes hasta la gestión del estado con hooks, aprenderás a construir aplicaciones web interactivas y reactivas. El curso incluye prácticas en el uso de Redux para el manejo del estado global.',
            'imagen': 'images/react.jpg',
            'imagen2': 'images/react2.jpg'
        }
    ]
    return render(request, 'info.html', {'titulo': 'Cursos', 'info': data, 'color': '#ff3333'})

def egresados(request):
    data = [
        {
            'Nombre': 'Jeff Dean',
            'Nombre_de_la_empresa': 'Google (Senior Fellow)',
            'Opinion': 'Jeff Dean, Senior Fellow en Google, ha utilizado su educación en ingeniería informática para hacer contribuciones significativas a la infraestructura de Google y a la investigación en aprendizaje automático. Aprecia la educación que recibió por proporcionarle una base sólida en teoría y práctica.',
            'imagen': 'images/dean.jpg',
            'imagen2': 'images/dean2.jpg'
        },
        {
            'Nombre': 'Marissa Mayer',
            'Nombre_de_la_empresa': 'Yahoo! (Ex CEO)',
            'Opinion': 'Marissa Mayer ha sido una figura destacada en el campo de la tecnología. Su enfoque innovador en la gestión de productos y su capacidad para liderar equipos han sido fundamentales en el desarrollo de numerosos productos exitosos. Con una trayectoria impresionante en Yahoo y Google, Mayer ha demostrado ser una líder visionaria. Su influencia continúa marcando la pauta en la industria tecnológica.',
            'imagen': 'images/mayer.jpg',
            'imagen2': 'images/mayer2.jpg'
        },
        {
            'Nombre': 'Margaret Hamilton',
            'Nombre_de_la_empresa': 'Hamilton Technologies (Fundadora y CEO)',
            'Opinion': 'Margaret Hamilton, conocida por su trabajo en el desarrollo del software de navegación del Apollo 11, destaca cómo su formación le permitió liderar el desarrollo de sistemas críticos para la misión lunar.',
            'imagen': 'images/hamilton.jpg',
            'imagen2': 'images/hamilton2.jpg'
        }
    ]
    return render(request, 'info.html', {'titulo': 'Egresados', 'info': data, 'color': '#9b59b6'})