import ipywidgets as widgets
from IPython.display import display, HTML
from legal_analysis_engine import LegalAnalysisEngine

class LegalAssistantApp:
    def __init__(self):
        self.engine = LegalAnalysisEngine()
        self.setup_ui()

    def setup_ui(self):
        self.text_input = widgets.Textarea(
            value="",
            placeholder="Digite o texto do processo ou documento para análise...",
            description="Texto:",
            layout=widgets.Layout(width='100%', height='200px')
        )

        self.document_type = widgets.Dropdown(
            options=['Análise Jurídica', 'Parecer Jurídico', 'Minuta de Voto', 'Petição Inicial', 'Contestação'],
            value='Análise Jurídica',
            description='Tipo de Documento:',
            layout=widgets.Layout(width='50%')
        )

        self.analyze_button = widgets.Button(
            description="Analisar",
            button_style='primary',
            layout=widgets.Layout(width='200px')
        )

        self.output_area = widgets.HTML(
            value="<p>Resultado da análise aparecerá aqui...</p>",
            layout=widgets.Layout(width='100%', height='400px', border='1px solid #ccc', padding='10px')
        )

        self.analyze_button.on_click(self.on_analyze_click)

    def on_analyze_click(self, button):
        input_text = self.text_input.value
        doc_type = self.document_type.value

        if not input_text.strip():
            self.output_area.value = "<p style='color: red;'>Por favor, insira um texto para análise.</p>"
            return

        try:
            result = self.engine.process_request(input_text, doc_type)
            formatted_result = result.replace('\n', '<br>')
            self.output_area.value = f"<div style='font-family: monospace; white-space: pre-wrap;'>{formatted_result}</div>"
        except Exception as e:
            self.output_area.value = f"<p style='color: red;'>Erro durante a análise: {str(e)}</p>"

    def display(self):
        display(HTML("<h2>🏛️ Assistente de IA Jurídico</h2>"))
        display(HTML("<p>Este assistente pode analisar documentos jurídicos e gerar peças com base na legislação brasileira e jurisprudências dos tribunais superiores.</p>"))
        
        display(self.text_input)
        display(self.document_type)
        display(self.analyze_button)
        display(HTML("<h3>Resultado:</h3>"))
        display(self.output_area)

# Função para executar no Colab
def run_legal_assistant():
    app = LegalAssistantApp()
    app.display()

if __name__ == '__main__':
    # Para execução direta (não no Colab)
    print("Para usar no Google Colab, execute: run_legal_assistant()")
    
    # Teste básico sem interface
    engine = LegalAnalysisEngine()
    sample_text = "Preciso de uma análise sobre responsabilidade civil no Código Civil."
    result = engine.process_request(sample_text)
    print("\n--- Teste do Motor de Análise ---")
    print(result)

