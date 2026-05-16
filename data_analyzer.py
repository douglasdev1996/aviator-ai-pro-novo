"""
🚀 AVIATOR AI - Data Analyzer
Análise de dados da plataforma com IA integrada
Aprendizado 24/7 com Neuroplasticidade
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from collections import defaultdict
import json

class DataAnalyzer:
    """Analisador de dados com IA integrada"""
    
    def __init__(self):
        self.dados_velas = []
        self.padroes_horarios = defaultdict(list)
        self.padroes_multiplicadores = defaultdict(list)
        self.padroes_sinais = defaultdict(list)
        self.historico_acertos = []
        self.historico_erros = []
        self.neuroplasticity_score = 0.5
        self.acuracidade = 0.0
        self.rodadas_analisadas = 0
        
    def adicionar_vela(self, multiplicador, hora, sinal=None):
        """Adiciona uma vela aos dados"""
        self.dados_velas.append({
            "multiplicador": multiplicador,
            "hora": hora,
            "sinal": sinal,
            "timestamp": datetime.now()
        })
        
        # Análise de padrão horário
        hora_key = hora.split(":")[0]  # Hora (00-23)
        self.padroes_horarios[hora_key].append(multiplicador)
        
        # Análise de padrão de multiplicador
        if multiplicador >= 10:
            self.padroes_multiplicadores["rosa"].append(multiplicador)
        elif multiplicador >= 5:
            self.padroes_multiplicadores["boa"].append(multiplicador)
        elif multiplicador >= 3:
            self.padroes_multiplicadores["neutra"].append(multiplicador)
        else:
            self.padroes_multiplicadores["baixa"].append(multiplicador)
    
    def analisar_padroes_horarios(self):
        """Analisa padrões por horário"""
        padroes = {}
        for hora, mults in self.padroes_horarios.items():
            if mults:
                padroes[hora] = {
                    "media": np.mean(mults),
                    "max": np.max(mults),
                    "min": np.min(mults),
                    "desvio": np.std(mults),
                    "total": len(mults)
                }
        return padroes
    
    def analisar_padroes_multiplicadores(self):
        """Analisa distribuição de multiplicadores"""
        total = sum(len(v) for v in self.padroes_multiplicadores.values())
        if total == 0:
            return {}
        
        return {
            "rosa": len(self.padroes_multiplicadores["rosa"]) / total * 100,
            "boa": len(self.padroes_multiplicadores["boa"]) / total * 100,
            "neutra": len(self.padroes_multiplicadores["neutra"]) / total * 100,
            "baixa": len(self.padroes_multiplicadores["baixa"]) / total * 100,
        }
    
    def prever_melhor_entrada(self, ultimas_velas=5):
        """Prevê o melhor momento para entrar"""
        if len(self.dados_velas) < ultimas_velas:
            return "AGUARDANDO_DADOS", 0.5
        
        ultimas = [v["multiplicador"] for v in self.dados_velas[-ultimas_velas:]]
        media = np.mean(ultimas)
        tendencia = np.polyfit(range(len(ultimas)), ultimas, 1)[0]
        
        # Calcula confiança
        confianca = min(0.99, 0.5 + (media / 10) * 0.3 + (tendencia / 5) * 0.2)
        
        if media >= 5.0 and tendencia > 0:
            return "EXCELENTE_ENTRADA", confianca
        elif media >= 4.0:
            return "BOA_ENTRADA", confianca * 0.9
        elif media >= 2.0:
            return "ENTRADA_NEUTRA", confianca * 0.7
        else:
            return "NAO_ENTRAR", confianca * 0.6
    
    def registrar_acerto(self):
        """Registra um acerto"""
        self.historico_acertos.append(datetime.now())
        self.neuroplasticity_score = min(0.99, self.neuroplasticity_score + 0.02)
        self.atualizar_acuracidade()
    
    def registrar_erro(self):
        """Registra um erro"""
        self.historico_erros.append(datetime.now())
        self.neuroplasticity_score = max(0.3, self.neuroplasticity_score - 0.01)
        self.atualizar_acuracidade()
    
    def atualizar_acuracidade(self):
        """Atualiza a acuracidade"""
        total = len(self.historico_acertos) + len(self.historico_erros)
        if total > 0:
            self.acuracidade = len(self.historico_acertos) / total * 100
    
    def obter_estatisticas(self):
        """Retorna estatísticas gerais"""
        return {
            "rodadas_analisadas": len(self.dados_velas),
            "acertos": len(self.historico_acertos),
            "erros": len(self.historico_erros),
            "acuracidade": round(self.acuracidade, 2),
            "neuroplasticity_score": round(self.neuroplasticity_score * 100, 2),
            "padroes_horarios": self.analisar_padroes_horarios(),
            "distribuicao_multiplicadores": self.analisar_padroes_multiplicadores()
        }
    
    def exportar_dados(self):
        """Exporta dados em JSON"""
        return {
            "dados_velas": self.dados_velas,
            "estatisticas": self.obter_estatisticas(),
            "ultima_atualizacao": datetime.now().isoformat()
        }
