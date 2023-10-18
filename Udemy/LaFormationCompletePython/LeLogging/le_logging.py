import logging

""" on definit ci-dessous le niveau de debug que l'on souhaite
 par defaut le niveau est sur warning, et ci-dessous il est à DEBUG"""
# logging.basicConfig(level=logging.DEBUG)

"""
level : parametre pour decrire le niveau de log desire. Choix entre
debug, info, warning, error et critical.

filename et filemode(w, a): Les parametres pour ecrire dans un fichier

format: Le parametre format afin de formatter le fichier affiché
"""

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s : %(levelname)s : %(message)s')

logging.debug("La fonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")
