class Documento:
    def imprimir(self):
        print("contenido")

class DocumentoFirma(Documento):
    def imprimir(self):
        super().imprimir()
        print("firma")