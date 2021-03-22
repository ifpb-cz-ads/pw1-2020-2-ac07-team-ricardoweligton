class Televisao:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho
        self.canal = 2
        self.ligada = False
    
    def muda_canal_para_baixo(self):
        self.canal -= 1
    
    def muda_canal_para_cima(self):
        self.canal += 1

    def tv_info(self):
        print(f"Essa eh uma TV {self.marca} de {self.tamanho} polegadas")
