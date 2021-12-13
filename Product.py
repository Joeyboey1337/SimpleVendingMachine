class Product:
    def __init__(self,name,price,qtc):
        self.name = name
        self.price = price
        self.qtc = qtc
    
    def info(self):
        format_drinks = f"{self.name:<12}"
        format_price  = f"RP.{self.price :,}"
        format_qtc    = f"{self.qtc:>3} bottles available"
        return "."+format_drinks+"\t : @"+format_price+" => "+format_qtc