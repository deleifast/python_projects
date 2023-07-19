import  sqlite3

def tabelas():
    conn = sqlite3.connect('lojas.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS impressora(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        loja TEXT(3) NOT NULL,
        sat TEXT(4) NOT NULL,
        modelo TEXT(40) NOT NULL,
        data_atual TEXT(20) NOT NULL)
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS ip(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        loja TEXT(3) NOT NULL,
        nome TEXT(40) NOT NULL,
        sat TEXT(4) NOT NULL,
        ip TEXT(20) NOT NULL,
        data_atual TEXT(20) NOT NULL)
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS cpu(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        loja TEXT(3) NOT NULL,
        sat TEXT(4) NOT NULL,
        modelo TEXT(60) NOT NULL,
        memoria TEXT(20) NOT NULL,
        hd_total TEXT(10) NOT NULL,
        hd_usado TEXT(10) NOT NULL,
        hd_livre TEXT(10) NOT NULL,
        data_atual TEXT(20) NOT NULL)
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS ver(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        loja TEXT(3) NOT NULL,
        sat TEXT(4) NOT NULL,
        arq TEXT(30) NOT NULL,
        data_gerada TEXT(20) NOT NULL)
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS ipdns(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        loja TEXT(3) NOT NULL,
        sat TEXT(4) NOT NULL,
        endereco TEXT(15) NOT NULL,
        vazio TEXT(5) NOT NULL,
        ip TEXT(15) NOT NULL)
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS chave(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        loja TEXT(3) NOT NULL,
        sat TEXT(4) NOT NULL,
        nome TEXT(10) NOT NULL,
        versao_w TEXT(3) NOT NULL,
        versao_1 TEXT(20) NOT NULL,
        prod_id TEXT(10) NOT NULL,
        prod_k TEXT(10) NOT NULL,
        pasta TEXT(10) NOT NULL,
        versao TEXT(5) NOT NULL,
        caixa TEXT(15) NOT NULL,
        data_modificado TEXT(20) NOT NULL,
        hora_modificado TEXT(20) NOT NULL)
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS satap(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        loja TEXT(3) NOT NULL,
        sat TEXT(4) NOT NULL,
        aparelho TEXT(10) NOT NULL,
        ultran TEXT(20) NOT NULL,
        ulcom TEXT(20) NOT NULL,
        serie TEXT(20) NOT NULL,
        basica TEXT(20) NOT NULL,
        cfeini TEXT(50) NOT NULL,
        cfefim TEXT(50) NOT NULL,
        certemi TEXT(20) NOT NULL,
        certven TEXT(20) NOT NULL,
        ip TEXT(20) NOT NULL,
        dns1 TEXT(20) NOT NULL,
        dns2 TEXT(20) NOT NULL,
        gw TEXT(20) NOT NULL,
        mascara TEXT(20) NOT NULL,
        estado TEXT(20) NOT NULL,
        data_atual TEXT(20) NOT NULL)
    ''')

    try:
        
        with open("relimp_lojas.txt", "r") as f:
            rows = f.readlines()
            for row in rows:
                fields = row.split(' ')
                c.execute(f'INSERT INTO impressora (loja, sat, modelo, data_atual)'\
                        f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}')")
    except:
        with open("errimp_lojas.txt", "w") as f:
            print("erro", file=f)
    conn.commit()

    #for row in c.execute('SELECT * FROM impressora'):
    #    print(row)

    try:	
        with open("relip_lojas.txt", "r") as f:
            rows = f.readlines()
            for row in rows:
                fields = row.split(' ')
                c.execute(f'INSERT INTO ip (loja, sat, nome, ip, data_atual)'\
                        f"VALUES ('{fields[0]}','{fields[1]}', '{fields[2]}', '{fields[3]}', '{fields[4]}')")
    except:
        with open("errip_lojas.txt", "w") as f:
            print("erro", file=f)

    conn.commit()

    #for row in c.execute('SELECT * FROM ip'):
    #    print(row)

    try:
        
        with open("relcpu_lojas.txt", "r") as f:
            rows = f.readlines()
            for row in rows:
                fields = row.split(',')
                c.execute(f'INSERT INTO cpu (loja, sat, modelo, memoria, hd_total, hd_usado, hd_livre, data_atual)'\
                        f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}','{fields[4]}','{fields[5]}','{fields[6]}','{fields[7]}')")
    except:
        with open("errcpu_lojas.txt", "w") as f:
            print("erro", file=f)

    conn.commit()

    #for row in c.execute('SELECT * FROM cpu'):
    #    print(row)

    try:
        
        with open("relverpdv_lojas.txt", "r") as f:
            rows = f.readlines()
            for row in rows:
                fields = row.split(',')
                c.execute(f'INSERT INTO ver (loja, sat, arq, data_gerada)'\
                        f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}')")
    except:
        with open("errpdv_lojas.txt", "w") as f:
            print("erro", file=f)

    conn.commit()

    #for row in c.execute('SELECT * FROM ver'):
    #    print(row)

    try:
        
        with open("reldns_lojas.txt", "r") as f:
            rows = f.readlines()
            for row in rows:
                fields = row.split(' ')
                c.execute(f'INSERT INTO ipdns (loja, sat, endereco, vazio, ip)'\
                        f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}','{fields[4]}')")
    except:
        with open("errdns_lojas.txt", "w") as f:
            print("erro", file=f)

    conn.commit()

    #for row in c.execute('SELECT * FROM ipdns'):
    #    print(row)

    try:
        
        with open("relkey_lojas.txt", "r") as f:
            rows = f.readlines()
            for row in rows:
                fields = row.split(' ')
                c.execute(f'INSERT INTO chave (loja, sat, nome, versao_w, versao_1, prod_id, prod_k, pasta, versao, caixa, data_modificado, hora_modificado)'\
                        f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}','{fields[4]}','{fields[5]}','{fields[6]}','{fields[7]}','{fields[8]}','{fields[9]}','{fields[10]}','{fields[11]}')")
    except:
        with open("errkey_lojas.txt", "w") as f:
            print("erro", file=f)

    conn.commit()

    for row in c.execute('SELECT * FROM chave'):
        print(row)

    try:
        
        with open("relsat_lojas.txt", "r") as f:
            rows = f.readlines()
            for row in rows:
                fields = row.split(',')
                c.execute(f'INSERT INTO satap (loja, sat, aparelho, ultran, ulcom, serie, basica, cfeini, cfefim, certemi, certven, ip, dns1, dns2, gw, mascara, estado, data_atual)'\
                        f"VALUES ('{fields[0]}', '{fields[1]}', '{fields[2]}', '{fields[3]}', '{fields[4]}', '{fields[5]}', '{fields[6]}', '{fields[7]}', '{fields[8]}', '{fields[9]}', '{fields[10]}', '{fields[11]}', '{fields[12]}', '{fields[13]}', '{fields[14]}', '{fields[15]}', '{fields[16]}', '{fields[17]}')")
    except:
        with open("errsat_lojas.txt", "w") as f:
            print("erro", file=f)

    conn.commit()

    #for row in c.execute('SELECT * FROM satap'):
    #    print(row)
    
    conn.close()
