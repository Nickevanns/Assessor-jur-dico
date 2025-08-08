import unittest
import os
import sqlite3
from knowledge_base_setup import setup_database, query_legal_codes, query_jurisprudences
from legal_analysis_engine import LegalAnalysisEngine

class TestLegalAssistant(unittest.TestCase):
    def setUp(self):
        self.db_path = "test_legal_knowledge_base.db"
        # Configurar um banco de dados de teste limpo para cada teste
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        
        # Chamar setup_database para criar o banco de dados de teste
        # É importante que setup_database use o caminho correto do DB para testes
        # Para isso, vamos passar o caminho do DB para as funções de query e setup
        # ou garantir que elas usem um caminho configurável.
        # Por enquanto, vamos garantir que as funções de query usem o DB de teste.
        
        # Criar o banco de dados de teste e suas tabelas
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS legal_codes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code_name TEXT NOT NULL,
                article_number TEXT,
                content TEXT NOT NULL,
                chapter TEXT,
                section TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jurisprudences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                court TEXT NOT NULL,
                case_number TEXT,
                summary TEXT NOT NULL,
                full_text TEXT,
                date TEXT
            )
        """)
        conn.commit()

        # Inserir dados de teste
        cursor.execute("""
            INSERT INTO legal_codes (code_name, article_number, content, chapter, section)
            VALUES (?, ?, ?, ?, ?)
        """, (
            'Código Civil',
            'Art. 186',
            'Aquele que, por ação ou omissão voluntária, negligência ou imprudência, violar direito e causar dano a outrem, ainda que exclusivamente moral, comete ato ilícito.',
            'Do Ato Ilícito',
            'Disposições Gerais'
        ))
        cursor.execute("""
            INSERT INTO jurisprudences (court, case_number, summary, full_text, date)
            VALUES (?, ?, ?, ?, ?)
        """, (
            'STJ',
            'REsp 123456',
            'Resumo da decisão do STJ sobre responsabilidade civil.',
            'Texto completo da decisão do STJ...', 
            '2023-01-15'
        ))
        conn.commit()
        conn.close()
        
        self.engine = LegalAnalysisEngine()
        # Ajustar o caminho do DB para as funções de query para o DB de teste
        # Isso é necessário porque as funções query_legal_codes e query_jurisprudences
        # usam um caminho fixo ('legal_knowledge_base.db').
        # Uma solução mais robusta seria passar o caminho do DB como argumento para essas funções.
        # Para este teste, vamos sobrescrever temporariamente o método connect do sqlite3
        # para que ele sempre se conecte ao DB de teste.
        self._original_sqlite_connect = sqlite3.connect
        sqlite3.connect = lambda db_name: self._original_sqlite_connect(self.db_path)

    def tearDown(self):
        # Restaurar o método original de conexão do sqlite3
        sqlite3.connect = self._original_sqlite_connect
        # Limpar o banco de dados de teste após cada teste
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_query_legal_codes(self):
        results = query_legal_codes(code_name="Código Civil", article_number="Art. 186")
        self.assertIsNotNone(results)
        self.assertEqual(len(results), 1)
        self.assertIn("ato ilícito", results[0][3])

    def test_query_jurisprudences(self):
        results = query_jurisprudences(court="STJ", case_number="REsp 123456")
        self.assertIsNotNone(results)
        self.assertEqual(len(results), 1)
        self.assertIn("responsabilidade civil", results[0][3])

    def test_analyze_text(self):
        text = "Este é um texto de teste mencionando o Art. 186 do Código Civil."
        analysis = self.engine.analyze_text(text)
        self.assertIn("Possível referência a artigo de lei.", analysis["found_references"])
        self.assertIn("Possível referência a lei.", analysis["found_references"])

    def test_generate_legal_document(self):
        analysis_results = {"analysis_summary": "Análise de teste.", "found_references": []}
        relevant_codes = query_legal_codes(code_name="Código Civil")
        relevant_jurisprudences = query_jurisprudences(court="STJ")
        
        document = self.engine.generate_legal_document(
            "Parecer Jurídico", analysis_results, relevant_codes, relevant_jurisprudences
        )
        self.assertIn("Tipo de Documento: Parecer Jurídico", document)
        self.assertIn("Legislação Aplicável:", document)
        self.assertIn("Jurisprudência Relevante:", document)

    def test_process_request_integration(self):
        input_text = "Preciso de uma análise sobre um caso de responsabilidade civil, considerando o Código Civil e jurisprudência do STJ."
        output_document = self.engine.process_request(input_text, document_type="Parecer Jurídico")
        
        self.assertIn("Tipo de Documento: Parecer Jurídico", output_document)
        self.assertIn("Legislação Aplicável:", output_document)
        self.assertIn("Jurisprudência Relevante:", output_document)
        self.assertIn("Código Civil", output_document)
        self.assertIn("STJ", output_document)

if __name__ == '__main__':
    unittest.main(argv=["first-arg-is-ignored"], exit=False)


