# https://programmerclick.com/article/8641129051/#python-db-api
# hay una librería llamada factory que te rellena los datos 

from datetime import date
import click
from base import Session, engine, Base
from flask import current_app
from flask.cli import with_appcontext  
from models import User, Marca, Producto, Comentario


def create_tables():
    Base.metadata.drop_all(bind=engine, tables=[Producto.__table__])
    Base.metadata.drop_all(bind=engine, tables=[Marca.__table__])
    Base.metadata.drop_all(bind=engine, tables=[User.__table__])
    Base.metadata.drop_all(bind=engine, tables=[Comentario.__table__])
    Base.metadata.create_all(engine)
    
    session = Session()

    co1 = Comentario("Mikel", "El servicio funciona muy bien, muy contento con el envía.")
    co2 = Comentario("Irati", "Gracias a esta página, obtengo los mejores productos para mi restaurante.")
    co3 = Comentario("Jon", "Compré todo tipo de productos y todos estaban en perfectas condificones.")
    co4 = Comentario("Ane", "Me parece una grán página.")
    co5 = Comentario("Iker", "Estoy muy satisfecho con las compras realizadas.")
    co6 = Comentario("Uxue", "Estoy alucinando con la rapidez del envío. Una gozada comprar aquí.")
    
    m1 = Marca("CocaCola")
    m2 = Marca("Mahou") 
    m3 = Marca("Frotaleza") 
    m4 = Marca("Lipton") 
    m5 = Marca("Arbequina") 
    m6 = Marca("Bezoya") 
    m7 = Marca("Fanta") 

    p1 = Producto(m1, 2024, "Te recomendamos que siempre leas las etiquetas, advertencias e instrucciones del embalaje del producto antes de utilizarlo o consumirlo, ya que podrás encontrar información más detallada y actualizada sobre el mismo.", 10.90, 9, "https://www.tutrebol.es/53507-large_default/refresco-lata-coca-cola-pack-12x330-ml.jpg" )
    p2 = Producto(m2, 2024, "Te recomendamos que siempre leas las etiquetas, advertencias e instrucciones del embalaje del producto antes de utilizarlo o consumirlo, ya que podrás encontrar información más detallada y actualizada sobre el mismo.", 7.90, 9, "https://m.media-amazon.com/images/I/8197BSbJl4L._AC_SL1500_.jpg" )
    
    p4 = Producto(m4, 2025, "50 sobres de te Lipton. Super pack ahorro.", 5, 14, "http://gomart.pk/image/cache/data/incoming/Images/1486/lipton-yellow-label-tea-bag-black-50-sachet-pack-gomart-pakistan-1444-500x500.jpg")
    p5 = Producto(m5, 2026, "Pack de 6 botellines de aceite en oliva virgen extra.", 25.98, 9, "https://olivizate.com/tienda/223-large_default/pack-de-6-botellas-arbequina.jpg") 
    p6 = Producto(m6, 2024, "Pack de 6 botellas de  1 L. ", 3.99, 25, "https://cdn.metro-group.com/es/es_pim_59271001001_01.png?w=400&h=400&mode=pad")


    session.add(co1)
    session.add(co2)
    session.add(co3)
    session.add(co4)
    session.add(co5)
    session.add(co6)

    session.add(m1)
    session.add(m2)
    session.add(m3)
    session.add(m4)
    session.add(m5)
    session.add(m6)
    session.add(m7)

    session.add(p1)
    session.add(p2)
  
    session.add(p4)
    session.add(p5)
    session.commit()
    
    print("SE HAN AÑADIDO LOS DATOS CORRECTAMENTE...")
    session.close()