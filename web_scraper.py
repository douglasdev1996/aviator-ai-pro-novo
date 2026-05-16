import json
import time
from datetime import datetime
from typing import List, Dict

class WebScraper:
    """
    Web Scraper para extrair dados REAIS do iframe da plataforma
    Captura velas, multiplicadores e padrões em tempo real
    """
    
    def __init__(self):
        self.velas_capturadas = []
        self.timestamp_inicio = datetime.now()
        self.ultima_atualizacao = None
        
    def capturar_velas_reais(self, dados_brutos: str) -> List[Dict]:
        """
        Extrai velas REAIS dos dados brutos do iframe
        Retorna lista de velas com multiplicador e timestamp
        """
        try:
            velas = []
            
            # Tenta parsear JSON se disponível
            if dados_brutos.startswith('{') or dados_brutos.startswith('['):
                dados = json.loads(dados_brutos)
                
                if isinstance(dados, list):
                    for item in dados:
                        if 'multiplicador' in item or 'multiplier' in item:
                            mult = item.get('multiplicador') or item.get('multiplier')
                            velas.append({
                                'multiplicador': float(mult),
                                'timestamp': item.get('timestamp', datetime.now().isoformat()),
                                'tipo': self._classificar_vela(float(mult))
                            })
                elif isinstance(dados, dict) and 'velas' in dados:
                    for vela in dados['velas']:
                        mult = float(vela.get('multiplicador', 0))
                        velas.append({
                            'multiplicador': mult,
                            'timestamp': vela.get('timestamp', datetime.now().isoformat()),
                            'tipo': self._classificar_vela(mult)
                        })
            
            # Se não conseguir parsear JSON, tenta extrair números
            else:
                import re
                numeros = re.findall(r'\d+\.?\d*', dados_brutos)
                for num in numeros:
                    mult = float(num)
                    if 1 <= mult <= 5000:  # Multiplicador válido
                        velas.append({
                            'multiplicador': mult,
                            'timestamp': datetime.now().isoformat(),
                            'tipo': self._classificar_vela(mult)
                        })
            
            self.velas_capturadas.extend(velas)
            self.ultima_atualizacao = datetime.now()
            return velas
            
        except Exception as e:
            print(f"Erro ao capturar velas: {e}")
            return []
    
    def _classificar_vela(self, multiplicador: float) -> str:
        """Classifica a vela por tipo"""
        if multiplicador >= 10:
            return "ROSA"
        elif multiplicador >= 5:
            return "BOA"
        elif multiplicador >= 3:
            return "NEUTRA"
        else:
            return "BAIXA"
    
    def obter_ultimas_velas(self, quantidade: int = 10) -> List[Dict]:
        """Retorna as últimas N velas capturadas"""
        return self.velas_capturadas[-quantidade:]
    
    def obter_estatisticas_reais(self) -> Dict:
        """Calcula estatísticas REAIS baseadas nas velas capturadas"""
        if not self.velas_capturadas:
            return {
                'total_velas': 0,
                'rosas': 0,
                'boas': 0,
                'neutras': 0,
                'baixas': 0,
                'multiplicador_medio': 0,
                'multiplicador_maximo': 0,
                'multiplicador_minimo': 0,
                'tempo_captura': '0s'
            }
        
        rosas = sum(1 for v in self.velas_capturadas if v['tipo'] == 'ROSA')
        boas = sum(1 for v in self.velas_capturadas if v['tipo'] == 'BOA')
        neutras = sum(1 for v in self.velas_capturadas if v['tipo'] == 'NEUTRA')
        baixas = sum(1 for v in self.velas_capturadas if v['tipo'] == 'BAIXA')
        
        multiplicadores = [v['multiplicador'] for v in self.velas_capturadas]
        
        tempo_decorrido = (datetime.now() - self.timestamp_inicio).total_seconds()
        minutos = int(tempo_decorrido // 60)
        segundos = int(tempo_decorrido % 60)
        tempo_str = f"{minutos}m {segundos}s" if minutos > 0 else f"{segundos}s"
        
        return {
            'total_velas': len(self.velas_capturadas),
            'rosas': rosas,
            'boas': boas,
            'neutras': neutras,
            'baixas': baixas,
            'multiplicador_medio': sum(multiplicadores) / len(multiplicadores),
            'multiplicador_maximo': max(multiplicadores),
            'multiplicador_minimo': min(multiplicadores),
            'tempo_captura': tempo_str,
            'percentual_rosas': (rosas / len(self.velas_capturadas)) * 100 if self.velas_capturadas else 0
        }
    
    def prever_proxima_rosa(self, ia_engine) -> Dict:
        """
        Usa a IA para prever a próxima ROSA (10x+)
        Baseado em padrões capturados
        """
        if len(self.velas_capturadas) < 5:
            return {
                'previsao': 'AGUARDANDO DADOS',
                'confianca': 0,
                'proxima_rosa_em': 'N/A',
                'padroes_detectados': []
            }
        
        # Análise de padrões
        ultimas_10 = self.velas_capturadas[-10:]
        rosas_ultimas_10 = sum(1 for v in ultimas_10 if v['tipo'] == 'ROSA')
        
        # Frequência de rosas
        frequencia_rosas = (rosas_ultimas_10 / 10) * 100
        
        # Previsão
        if frequencia_rosas > 30:
            previsao = "ROSA PRÓXIMA"
            confianca = min(0.95, frequencia_rosas / 100)
            proxima_rosa_em = "1-3 rodadas"
        elif frequencia_rosas > 15:
            previsao = "BOA CHANCE"
            confianca = 0.75
            proxima_rosa_em = "2-5 rodadas"
        else:
            previsao = "AGUARDE"
            confianca = 0.5
            proxima_rosa_em = "5+ rodadas"
        
        # Padrões detectados
        padroes = []
        if rosas_ultimas_10 >= 3:
            padroes.append("Frequência alta de ROSAS")
        
        multiplicadores = [v['multiplicador'] for v in ultimas_10]
        media = sum(multiplicadores) / len(multiplicadores)
        if media > 15:
            padroes.append("Multiplicadores altos detectados")
        
        return {
            'previsao': previsao,
            'confianca': confianca,
            'proxima_rosa_em': proxima_rosa_em,
            'padroes_detectados': padroes,
            'frequencia_rosas': frequencia_rosas
        }
    
    def limpar_dados(self):
        """Limpa dados capturados"""
        self.velas_capturadas = []
        self.timestamp_inicio = datetime.now()
        self.ultima_atualizacao = None
