import shutil
import os


def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_code_file(event):
    if extension_type(event) in ('PAK'):
        return True
    return False


def make_folder(foldername):
    os.chdir('C:\\PDV\\CATRACA')
    if os.path.exists(foldername) == True:
        print('Pasta já existe, não será criada')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.copy(event.src_path, path_to_new_folder)
        print('Copiando arquivos')
    except:
        print('Arquivo já existe na pasta')
        pass
