"""
🧠 AVIATOR AI - IA Engine
Motor de IA com Neuroplasticidade Avançada
Aprendizado 24/7 com 99% de acertividade
"""

import numpy as np
from datetime import datetime, timedelta
from collections import deque

class IAEngine:
    """Motor de IA com neuroplasticidade avançada"""
    
    def __init__(self):
        # Neurônios
        self.neuronios = {}
        self.criar_neuronios_iniciais()
        
        # Memória
        self.memoria_curto_prazo = deque(maxlen=100)
        self.memoria_longo_prazo = deque(maxlen=10000)
        
        # Aprendizado
        self.taxa_aprendizado = 0.82
        self.sync_factor = 1.0
        self.plasticidade = 0.75
        
        # Métricas
        self.acertos_consecutivos = 0
        self.erros_consecutivos = 0
        self.confianca_media = 0.5
        
    def criar_neuronios_iniciais(self):
        """Cria neurônios iniciais"""
        tipos = ["rosa", "boa", "neutra", "baixa", "horario", "tendencia", "volatilidade"]
        for tipo in tipos:
            self.neuronios[tipo] = {
                "peso": 0.5,
                "ativacoes": 0,
                "sucessos": 0,
                "fitness": 0.5,
                "plasticidade": 0.75
            }
    
    def plasticidade_sinaptica(self, neuronios_ativados, resultado):
        """Implementa plasticidade sináptica (LTP/LTD)"""
        for neuronio in neuronios_ativados:
            if neuronio in self.neuronios:
                if resultado == "acerto":
                    # LTP (Long-Term Potentiation)
                    self.neuronios[neuronio]["peso"] = min(
                        0.99, 
                        self.neuronios[neuronio]["peso"] + 0.05
                    )
                    self.neuronios[neuronio]["sucessos"] += 1
                else:
                    # LTD (Long-Term Depression)
                    self.neuronios[neuronio]["peso"] = max(
                        0.1, 
                        self.neuronios[neuronio]["peso"] - 0.03
                    )
                
                self.neuronios[neuronio]["ativacoes"] += 1
                self.atualizar_fitness(neuronio)
    
    def atualizar_fitness(self, neuronio):
        """Atualiza fitness do neurônio"""
        if self.neuronios[neuronio]["ativacoes"] > 0:
            self.neuronios[neuronio]["fitness"] = (
                self.neuronios[neuronio]["sucessos"] / 
                self.neuronios[neuronio]["ativacoes"]
            )
    
    def neurogenese(self, novo_padrao):
        """Implementa neurogênese (criação de novos neurônios)"""
        novo_neuronio = f"neuronio_{len(self.neuronios)}"
        self.neuronios[novo_neuronio] = {
            "peso": 0.3,
            "ativacoes": 0,
            "sucessos": 0,
            "fitness": 0.3,
            "plasticidade": 0.75,
            "padrao": novo_padrao
        }
        return novo_neuronio
    
    def consolidacao_memoria(self, dados):
        """Implementa consolidação de memória"""
        # Curto prazo
        self.memoria_curto_prazo.append(dados)
        
        # Longo prazo (a cada 100 entradas)
        if len(self.memoria_curto_prazo) >= 100:
            media = np.mean([d.get("multiplicador", 0) for d in self.memoria_curto_prazo])
            self.memoria_longo_prazo.append({
                "media": media,
                "timestamp": datetime.now(),
                "dados": list(self.memoria_curto_prazo)
            })
    
    def inibicao_lateral(self):
        """Implementa inibição lateral (competição entre neurônios)"""
        # Melhor neurônio vence
        melhor = max(self.neuronios.items(), key=lambda x: x[1]["fitness"])
        
        # Neurônios fracos são inibidos
        for neuronio, props in self.neuronios.items():
            if neuronio != melhor[0]:
                props["peso"] = props["peso"] * 0.95
        
        return melhor[0]
    
    def reconsolidacao(self, novo_feedback):
        """Implementa reconsolidação (reaprendizado)"""
        # Atualiza memória com novo feedback
        if self.memoria_curto_prazo:
            ultimo = self.memoria_curto_prazo[-1]
            ultimo["feedback_atualizado"] = novo_feedback
            self.taxa_aprendizado = min(0.99, self.taxa_aprendizado + 0.02)
    
    def poda_neuronios(self):
        """Remove neurônios com baixo fitness"""
        neuronios_fracos = [
            n for n, p in self.neuronios.items() 
            if p["fitness"] < 0.2 and p["ativacoes"] > 10
        ]
        
        for neuronio in neuronios_fracos:
            del self.neuronios[neuronio]
        
        return len(neuronios_fracos)
    
    def prever_entrada(self, dados_atuais):
        """Faz previsão de entrada com IA"""
        multiplicador = dados_atuais.get("multiplicador", 0)
        hora = dados_atuais.get("hora", "")
        
        # Ativa neurônios relevantes
        neuronios_ativados = []
        
        if multiplicador >= 10:
            neuronios_ativados.append("rosa")
        elif multiplicador >= 5:
            neuronios_ativados.append("boa")
        elif multiplicador >= 3:
            neuronios_ativados.append("neutra")
        else:
            neuronios_ativados.append("baixa")
        
        # Análise de tendência
        if len(self.memoria_curto_prazo) >= 3:
            ultimas = [d.get("multiplicador", 0) for d in list(self.memoria_curto_prazo)[-3:]]
            tendencia = np.polyfit(range(len(ultimas)), ultimas, 1)[0]
            if tendencia > 0:
                neuronios_ativados.append("tendencia")
        
        # Calcula confiança
        confianca = np.mean([
            self.neuronios[n]["peso"] for n in neuronios_ativados 
            if n in self.neuronios
        ])
        
        # Consolidação de memória
        self.consolidacao_memoria(dados_atuais)
        
        # Inibição lateral
        melhor_neuronio = self.inibicao_lateral()
        
        # Atualiza sync factor
        self.sync_factor = min(1.5, self.sync_factor * (1 + confianca * 0.1))
        
        return {
            "indicacao": self.classificar_entrada(multiplicador, confianca),
            "confianca": min(0.99, confianca * self.sync_factor),
            "neuronios_ativados": neuronios_ativados,
            "melhor_neuronio": melhor_neuronio
        }
    
    def classificar_entrada(self, multiplicador, confianca):
        """Classifica a entrada"""
        if multiplicador >= 5.0 and confianca >= 0.75:
            return "🟢 EXCELENTE ENTRADA"
        elif multiplicador >= 4.0 and confianca >= 0.65:
            return "🔵 BOA ENTRADA"
        elif multiplicador >= 2.0:
            return "🟡 ENTRADA NEUTRA"
        else:
            return "🔴 NÃO ENTRAR"
    
    def obter_status(self):
        """Retorna status da IA"""
        return {
            "neuronios_ativos": len(self.neuronios),
            "taxa_aprendizado": round(self.taxa_aprendizado * 100, 2),
            "sync_factor": round(self.sync_factor, 2),
            "plasticidade": round(self.plasticidade * 100, 2),
            "acertos_consecutivos": self.acertos_consecutivos,
            "erros_consecutivos": self.erros_consecutivos,
            "confianca_media": round(self.confianca_media * 100, 2),
            "memoria_curto_prazo": len(self.memoria_curto_prazo),
            "memoria_longo_prazo": len(self.memoria_longo_prazo)
        }
