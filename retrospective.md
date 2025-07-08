##  Reflexión y aprendizaje

Diría que una de las cosas más desafiantes fue aprender a manejar *Git* y entender cómo debía ser el flujo de trabajo en equipo. Al principio no sabíamos ni cómo bifurcar las ramas correctamente. Con el tiempo fuimos entendiendo que cada funcionalidad debía trabajarse en su propia rama feature/*, saliendo desde develop.

Uno de los errores comunes al inicio fue que, cuando alguien creaba una rama nueva, no sabíamos cómo traer los cambios que ya estaban en develop. Solíamos hacer un merge desde develop, pero después aprendimos que lo correcto era hacer un pull origin develop dentro de la rama feature para obtener los cambios actualizados.

También nos costó al principio entender cómo funcionaban los *Pull Requests*. En lugar de usarlos, hacíamos merge directamente desde local hacia develop. Más adelante entendimos cómo hacer push desde nuestras ramas y abrir el pull request desde GitHub, lo cual facilitó mucho el trabajo colaborativo y el control del proyecto.

Una vez tuvimos todas las funcionalidades integradas en develop, se hizo un **Pull Request final hacia main**, consolidando el proyecto completo.

Con muchos errores, bloqueos y confusiones al inicio, logramos adaptarnos y aplicar buenas prácticas de desarrollo. Esta experiencia nos ayudó no solo a mejorar nuestro código, sino también a *trabajar en equipo y entender la importancia del control de versiones con Git*  adaptarnos a las buenas practicas y manejar una cultura Scrum