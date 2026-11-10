import random

rimas = [
    "Estoy en el top, no me bajo ni un poco",
    "Empecé desde abajo y ahora sueno como un loco",
    "Vengo de la calle, donde aprendí a soñar",
    "No tenía nada, pero tenía flow para dar",
    "Tengo un sueño y no lo voy a soltar",
    "De la calle al top me van a escuchar",
    "Tengo fuego en el pecho y no me voy a apagar",
    "Mi barrio me enseñó a nunca rajarme",
    "Lo hago por mi familia, por mi madre y mi fe",
    "Mi futuro es brillante, lo puedo ver, de Tijuana pa'l mundo, me van a conocer"
]

print("🎤 Mi Hit Hook dice:")
for rima in random.sample(rimas, 4):
    print(rima)
