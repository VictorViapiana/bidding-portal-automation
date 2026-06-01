import os
from datetime import datetime

# Termos de Busca e Filtros de Análise
STATUS_FILTROS = ["Recebendo Propostas", "Em Andamento"]

PALAVRAS_NEGATIVAS = [
    "obra", "engenharia civil", "pavimentação", "combustível", 
    "vigilância", "limpeza", "mobiliário", "construção", "impressão gráfica", 
    "videomonitoramento", "locação de equipamentos", "equipamentos", 
    "fonrnecimento de equipamentos", "antivírus", "equipamento"
]

PALAVRAS_POSITIVAS = [
    "whatsapp", "api", "chatbot", "omnichannel", "atendimento digital", 
    "integração", "middleware", "crm", "erp", "automação", "mensageria",
    "inteligência artificial", "ia", "SaaS", "cloud", "help desk", "integrações",
    "atendimento multicanal", "plataforma web", "web", "painel administrative",
    "notificações", "comunicação digital", "canal digital", "canais digitais", 
    "atendimento automatizado", "webservice", "hub de integração", "hub",
    "microserviços", "integração rest", "openai", "meta", "microsoft",
    "azure", "aws", "e-commerce"
]

def obter_caminho_salvamento():
    """Gerencia a criação da pasta e define o nome sequencial do arquivo Excel"""
    caminho_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    nome_pasta = os.path.join(caminho_desktop, "licitacoes_2026")
    
    if not os.path.exists(nome_pasta):
        os.makedirs(nome_pasta)
        print(f"📁 Pasta 'licitacoes_2026' criada com sucesso na Área de Trabalho!", flush=True)

    else: 
        print(f"Pasta {nome_pasta} já existente na sua área de trabalho!")
        
    data_atual = datetime.now().strftime("%Y-%m-%d")
    nome_base = f"Oportunidades_Galactix_{data_atual}"
    nome_planilha = os.path.join(nome_pasta, f"{nome_base}.xlsx")
    
    contador = 1
    while os.path.exists(nome_planilha):
        nome_planilha = os.path.join(nome_pasta, f"{nome_base}({contador}).xlsx")
        contador += 1
        
    return nome_planilha