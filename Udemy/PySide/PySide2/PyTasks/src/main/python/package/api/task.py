import os
from pathlib import Path
import logging
import json


logging.basicConfig(level=logging.DEBUG)

TASKS_DIR = os.path.join(Path.home(), ".todo")
TASKS_FILEPATH = os.path.join(TASKS_DIR, "tasks.json")


def get_tasks():
    if os.path.exists(TASKS_FILEPATH):
        with open(TASKS_FILEPATH, "r") as f:
            try:
                return json.load(f)
            except ValueError as e:
                print("invalid json: %s" % e)
                return None
    else:
        return {}


def add_task(name):
    tasks = get_tasks()
    if name in tasks.keys():
        logging.error("Une tache avec le meme nom existe deja.")
        return False

    tasks[name] = False
    _write_tasks_to_disk(tasks=tasks)
    return True


def remove_task(name):
    tasks = get_tasks()
    if name not in tasks.keys():
        logging.error("La tache n'existe pas dans le dictionnaire")
        return False

    del tasks[name]
    _write_tasks_to_disk(tasks=tasks)
    return True

def set_tasks_statut(name, done=True):
    tasks = get_tasks()
    if name not in tasks.keys():
        logging.error("La tache n'existe pas.")
        return False

    tasks[name] = done
    _write_tasks_to_disk(tasks=tasks)
    return True

def _write_tasks_to_disk(tasks):
    if not os.path.exists(TASKS_DIR):
        os.makedirs(TASKS_DIR)

    with open(TASKS_FILEPATH, "w") as f:
        json.dump(tasks, f, indent=4)
        logging.info("Les taches ont bien ete mises à jour.")


if __name__ == '__main__':
    # add_task("Apprendre Python")
    # set_tasks_statut(name='Apprendre Python')
    remove_task(name='Apprendre Python')