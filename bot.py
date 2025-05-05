print("¡Bienvenido al chatbot jurídico!")
print("Opciones disponibles: divorcio, custodia, pensión alimenticia")

# Solicitar consulta del usuario
tema = input("Escribe tu consulta: ")

# Respuestas del bot
if tema.lower() == "divorcio":
    print("El divorcio puede ser de mutuo acuerdo o contencioso. Se tramita ante un juez o notario según el caso.")
elif tema.lower() == "custodia":
    print("La custodia de los hijos se determina según el interés superior del menor.")
elif tema.lower() == "pensión alimenticia":
    print("La pensión alimenticia es un derecho de los hijos y se calcula según los ingresos del responsable.")
else:
    print("Lo siento, aún no tengo información sobre ese tema.")
