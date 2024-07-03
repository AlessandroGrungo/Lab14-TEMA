from database.DB_connect import DBConnect
from model.Gene import Gene


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllGeni():
        result = []
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""SELECT * FROM genes""")
        for row in cursor.fetchall():
            result.append(Gene(row["GeneID"], row["Function"], row["Essential"], row["Chromosome"]))
        cursor.close()
        conn.close()
        return result

    # Un arco collega due cromosomi diversi solo se i due cromosomi contengono due geni (uno per cromosoma)
    # che compaiono (nello stesso ordine) nella tabella interactions. Si noti che, per ciascun cromosoma, possono
    # esistere più geni, e ciascuno di essi potrebbe essere presente più volte (associato a function diverse).
    # Il peso di ciascun arco dovrà essere calcolato come la somma algebrica della correlazione (tabella
    # interactions, campo Expression_Corr), facendo attenzione a contare ogni coppia di geni una sola volta.

    @staticmethod
    def getGeniConnessi():
        result = []
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select g1.GeneID as Gene1, g2.GeneID as Gene2, i.Expression_Corr
                    FROM genes g1, genes g2, interactions i 
                    where  g1.GeneID = i.GeneID1 and g2.GeneID = i.GeneID2  
                    and g2.Chromosome != g1.Chromosome
                    and g2.Chromosome>0
                    and g1.Chromosome>0
                    group by g1.GeneID, g2.GeneID
                        """
        cursor.execute(query)
        for row in cursor.fetchall():
            result.append(((row["Gene1"]), row["Gene2"], float(row["Expression_Corr"])))
        cursor.close()
        conn.close()
        return result

