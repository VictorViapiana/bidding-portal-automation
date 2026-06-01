import sys
import io

# Força a saída do sistema a usar UTF-8, independente do terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Importa as engrenagens modulares do nosso pacote src
from src.bot import executar_raspagem, salvar_e_formatar_planilha

if __name__ == "__main__":
    print("🚀 Iniciando a operação do Robô de Licitações Galactix...", flush=True)
    
    # 1. Executa a varredura web e coleta os dados
    dados_propostas, dados_andamento = executar_raspagem()
    
    # 2. Compila e estiliza o relatório Excel diretamente na Área de Trabalho
    salvar_e_formatar_planilha(dados_propostas, dados_andamento)
    
    print("\n🏁 Processo finalizado com sucesso!", flush=True)