import os
from app import app

# Brojač datoteka u folderu - koristi se za prikazivanje prošla i sljedeća lekcija
def count_lections():
    lections_directory = os.path.join(app.root_path, 'static', 'lections')
    lection_files = [filename for filename in os.listdir(lections_directory) if filename.endswith('.svg')]
    return len(lection_files)
