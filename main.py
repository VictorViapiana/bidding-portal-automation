import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.bot import executar_raspagem, salvar_e_formatar_planilha

if __name__ == "__main__":
    print("🚀 Iniciando a operação do Robô de Licitações Galactix...", flush=True)
    
    dados_propostas, dados_andamento = executar_raspagem()
    
    salvar_e_formatar_planilha(dados_propostas, dados_andamento)
    
    print("\n🏁 Processo finalizado com sucesso!", flush=True)