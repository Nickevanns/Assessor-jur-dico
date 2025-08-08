import sqlite3

def setup_database():
    conn = sqlite3.connect('legal_knowledge_base.db')
    cursor = conn.cursor()

    # Tabela para Códigos Legais
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS legal_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code_name TEXT NOT NULL,
            article_number TEXT,
            content TEXT NOT NULL,
            chapter TEXT,
            section TEXT
        )
    ''')

    # Tabela para Jurisprudências
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jurisprudences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            court TEXT NOT NULL,
            case_number TEXT,
            summary TEXT NOT NULL,
            full_text TEXT,
            date TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_sample_data():
    conn = sqlite3.connect('legal_knowledge_base.db')
    cursor = conn.cursor()

    # Inserir dados de exemplo para Códigos Legais
    cursor.execute("""
        INSERT INTO legal_codes (code_name, article_number, content, chapter, section)
        VALUES (?, ?, ?, ?, ?)
    """, ('Código Civil', 'Art. 186', 'Aquele que, por ação ou omissão voluntária, negligência ou imprudência, violar direito e causar dano a outrem, ainda que exclusivamente moral, comete ato ilícito.', 'Do Ato Ilícito', 'Disposições Gerais'))

    cursor.execute("""
        INSERT INTO legal_codes (code_name, article_number, content, chapter, section)
        VALUES (?, ?, ?, ?, ?)
    """, ('Código de Defesa do Consumidor', 'Art. 6', 'São direitos básicos do consumidor: I - a proteção da vida, saúde e segurança contra os riscos provocados por práticas no fornecimento de produtos e serviços considerados perigosos ou nocivos;', 'Dos Direitos Básicos do Consumidor', 'Disposições Gerais'))

    # Inserir dados de exemplo para Jurisprudências
    cursor.execute("""
        INSERT INTO jurisprudences (court, case_number, summary, full_text, date)
        VALUES (?, ?, ?, ?, ?)
    """, ('STJ', 'REsp 123456', 'Resumo da decisão do STJ sobre responsabilidade civil.', 'Texto completo da decisão do STJ...', '2023-01-15'))

    cursor.execute("""
        INSERT INTO jurisprudences (court, case_number, summary, full_text, date)
        VALUES (?, ?, ?, ?, ?)
    """, ('TST', 'RR 789012', 'Resumo da decisão do TST sobre vínculo empregatício.', 'Texto completo da decisão do TST...', '2022-11-20'))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
    insert_sample_data()
    print('Base de conhecimento jurídica configurada e dados de exemplo inseridos.')





def query_legal_codes(code_name=None, article_number=None, keyword=None):
    conn = sqlite3.connect("legal_knowledge_base.db")
    cursor = conn.cursor()
    query = "SELECT * FROM legal_codes WHERE 1=1"
    params = []

    if code_name:
        query += " AND code_name LIKE ?"
        params.append(f"%{code_name}%")
    if article_number:
        query += " AND article_number LIKE ?"
        params.append(f"%{article_number}%")
    if keyword:
        query += " AND content LIKE ?"
        params.append(f"%{keyword}%")

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def query_jurisprudences(court=None, case_number=None, keyword=None):
    conn = sqlite3.connect("legal_knowledge_base.db")
    cursor = conn.cursor()
    query = "SELECT * FROM jurisprudences WHERE 1=1"
    params = []

    if court:
        query += " AND court LIKE ?"
        params.append(f"%{court}%")
    if case_number:
        query += " AND case_number LIKE ?"
        params.append(f"%{case_number}%")
    if keyword:
        query += " AND (summary LIKE ? OR full_text LIKE ?)"
        params.append(f"%{keyword}%")
        params.append(f"%{keyword}%")

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results



