#encoding: iso-8859-1



import psutil as ps

print('Lista de processos em execução:')
for proc in ps.process_iter():
    info = proc.as_dict(attrs=['pid', 'name'])
    print('Processo: {} (PID: {})'.format(info['pid'], info['name']))