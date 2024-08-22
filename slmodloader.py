import zipfile
import os
import shutil

name_mod = ""
folder_path = ""

def extract_slmod(archive_name):
    # Renommer l'archive avec l'extension zip temporairement
    zip_archive = archive_name.replace('.slmod', '.zip')
    os.rename(archive_name, zip_archive)
    
    # Extraire l'archive
    with zipfile.ZipFile(zip_archive, 'r') as archive:
        archive.extractall("extracted_content")
    
    # Renommer l'archive avec l'extension personnalisée
    os.rename(zip_archive, archive_name)
    
def loadmods(name_mod):
    if name_mod == "*5ç$":
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Chemin du dossier (à adapter selon votre situation)
        folder_path = os.path.join(current_dir, "Mods")
        
        # Lister les fichiers dans le dossier
        files = os.listdir(folder_path)

        # Boucle for avec filtrage des fichiers .slmod
        for file_name in files:
        # Vérifier si le fichier a l'extension .slmod
            if file_name.endswith('.slmod'):
                # Utiliser le nom du fichier
                print(f".slmod file found : {file_name}")
                
                # Renommer l'archive avec l'extension zip temporairement
                zip_archive = file_name.replace('.slmod', '.zip')
                file_path = os.path.join(folder_path, file_name)
                zip_path = os.path.join(folder_path, zip_archive)
                file_path = file_path.replace("extracted_content", "Mods")
                zip_path = zip_path.replace("extracted_content", "Mods")
                os.rename(file_path, zip_path)
    
                # Extraire l'archive
                with zipfile.ZipFile(zip_path, 'r') as archive:
                    archive.extractall("extracted_content")
    
                # Renommer l'archive avec l'extension personnalisée
                os.rename(zip_path, file_path)
                
                folder_path = os.path.join(current_dir, )
                file_name = file_name.replace('.slmod', '')

                # Lire le contenu de mod.txt
                mod_text_path = os.path.join(folder_path, "extracted_content", file_name, "mod", "mod.txt")
    
                with open(mod_text_path, 'r') as file:
                    path = file.read().strip()  # Stocke le contenu de mod.txt dans la variable `path`

                # Vérifier si le chemin est valide
                if not os.path.isdir(path):
                    raise ValueError(f"The path is not valid: {path}")

                # Lister les fichiers dans le dossier
                modfiles_path = os.path.join(folder_path, "extracted_content", file_name, "mod")
                modfiles = os.listdir(modfiles_path)

                # Identifier les fichiers
                for modname in modfiles:
                    if modname == 'path.txt':
                        path_file = os.path.join(folder_path, "extracted_content", file_name, "mod", modname)
                    else:
                        unknown_file = os.path.join(folder_path, "extracted_content", file_name, "mod", modname)

    
                # Chemin du fichier à envoyer
                file_to_send = os.path.join(folder_path, "extracted_content", file_name, "mod", unknown_file)
    
                # Copier le fichier vers la direction spécifiée
                shutil.copy(file_to_send, path)

                print(f"File '{file_to_send}' successfully applied. \n")

                folder_path = os.path.join(current_dir, "extracted_content")
                shutil.rmtree(folder_path)


                
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Chemin du dossier (à adapter selon votre situation)
        folder_path = os.path.join(current_dir, "Mods")
        
        # Lister les fichiers dans le dossier
        files = os.listdir(folder_path)

        # Boucle for avec filtrage des fichiers .slmod
        for file_name in files:
        # Vérifier si le fichier a l'extension .slmod
            if file_name == name_mod:
                # Utiliser le nom du fichier
                print(f".slmod file found : {file_name}")
                
                # Renommer l'archive avec l'extension zip temporairement
                zip_archive = file_name.replace('.slmod', '.zip')
                file_path = os.path.join(folder_path, file_name)
                zip_path = os.path.join(folder_path, zip_archive)
                os.rename(file_path, zip_path)
    
                # Extraire l'archive
                with zipfile.ZipFile(zip_path, 'r') as archive:
                    archive.extractall("extracted_content")
    
                # Renommer l'archive avec l'extension personnalisée
                os.rename(zip_path, file_path)
                
                folder_path = os.path.join(current_dir, )
                file_name = file_name.replace('.slmod', '')

                # Lire le contenu de mod.txt
                mod_text_path = os.path.join(folder_path, "extracted_content", file_name, "mod", "mod.txt")
    
                with open(mod_text_path, 'r') as file:
                    path = file.read().strip()  # Stocke le contenu de mod.txt dans la variable `path`

                # Vérifier si le chemin est valide
                if not os.path.isdir(path):
                    raise ValueError(f"The path is not valid: {path}")

                # Lister les fichiers dans le dossier
                modfiles_path = os.path.join(folder_path, "extracted_content", file_name, "mod")
                modfiles = os.listdir(modfiles_path)

                # Identifier les fichiers
                for modname in modfiles:
                    if modname == 'path.txt':
                        path_file = os.path.join(folder_path, "extracted_content", file_name, "mod", modname)
                    else:
                        unknown_file = os.path.join(folder_path, "extracted_content", file_name, "mod", modname)

    
                # Chemin du fichier à envoyer
                file_to_send = os.path.join(folder_path, "extracted_content", file_name, "mod", unknown_file)
    
                # Copier le fichier vers la direction spécifiée
                shutil.copy(file_to_send, path)
    
                print(f"File '{file_to_send}' successfully applied. \n")

                folder_path = os.path.join(current_dir, "extracted_content")
                shutil.rmtree(folder_path)


def removmods():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Chemin du dossier (à adapter selon votre situation)
    folder_path = os.path.join(current_dir, "Mods")
    
    # Lister les fichiers dans le dossier
    files = os.listdir(folder_path)

    # Boucle for avec filtrage des fichiers .slmod
    for file_name in files:
    # Vérifier si le fichier a l'extension .slmod
        if file_name.endswith('.slmod'):
            # Utiliser le nom du fichier
            print(f".slmod file found : {file_name}")
            
            # Renommer l'archive avec l'extension zip temporairement
            zip_archive = file_name.replace('.slmod', '.zip')
            file_path = os.path.join(folder_path, file_name)
            zip_path = os.path.join(folder_path, zip_archive)
            os.rename(file_path, zip_path)

            # Extraire l'archive
            with zipfile.ZipFile(zip_path, 'r') as archive:
                archive.extractall("extracted_content")

            # Renommer l'archive avec l'extension personnalisée
            os.rename(zip_path, file_path)
            
            folder_path = os.path.join(current_dir, )
            file_name = file_name.replace('.slmod', '')

            # Lire le contenu de mod.txt
            mod_text_path = os.path.join(folder_path, "extracted_content", file_name, "original", "original.txt")

            with open(mod_text_path, 'r') as file:
                path = file.read().strip()  # Stocke le contenu de mod.txt dans la variable `path`

            # Vérifier si le chemin est valide
            if not os.path.isdir(path):
                raise ValueError(f"The path is not valid: {path}")

            # Lister les fichiers dans le dossier
            modfiles_path = os.path.join(folder_path, "extracted_content", file_name, "original")
            modfiles = os.listdir(modfiles_path)

            # Identifier les fichiers
            for modname in modfiles:
                if modname == 'path.txt':
                    path_file = os.path.join(folder_path, "extracted_content", file_name, "original", modname)
                else:
                    unknown_file = os.path.join(folder_path, "extracted_content", file_name, "original", modname)


            # Chemin du fichier à envoyer
            file_to_send = os.path.join(folder_path, "extracted_content", file_name, "original", unknown_file)

            # Copier le fichier vers la direction spécifiée
            shutil.copy(file_to_send, path)

            folder_path = os.path.join(current_dir, "extracted_content")

            print(f"File '{file_to_send}' successfully replaced with original file. \n")
            shutil.rmtree(folder_path)
    

def checkmods(name):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Spécifier le dossier cible (situé dans le même dossier que le script)
    name = name + ".slmod"
    target_folder = os.path.join(current_dir, "Mods", name)

    # Vérifier si le dossier existe
    if os.path.isfile(target_folder):
        loadmods(name)
    else:
        print(f"The mod folder {target_folder} doesn't exist. \n")
        
print("\033[38;2;255;220;23m░██████╗██╗░░░░░  ███╗░░░███╗░█████╗░██████╗░  ██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░\n██╔════╝██║░░░░░  ████╗░████║██╔══██╗██╔══██╗  ██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗\n╚█████╗░██║░░░░░  ██╔████╔██║██║░░██║██║░░██║  ██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝\n░╚═══██╗██║░░░░░  ██║╚██╔╝██║██║░░██║██║░░██║  ██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗\n██████╔╝███████╗  ██║░╚═╝░██║╚█████╔╝██████╔╝  ███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║\n╚═════╝░╚══════╝  ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░  ╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝\033[0m")
a = 2

while a != 1:
    answer = input("Do you want to :\n     - Load all \033[38;2;255;220;23m.slmod\033[0m files located in the Mods folder (y)\n     - Remove all mods located in the Mods folder from the game (n)\n     - Load a specific \033[38;2;255;220;23m.slmod\033[0m file located in Mods folder (input file name)\n   Close this window to exit mod loader. 👈(ﾟヮﾟ👈) \n \n")
    if answer == "y":
        loadmods("*5ç$")
    elif answer == "n":
        removmods()
    else:
        checkmods(answer)
