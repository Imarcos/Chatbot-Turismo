# Chatbot-Turismo
He creado este chatbot para sugerencias de planes interesantes y originales cuando estamos en otra ciudad o pais de vacaciones, incluidos free tour y excursiones.
## Parte I: enfoque Top-Down


He programado el chatbot usando el cliente de Pandorabots. El bot pregunta al usuario la ciudad donde va a viajar y acontinuación pregunta por sus gustos.Si prefiere un plan cultural (como museos, galerias de arte o rutas historicas), le preguntará si le gusta la historia o la pintura y ofrece un plan en funcion de la respuesta. Tambien puede preferir un plan gastronómico e igual le pregunta si prefiere comida tradicional o moderna.

Al hacerlo he notado que las principales ventajas que proporcina este cliente es que es muy intuitivo y amigable, ya que puedes probar rapidamente el codigo en AIML y obtener una simulación parecida al resultado final, además de poder añadir elementos html como links, emoticonos e imagenes.
La principal desventaja que le veo es que aiml es muy estricto. Para poder seguir el flujo de la conversación las respuestas pasadas al bot deben coincidir con el pattern, no obviando faltas de ortografia. Es posible redirigir la respuestas mediante las variables, la etiqueta that. El resultado es que la conversación resulta natural.

## Parte I: enfoque Top-Down

He usado la web de ML4K, para dividir las respuestas del chatbot en categorias, clasificarlas y crear el modelo, estas son gastronomia, arte y otros, en cada una de ellas he incluido posibles entradas que puede introducir el usuario. Por ejemplo para la categoria arte he incluido: quiero ver museos o me gusta el arte. 

## Parte III: ¿lo mejor de los dos mundos?

En esta tercera parte he combinado el aiml con el codigo en program-y en jupyter notebook pasandole la respuesta clasificada en el paso anterior como pattern para el bot. 

Tras probar estos tres modelos podemos concluir que el tercer enfoque es lo mejor para obtener un asistente conversacional que se "parezca" a un ser humano. Pandorabots es muy intuitivo y amigable, ya que puedes probar rapidamente el codigo en AIML y obtener una simulación parecida al resultado final, además de que la interfaz es parecida a una ventana de chat, y se pueden mostrar elementos html como links, emoticonos e imagenes.
La principal desventaja que le veo es que aiml es muy estricto. Para poder seguir el flujo de la conversación las respuestas pasadas al bot deben coincidir con el pattern, no obviando faltas de ortografia. Aunque,es posible redirigir la respuestas mediante las variables, la etiqueta that. 
El segundo enfoque solo clasifica las respuesta sin tener en cuenta el dialogo con el usuario. 

Enlace al video demostración: https://drive.google.com/file/d/1pQNsUAZnKyJovENZL-vTlhmNnIXWJbWD/view?usp=sharing
