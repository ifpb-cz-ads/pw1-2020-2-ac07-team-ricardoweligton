class Televisao:
    def __init__(self, canal_min=2, canal_max=14):
        self.canal = 2
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.ligada = False

    def muda_canal_para_baixo(self):
        if self.canal - 1 < self.canal_min:
            self.canal = self.canal_max
        else:
            self.canal -= 1
    
    def muda_canal_para_cima(self):
        if self.canal + 1 > self.canal_max:
            self.canal = self.canal_min
        else:
            self.canal += 1
