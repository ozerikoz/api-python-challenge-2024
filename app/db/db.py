import oracledb
from flask import current_app, g

def get_db():
    # se a conexão com o banco de dados não existir, cria uma nova conexão.
    if 'db' not in g:
        try:
            g.db = oracledb.connect(
                user=current_app.config['ORACLE_DB_USER'],
                password=current_app.config['ORACLE_DB_PASSWORD'],
                dsn=f"{current_app.config['ORACLE_DB_HOST']}:{current_app.config['ORACLE_DB_PORT']}/{current_app.config['ORACLE_DB_SID']}"
            )
            print("Conexão com o banco de dados foi estabelecida com sucesso!")
        except oracledb.DatabaseError as e:
            print("Erro ao conectar ao banco de dados:", e)
            raise e

    return g.db

def init_db(app):
    # fecha a conexão automaticamente após o processamento de cada requisição.
    @app.teardown_appcontext
    def close_connection(exception):
        db = g.pop('db', None)
        if db is not None:
            db.close()
